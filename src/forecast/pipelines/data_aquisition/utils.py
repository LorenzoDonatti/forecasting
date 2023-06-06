import yaml
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

import warnings
from influxdb_client.client.warnings import MissingPivotFunction

def get_str(bucket:str, org:str,token:str, url:str):

    client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org,
    timeout=10_000
    )

    # Query script
    query_api = client.query_api()
    query = 'from(bucket:"mux-energia-telemedicao-b")\
    |> range(start: -100d, stop: now())\
    |> filter(fn: (r) => r["_measurement"] == "payload")\
    |> filter(fn: (r) => r["_field"] == "consumed_total_energy")\
    |> keyValues(keyColumns: ["dev_id"])\
    |> keep(columns: ["dev_id"])'

    result = client.query_api().query_data_frame(org=org, query=query)
    dev_id = result["dev_id"].to_list()

    return dev_id


def generate_param(dev_id:str):
    
    id = dev_id.split('-')[1]

    data = """
    dev_id_{num}: {dev}
    
    """.format(num=id,dev=dev_id)

    names = yaml.safe_load(data)

    with open('/home/ldonatti/teste/forecast/conf/base/parameters.yml', 'a') as file:
        yaml.safe_dump(names, file)

    return id
    

def create_catalog(names:set, id:str, kind:str):

    for name in names:
        if kind == 'csv':
            data = """
            {name}_{id}:
                type: pandas.CSVDataSet
                filepath: /home/ldonatti/teste/forecast/data/03_primary/{name}_{id}.csv
                save_args:
                    index: False
                    date_format: "%Y/%m/%d %H%M"
                    decimal: .
                """.format(name=name,id=id)

        else: 
            if name == 'best_model':
                data = """
                {name}_{id}:
                    type: pickle.PickleDataSet
                    filepath: /home/ldonatti/teste/forecast/data/06_models/{name}_{id}.pkl
                """.format(name=name,id=id)
            elif name == 'predictions_lgbm':
                data = """
                {name}_{id}:
                    type: pandas.CSVDataSet
                    filepath: /home/ldonatti/teste/forecast/data/07_model_output/{name}_{id}.csv
                    save_args:
                        index: False
                        decimal: .
                    """.format(name=name,id=id)
                

            else:    
                data = """
                {name}_{id}:
                    type: json.JSONDataSet
                    filepath: /home/ldonatti/teste/forecast/data/04_feature/{name}_{id}.json
                    """.format(name=name,id=id)


        data = yaml.safe_load(data)

        with open('/home/ldonatti/teste/forecast/conf/base/catalog.yml', 'a') as file:
            yaml.safe_dump(data, file)
     
    return None    

