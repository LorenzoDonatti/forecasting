"""
This is a boilerplate pipeline 'data_manipulation'
generated using Kedro 0.18.7
"""

from typing import Any, Dict, Tuple

from prophet import Prophet
import numpy as np
import pandas as pd
from datetime import date

from math import sqrt

def preprocessdata(df1: pd.DataFrame, df2: pd.DataFrame, df3: pd.DataFrame, df4: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    col_temp = df4.columns*df4.columns.str.contains('TEMPERATURA DO AR')
    col_temp = col_temp.drop('')[0]

    col_umidade = df4.columns*df4.columns.str.contains('UMIDADE RELATIVA')
    col_umidade = col_umidade.drop('')[0]

    col_chuva = df4.columns*df4.columns.str.contains('PRECIPITAÇÃO')
    col_chuva = col_chuva.drop('')[0]

    df4 = df4[['Data', 'Hora UTC', col_temp,col_umidade,col_chuva]]

    df = pd.concat([df1,df2,df3])

    num_validos = df.notna().sum()
    num_validos = num_validos[num_validos==0].index
    ######Valores que serão removidos
    df.drop(columns=num_validos, inplace=True)

    return df, df4

def changetype(df: pd.DataFrame, df4:pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
  #Colocando na lista todas as colunas a serem alteradas
  colunas = df.iloc[:,3:].columns
  etc = np.where(colunas.str.contains('ETC')==True)[0]

  for col in colunas:
    #Para a alteração de ',' para '.', a seguinte função é usada:
    if(df[col].dtype== 'O'):
      df[col] = df[col].str.replace(',', '.', 1)

      if col == colunas[etc]:
        df[col] = df[col].str.replace('.','').str.replace(',', '.')

    #Após isso, é possível a transformação para float.
    df[col] = pd.to_numeric(df[col])

  colunas = df4.iloc[:,2:].columns

  for col in colunas:
    #Para a alteração de ',' para '.', a seguinte função é usada:
    if(df4[col].dtype== 'O'):
      df4[col] = df4[col].str.replace(',', '.', 1)

    #Após isso, é possível a transformação para float.
    df4[col] = pd.to_numeric(df4[col])

  df['Data'] = df['Data'] + ' ' + df['Hora']
  df['Data'] = pd.to_datetime(df['Data'], format="%d/%m/%Y %H:%M:%S")

  df.drop(columns=['Hora','UC'], inplace = True)

  df4['Data'] = df4['Data'] + ' ' + df4['Hora UTC'].str[:4]
  df4['Data'] = pd.to_datetime(df4['Data'], format = "%Y/%m/%d %H%M")

  df4.drop(columns=['Hora UTC'], inplace = True)

  return df, df4

def clean_energy(df:pd.DataFrame) -> pd.DataFrame:
  array = df['ETC - Energia consumida (kWh)'].to_numpy()
  new_array = []
  for i in range(len(df.index)):
    if i==0:
      new_array.append(0)
    if i > 0:
      new_array.append((array[i] - array[i-1]))

  df['ETC - Energia consumida (kWh)'] = new_array
  return df

def removeless24(df:pd.DataFrame, df4:pd.DataFrame) -> pd.DataFrame:
  #pot_SA = pd.Series.to_frame(df.groupby(df['Data'].dt.to_period('H'))['SA - Potência aparente na fase A (VA)'].mean())
  pot_SA = pd.Series.to_frame(df.groupby(df['Data'].dt.to_period('H'))['ETC - Energia consumida (kWh)'].mean())
  pot_SA.index = pot_SA.index.to_timestamp()

  drop = pot_SA.index.strftime('%Y-%m-%d').value_counts()
  drop = drop[drop<24].index

  for d in drop:
    pot_SA.drop(index = pot_SA[pot_SA.index.strftime('%Y-%m-%d') == d].index, inplace=True)

  df4 = df4[df4['Data'].isin(pot_SA.index.values)==True].copy()
  df4.index = df4['Data']
  df4.drop(columns='Data',inplace=True)

  pot_SA = pot_SA.merge(df4, left_index=True, right_index=True)  

  return pot_SA

'''def mergedata(pot_SA:pd.DataFrame,df4:pd.DataFrame) -> pd.DataFrame:

  df4 = df4[df4['Data'].isin(pot_SA.index.values)==True].copy()
  df4.index = df4['Data']
  df4.drop(columns='Data',inplace=True)

  pot_SA = pot_SA.merge(df4, left_index=True, right_index=True)

  return pot_SA'''

def addfeatures(pot_SA:pd.DataFrame) -> pd.DataFrame:
  pot_SA['Data'] = pot_SA['Data'].apply(pd.to_datetime)
  print(pot_SA.dtypes)

  '''pot_SA['hour'] = pot_SA.index.hour
  pot_SA['dayofweek'] = pot_SA.index.dayofweek
  pot_SA['quarter'] = pot_SA.index.quarter
  pot_SA['month'] = pot_SA.index.month
  pot_SA['dayofmonth'] = pot_SA.index.day'''
  
  pot_SA['hour'] = pot_SA['Data'].dt.hour
  pot_SA['dayofweek'] = pot_SA['Data'].dt.dayofweek
  pot_SA['quarter'] = pot_SA['Data'].dt.quarter
  pot_SA['month'] = pot_SA['Data'].dt.month
  pot_SA['dayofmonth'] = pot_SA['Data'].dt.day

  horizon = 24*7
  temp_df = pot_SA.reset_index()
  #temp_df = temp_df[['Data', 'SA - Potência aparente na fase A (VA)']]
  temp_df = temp_df[['Data', 'ETC - Energia consumida (kWh)']]
  #temp_df.rename(columns={'Data': 'ds', 'SA - Potência aparente na fase A (VA)': 'y'}, inplace=True)
  temp_df.rename(columns={'Data': 'ds', 'ETC - Energia consumida (kWh)': 'y'}, inplace=True)

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

  pot_SA = pot_SA.merge(predictions, left_on='Data', right_on='ds')
  pot_SA.drop(columns= ['ds','Data'], inplace=True)

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

def normalizingweather(pot_SA:pd.DataFrame) -> pd.DataFrame:

  categorical_columns = ['hour','dayofweek','quarter','dayofmonth']
  numerical_columns = ['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)','UMIDADE RELATIVA DO AR, HORARIA (%)','PRECIPITAÇÃO TOTAL, HORÁRIO (mm)']

  for column in numerical_columns: 
    pot_SA[column] = pot_SA[column]  / pot_SA[column].abs().max() 

  return pot_SA