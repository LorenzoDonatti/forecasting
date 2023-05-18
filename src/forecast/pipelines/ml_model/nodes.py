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

#from optuna.integration.mlflow import MLflowCallback   Descomentar caso seja necessário a integração de todos os studies do optuna
import mlflow
from mlflow.models.signature import infer_signature

def splitdata(pot_SA:pd.DataFrame) -> json:

  train = pot_SA.iloc[-127*24:-7*24,:]
  test = pot_SA.iloc[-7*24:,:]

  # restructure into samples of daily data shape is [samples, hours, feature]
  train = np.array(np.split(train, len(train)/24))
  test = np.array(np.split(test, len(test)/24))

  split = {"train": train.tolist(),
           "test": test.tolist()}
  
  split = json.dumps(split)  # use dump() to write array into file

  return split

def trainforecasting(split:json) -> json:

  #train = np.loadtxt('/home/ldonatti/teste/forecast/data/04_feature/train.txt')
  #train = train.reshape((int(train.shape[0]/24), 24, train.shape[1]))

  train = np.asarray(json.loads(split)["train"])

  n_input = 24
  n_out = 24
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
  

def optimize(train_data:json, split:json) -> json:

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

    n_input = 24
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

  #mlflc = MLflowCallback(tracking_uri= mlflow.get_tracking_uri(), metric_name='mape')     optuna studies no mlflow
  #mlflow.end_run()

  study = optuna.create_study(direction="minimize")
  study.optimize(objective, n_trials=5)#, callbacks=[mlflc])

  mlflow.log_param("best_params", study.best_params)

  best_params = json.dumps(study.best_params)
  return best_params

  #return study.best_params

def fitmodel(train_data:json, best_params: json,) -> lightgbm.LGBMRegressor:

  x_train = np.asarray(json.loads(train_data)["x_train"])
  y_train = np.asarray(json.loads(train_data)["y_train"])

  best_params = json.loads(best_params)

  lgbm = lightgbm.LGBMRegressor(**best_params)
  lgbm.fit(x_train, y_train)

  signature = infer_signature(x_train, lgbm.predict(x_train))
  mlflow.sklearn.log_model(lgbm, "LGBM", signature=signature)

  return lgbm

def predict(lgbm:lightgbm.sklearn.LGBMRegressor,split:json) -> tuple[np.array, dict[str,Any], dict[str,Any]]:

  print(type(lgbm))
  train = np.asarray(json.loads(split)["train"])
  test = np.asarray(json.loads(split)["test"])

  n_input = 24
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
  metrics = {"MAPE": mape}
  mlf_metrics = {"accurracy": {"value": mape, "step": 1}}

  return [predictions_lgbm, metrics, mlf_metrics]


def plotresults(predictions_lgbm:np.array, split:json):

  test = np.asarray(json.loads(split)["test"])

  fig, axis = plt.subplots(1, 1, figsize=[20,10])

  axis.plot(np.arange(0,24*7), test[:,:,0].flatten()[24*0:24*7], color = 'black', label='Actual')
  axis.plot(np.arange(0,24*7), predictions_lgbm.flatten()[24*0:24*7],color ='red', label='Predicted',alpha=1)

  axis.set_title('24 hr Actual vs Predicted')
  
  axis.set_xlabel("Hour")
  axis.set_ylabel("Active Power [kW]")

  axis.legend()

  plot_writer = MatplotlibWriter(filepath="/home/ldonatti/teste/forecast/data/07_model_output/output_plot.png")
  plt.close()
  plot_writer.save(fig)