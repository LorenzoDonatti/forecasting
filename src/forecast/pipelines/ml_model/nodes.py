"""
This is a boilerplate pipeline 'ml_model'
generated using Kedro 0.18.7
"""

from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from kedro.extras.datasets.matplotlib import MatplotlibWriter

import lightgbm
from lightgbm import LGBMRegressor
from math import sqrt
from sklearn.metrics import mean_absolute_percentage_error

import optuna
import json

import influxdb_client
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

from influxdb_client.client.write.dataframe_serializer import data_frame_to_list_of_points


def splitdata(pot_SA:pd.DataFrame) -> json:

  train = pot_SA.iloc[:-7*24,:]
  test = pot_SA.iloc[-7*24:,:]

  # restructure into samples of daily data shape is [samples, hours, feature]
  train = np.array(np.split(train, len(train)/24))
  test = np.array(np.split(test, len(test)/24))

  split = {"train": train.tolist(),
           "test": test.tolist()}
  
  split = json.dumps(split)  # use dump() to write array into file

  return split


def trainforecasting(split:json, n_input:int, n_out:int) -> json:

  train = np.asarray(json.loads(split)["train"])

  # flatten data
  data = train.reshape((train.shape[0]*train.shape[1], train.shape[2]))
  x_train, y_train = list(), list()
  in_start = 0
  # step over the entire history one time step at a time
  for _ in range(len(data)):
    # define the end of the input sequence
    in_end = in_start + n_input
    out_end = in_end + n_out
    # ensure we have enough data for this instance
    if out_end <= len(data):
      x_input = data[in_start:in_end, :]
      x_train.append(x_input)
      y_train.append(data[in_end:out_end, 0])
    # move along one time step of 1 hour
    in_start += 1

  x_train, y_train = np.array(x_train), np.array(y_train)  

  x_train= np.reshape(x_train, (x_train.shape[0]*x_train.shape[1], x_train.shape[2]))
  y_train = np.reshape(y_train, (y_train.shape[0]*y_train.shape[1],))

  train_data = {"x_train": x_train.tolist(),
                "y_train": y_train.tolist()}
  
  train_data = json.dumps(train_data)
  
  return train_data
  

def optimize(train_data:json, split:json, n_input:int) -> json:

  train = np.asarray(json.loads(split)["train"])
  test = np.asarray(json.loads(split)["test"])

  x_train = np.asarray(json.loads(train_data)["x_train"])
  y_train = np.asarray(json.loads(train_data)["y_train"])

  def objective(trial):
    param = {
        "objective": "regression",
        "metric": "mape",
        "verbosity": -1,
        "boosting_type": "gbdt",
        "lambda_l1": trial.suggest_float("lambda_l1", 1e-8, 10.0, log=True),
        "lambda_l2": trial.suggest_float("lambda_l2", 1e-8, 10.0, log=True),
        "num_leaves": trial.suggest_int("num_leaves", 2, 1000),
        "num_estimators": trial.suggest_int("num_estimators", 2, 1000),
        "feature_fraction": trial.suggest_float("feature_fraction", 0.4, 1.0),
        "bagging_fraction": trial.suggest_float("bagging_fraction", 0.4, 1.0),
        "bagging_freq": trial.suggest_int("bagging_freq", 1, 7),
        "min_child_samples": trial.suggest_int("min_child_samples", 5, 100),
        }

    lgbm = LGBMRegressor(**param)
    lgbm.fit(x_train, y_train)

    # lista de horas
    history = [x for x in train]
    predictions_lgbm = []
    for i in range(len(test)):
      # predict
      data = np.array(history)
      data = data.reshape((data.shape[0]*data.shape[1], data.shape[2]))
      # guarda na lista
      input_x = data[-n_input:, :]
      yhat_reg = lgbm.predict(input_x)
    # forecast the next week
      predictions_lgbm.append(yhat_reg)
      history.append(test[i, :])
    # evaluate predictions hours for each day
    predictions_lgbm = np.array(predictions_lgbm)

    mape = mean_absolute_percentage_error(test[:,:,0].flatten(), predictions_lgbm.flatten())
    return mape

  study = optuna.create_study(direction="minimize")
  study.optimize(objective, n_trials=5)

  best_params = json.dumps(study.best_params)
  return best_params


def fitmodel(train_data:json, best_params: json) -> lightgbm.LGBMRegressor:

  x_train = np.asarray(json.loads(train_data)["x_train"])
  y_train = np.asarray(json.loads(train_data)["y_train"])

  best_params = json.loads(best_params)

  lgbm = lightgbm.LGBMRegressor(**best_params)
  lgbm.fit(x_train, y_train)

  return lgbm


def predict(lgbm:lightgbm.sklearn.LGBMRegressor,split:json, n_input:int) -> tuple[pd.DataFrame, dict[str,Any]]:

  train = np.asarray(json.loads(split)["train"])
  test = np.asarray(json.loads(split)["test"])

  history = [x for x in train]
  predictions_lgbm = []
  for i in range(len(test)):
    # predict
    data = np.array(history)
    data = data.reshape((data.shape[0]*data.shape[1], data.shape[2]))
    # guarda na lista
    input_x = data[-n_input:, :]
    yhat_reg = lgbm.predict(input_x)
    # forecast the next week
    predictions_lgbm.append(yhat_reg)
    history.append(test[i, :])
    # evaluate predictions hours for each day

  mape = mean_absolute_percentage_error(test[:,:,0].flatten(), np.array(predictions_lgbm).flatten())
  metrics = {"MAPE": mape}
  mlf_metrics = {"accurracy": {"value": mape, "step": 1}}

  predictions_lgbm = pd.DataFrame(np.array(predictions_lgbm))

  return [predictions_lgbm, metrics]


def writedata(data:pd.DataFrame, predictions_lgbm:pd.DataFrame, dev_id:str):

  bucket = "mux-energia-telemedicao-b-predicts"
  org = "fox-iot"
  token = "j5e67MfZPqCGIrepobO2iJs-nOB-4JEBoW_QBfd0Hu7ohNZRzv_Bi59L_2tQwWr-dhD2CMrzRlycabepUxjNKg=="
  # Store the URL of your InfluxDB instance
  url="https://influxdb-analytics.dev.spinon.com.br"

  predictions_lgbm = predictions_lgbm.to_numpy().flatten()

  print(data[dev_id])
  print(predictions_lgbm)

  data = data.iloc[-7*24:,:]
  data[dev_id] = predictions_lgbm
  
  client = influxdb_client.InfluxDBClient(
      url=url,
      token=token,
      org=org,
      timeout=10_000
  )

  write_api = client.write_api(write_options=WriteOptions(batch_size=1000, 
                                                          flush_interval=10_000,
                                                          jitter_interval=2_000,
                                                          retry_interval=5_000))

  # Convert the DataFrame to InfluxDB-compatible data points
  data_points = []
  for _, row in data.iterrows():
      point = Point('kedro_teste').field(row['_field'], row[dev_id]).tag("dev_id", dev_id).time(row["_time"])
      data_points.append(point)

  # Write the data points to InfluxDB
  write_api = client.write_api(write_options=SYNCHRONOUS)
  write_api.write(bucket=bucket, org=org, record=data_points)

  # Close the InfluxDB client
  client.close()

  return None


