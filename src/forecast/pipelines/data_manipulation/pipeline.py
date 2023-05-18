"""
This is a boilerplate pipeline 'data_manipulation'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocessdata, changetype, clean_energy, removeless24, addfeatures, normalizingweather

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocessdata,
                inputs=["dataset_01_03_22", "dataset_04_06_22", "dataset_07_12_22","dataset_temp", "params:search_columns"],
                outputs=["df","df4_e"],
                name="preprocessdata",
            ),
            node(
                func=changetype,
                inputs=["df", "df4_e"],
                outputs=["df_type","df4_type"],
                name="changetype",
            ),
            node(
                func=clean_energy,
                inputs="df_type",
                outputs="df_entype",
                name="clean_energy",
            ),
            node(
                func=removeless24,
                inputs=["df_entype","df4_type","params:column_to_forecast"],
                outputs="pot_SA",
                name="removeless24",
            ),
            #node(
            #    func=mergedata,
            #    inputs=["pot_SA", "df4_type"],
            #    outputs="pot_SA_merge",
            #    name="mergedata",
            #),            
            node(
                func=addfeatures,
                inputs=["pot_SA","params:column_to_forecast"],
                outputs="pot_SA_add",
                name="addfeatures",
            ),
            node(
                func=normalizingweather,
                inputs=["pot_SA_add","params:numerical_columns"],
                outputs="pot_SA_norm",
                name="normalizingweather",
            ),
        ]
    )