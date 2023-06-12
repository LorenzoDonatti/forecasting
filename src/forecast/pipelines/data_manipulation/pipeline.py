"""
This is a boilerplate pipeline 'data_manipulation'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline
from .nodes import preprocessdata, clean_energy, removeless24, addfeatures

import forecast.pipelines.data_aquisition.utils as utils

def create_pipeline(**kwargs) -> Pipeline:
    data_manipulation = pipeline(
        [
            node(
                func=preprocessdata,
                #inputs=["data","dataset_temp", "params:search_columns"],
                inputs=["data", "params:search_columns"],
                #outputs=["df","df4"],
                outputs="df",
                name="preprocessdata",
            ),
            node(
                func=clean_energy,
                inputs="df",
                outputs="df_type",
                name="clean_energy",
            ),
            node(
                func=removeless24,
                #inputs=["df_type","df4","params:column_to_forecast"],
                inputs=["df_type","params:column_to_forecast"],
                outputs="pot_SA",
                name="removeless24",
            ),           
            node(
                func=addfeatures,
                inputs=["pot_SA","params:column_to_forecast"],
                outputs="pot_SA_add",
                name="addfeatures",
            ),
        ]
    )
    dm_pipeline = []

    dev_id = utils.get_str(bucket='mux-energia-telemedicao-b', 
                           org='fox-iot',
                           token= 'j5e67MfZPqCGIrepobO2iJs-nOB-4JEBoW_QBfd0Hu7ohNZRzv_Bi59L_2tQwWr-dhD2CMrzRlycabepUxjNKg==',
                           url= 'https://influxdb-analytics.dev.spinon.com.br')
                           
    for i in range(len(dev_id[:2])):
        id = utils.generate_param(dev_id[i])
        #utils.create_catalog(data_manipulation.all_outputs(), id, 'csv')
        dm_pipeline.append(pipeline(
            pipe=data_manipulation,
            inputs={'data':'data_{}'.format(id),
                    #'dataset_temp':'dataset_temp',
                    },
            outputs={'df':'df_{}'.format(id),
                     'df_type':'df_type_{}'.format(id),
                     'pot_SA':'pot_SA_{}'.format(id),
                     'pot_SA_add':'pot_SA_add_{}'.format(id),
                     #'df4':'df4_{}'.format(id)
                    },
            namespace="teste_dm_{}".format(i),
            parameters={"params:search_columns":"params:search_columns",
                        "params:column_to_forecast":"params:column_to_forecast",
            }
        ))

    return sum(dm_pipeline)