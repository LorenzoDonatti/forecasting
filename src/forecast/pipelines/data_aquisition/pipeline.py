"""
This is a boilerplate pipeline 'data_aquisition'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline
from .nodes import downfiles

import forecast.pipelines.data_aquisition.utils as utils

def create_pipeline(**kwargs) -> Pipeline:
    data_aquisition =  pipeline(
        [
            node(
                func=downfiles,
                inputs=["params:bucket_read", "params:org","params:token_read", "params:url_read", "params:dev_id"],
                outputs="data",
                name="downfiles",
            ),
        ]
    )
    da_pipeline = []

    dev_id = utils.get_str(bucket='mux-energia-telemedicao-b', 
                           org='fox-iot',
                           token= 'j5e67MfZPqCGIrepobO2iJs-nOB-4JEBoW_QBfd0Hu7ohNZRzv_Bi59L_2tQwWr-dhD2CMrzRlycabepUxjNKg==',
                           url= 'https://influxdb-analytics.dev.spinon.com.br')

    for i in range(len(dev_id[:50])):
        id = utils.generate_param(dev_id[i])
        utils.create_catalog(data_aquisition.all_outputs(), id, 'csv')
        da_pipeline.append(pipeline(
            pipe=data_aquisition,
            outputs={'data':'data_{}'.format(id)},
            namespace="teste_da_{}".format(i),
            parameters={"params:bucket_read":"params:bucket_read", 
                        "params:org":"params:org",
                        "params:token_read":"params:token_read", 
                        "params:url_read":"params:url_read", 
                        "params:dev_id":"params:dev_id_{}".format(id),
                        }
        ))

    return sum(da_pipeline)