"""
This is a boilerplate pipeline 'data_manipulation'
generated using Kedro 0.18.7
"""

from typing import Any, Dict, Tuple

from prophet import Prophet
import pandas as pd

from math import sqrt

def preprocessdata(df: pd.DataFrame, searchfor:list) -> pd.DataFrame:

  cols = df.columns[df.columns.str.contains('|'.join(['fxrl','_time']))]
  df = df[cols]

  col = df.columns[df.columns.str.contains('fxrl')][0]
  df.rename(columns={col:'ETC - Energia consumida (kWh)'}, inplace=True)

  return df#, df4


def clean_energy(df:pd.DataFrame) -> pd.DataFrame:

  array = df.iloc[:,-1].to_numpy(dtype=float)
  new_array = []
  for i in range(len(df)):
    if i==0:
      new_array.append(0)
    if i > 0:
      new_array.append((array[i] - array[i-1]))
  
  df.iloc[:,-1] = new_array

  return df


def removeless24(pot_SA:pd.DataFrame, column:str) -> pd.DataFrame:
  pot_SA['_time'] = pot_SA['_time'].apply(pd.to_datetime)
  drop = pot_SA['_time'].dt.strftime('%Y-%m-%d').value_counts()
  drop = drop[drop<24].index
  for d in drop:
    pot_SA.drop(index = pot_SA[ pot_SA['_time'].dt.strftime('%Y-%m-%d') == d].index, inplace=True)
 
  return pot_SA


def addfeatures(pot_SA:pd.DataFrame, column:str) -> pd.DataFrame:

  pot_SA['_time'] = pot_SA['_time'].apply(pd.to_datetime)

  pot_SA['hour'] = pot_SA['_time'].dt.hour
  pot_SA['dayofweek'] = pot_SA['_time'].dt.dayofweek
  pot_SA['quarter'] = pot_SA['_time'].dt.quarter
  pot_SA['month'] = pot_SA['_time'].dt.month
  pot_SA['dayofmonth'] = pot_SA['_time'].dt.day

  horizon = 24*7
  temp_df = pot_SA.reset_index()

  temp_df = temp_df[['_time', column]]
  temp_df.rename(columns={'_time': 'ds', column: 'y'}, inplace=True)

  #take last week of the dataset for validation
  train, test = temp_df.iloc[:-horizon,:], temp_df.iloc[-horizon:,:]

  #define prophet model
  m = Prophet(
              growth='linear',
              seasonality_mode='additive',
              interval_width=0.95,
              daily_seasonality=True,
              weekly_seasonality=True,
              yearly_seasonality=False
          )
  #train prophet model
  m.fit(train)

  #extract features from data using prophet to predict train set
  predictions_train = m.predict(train.drop('y', axis=1))
  #extract features from data using prophet to predict test set
  predictions_test = m.predict(test.drop('y', axis=1))
  #merge train and test predictions
  predictions = pd.concat([predictions_train, predictions_test], axis=0)

  pot_SA = pot_SA.merge(predictions, left_on='_time', right_on='ds')
  pot_SA.drop(columns= ['ds','_time'], inplace=True)

  pot_SA['lag_1dia'] = pot_SA[pot_SA.columns.values[0]].shift(24)
  pot_SA['lag_23hrs'] = pot_SA[pot_SA.columns.values[0]].shift(23)
  pot_SA['lag_25hrs'] = pot_SA[pot_SA.columns.values[0]].shift(25)
  pot_SA['lag_7dias'] = pot_SA[pot_SA.columns.values[0]].shift(24*7)
  pot_SA['lag_28dias'] = pot_SA[pot_SA.columns.values[0]].shift(24*28)
  pot_SA['lag_90dias'] = pot_SA[pot_SA.columns.values[0]].shift(24*90)

  pot_SA['lag_1dia_y'] = pot_SA['yhat'].shift(24)
  pot_SA['lag_23hrs_y'] = pot_SA['yhat'].shift(23)
  pot_SA['lag_25hrs_y'] = pot_SA['yhat'].shift(25)
  pot_SA['lag_7dias_y'] = pot_SA['yhat'].shift(24*7)
  pot_SA['lag_28dias_y'] = pot_SA['yhat'].shift(24*28)
  pot_SA['lag_90dias_y'] = pot_SA['yhat'].shift(24*90)

  return pot_SA