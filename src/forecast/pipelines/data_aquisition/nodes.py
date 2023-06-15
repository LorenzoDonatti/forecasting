"""
This is a boilerplate pipeline 'data_aquisition'
generated using Kedro 0.18.7
"""

from typing import Any, Dict
import pandas as pd

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

import warnings
from influxdb_client.client.warnings import MissingPivotFunction


def downfiles(bucket:str, org:str,token:str, url:str, dev_id:str) -> pd.DataFrame:
    warnings.simplefilter("ignore", MissingPivotFunction)

    id = dev_id.split('-')[1]

    dev = [dev_id]
    dev = '[{}]'.format(', '.join('"{}"'.format(item) for item in dev))

    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org,
        timeout=100_000
    )

# Query script
    query_api = client.query_api()
    query = 'from(bucket:"mux-energia-telemedicao-b")\
    |> range(start: -60d, stop: now())\
    |> filter(fn: (r) => r["_measurement"] == "payload")\
    |> filter(fn: (r) => r["_field"] == "consumed_total_energy")\
    |> filter(fn: (r) => contains(value: r["dev_id"], set: {setf}))\
    |> aggregateWindow(every: 1h, fn: mean, createEmpty: false)\
    |> pivot(rowKey:["_time"], columnKey: ["dev_id"], valueColumn: "_value")\
    |> drop(columns:["_start", "_stop", "_measurement"])'.format(setf = dev)

    result = client.query_api().query_data_frame(org=org, query=query)
    #result.to_csv('data/03_primary/data_{name}.csv'.format(name=id))

    return result
