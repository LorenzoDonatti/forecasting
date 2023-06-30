"""
This is a boilerplate pipeline 'ml_model'
generated using Kedro 0.18.7
"""

from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd

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

import ray
from ray import tune
from ray.tune.search.optuna import OptunaSearch

import xgboost
from xgboost import XGBRegressor


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


#def trainforecasting(split:json, n_input:int, n_out:int) -> json:
def trainforecasting(split:json, n_input:int, n_out:int) -> tuple[pd.DataFrame, pd.DataFrame]:

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

  x_train, y_train = np.asarray(x_train), np.asarray(y_train)  

  x_train= np.reshape(x_train, (x_train.shape[0]*x_train.shape[1], x_train.shape[2]))
  y_train = np.reshape(y_train, (y_train.shape[0]*y_train.shape[1],))

  x_train_df = pd.DataFrame(x_train)
  y_train_df = pd.DataFrame(y_train)
  x_train = x_train_df.to_numpy()
  #train_data = {"x_train": x_train.tolist(),
  #              "y_train": y_train.tolist()}
  #train_data = json.dumps(train_data)
  
  return [x_train_df, y_train_df]
  

#def optimize(train_data:json, split:json, n_input:int) -> json:
def optimize(x_train:pd.DataFrame, y_train:pd.DataFrame, split:json, n_input:int) -> json:

  train = np.asarray(json.loads(split)["train"])
  test = np.asarray(json.loads(split)["test"])
  #x_train = np.asarray(json.loads(train_data)["x_train"])
  #y_train = np.asarray(json.loads(train_data)["y_train"])
  x_train = x_train.to_numpy()
  y_train = y_train.to_numpy().reshape(1,-1).T

  def objective(config):

    lgbm = XGBRegressor(**config)
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
    tune.report(mape=mape)

  analysis = tune.run(objective,
                      config = {"objective": "reg:squarederror",
                                'random_state': 48,
                                'n_estimators': tune.randint(50,500),
                                'reg_alpha': tune.loguniform(1e-3, 10.0),
                                'reg_lambda': tune.loguniform(1e-3, 10.0),
                                'colsample_bytree': tune.choice([0.3,0.4,0.5,0.6,0.7,0.8,0.9, 1.0]),
                                'subsample': tune.choice([0.4,0.5,0.6,0.7,0.8,1.0]),
                                'learning_rate': tune.choice([0.006,0.008,0.01,0.014,0.017,0.02]),
                                'max_depth': tune.choice([10,20,100]),
                                },
                      metric="mape", 
                      mode="min",
                      search_alg=OptunaSearch(),
                      num_samples=5,
                      resources_per_trial={"cpu": 1,
                                           "gpu": 1},
                      )

  best_params = json.dumps(analysis.best_config)
  ray.shutdown()
  return best_params

#def fitmodel(train_data:json, best_params: json) -> lightgbm.LGBMRegressor:
def fitmodel(x_train:pd.DataFrame, y_train:pd.DataFrame, best_params: json):

  #x_train = np.asarray(json.loads(train_data)["x_train"])
  #y_train = np.asarray(json.loads(train_data)["y_train"])
  x_train = x_train.to_numpy()
  y_train = y_train.to_numpy().reshape(1,-1).T

  best_params = json.loads(best_params)
  lgbm = XGBRegressor(**best_params, tree_method= 'gpu_hist')
  lgbm.fit(x_train, y_train)

  return lgbm


def predict(lgbm,split:json, n_input:int) -> tuple[pd.DataFrame, dict[str,Any]]:

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

  predictions_lgbm = pd.DataFrame(np.array(predictions_lgbm))

  return [predictions_lgbm, metrics]


def writedata(data:pd.DataFrame, predictions_lgbm:pd.DataFrame, bucket:str, org:str, token:str, url:str, dev_id:str):

  predictions_lgbm = predictions_lgbm.to_numpy().flatten()
  #data['_time'] = data['_time'].dt.tz_localize(None)

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


