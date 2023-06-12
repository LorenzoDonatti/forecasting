"""
This is a boilerplate pipeline 'ml_model'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline
from .nodes import splitdata, trainforecasting, optimize, fitmodel, predict, plotresults

import forecast.pipelines.data_aquisition.utils as utils


def create_pipeline(**kwargs) -> Pipeline:
    ml_model = pipeline(
        [
            node(
                func=splitdata,
                inputs="pot_SA_add",
                outputs="split",
                name="splitdata",
            ),
            node(
                func=trainforecasting,
                inputs=["split","params:n_input","params:n_out"],
                outputs="train_data",
                name="trainforecasting",
            ),
            node(
                func=optimize,
                inputs=["train_data", "split", "params:n_input"],
                outputs="best_params",
                name="optimize",
            ),
            node(
                func=fitmodel,
                inputs=["train_data", "best_params"],
                outputs="best_model",
                name="fitmodel",
            ),
            node(
                func=predict,
                inputs=["best_model","split", "params:n_input"],
                outputs=["predictions_lgbm","metrics", "mlf_metrics"],
                name="predict",
            ),
            node(
                func=plotresults,
                inputs=["predictions_lgbm", "split", "params:dev_id"],
                outputs=None,
                name="plotresults",
            ),
        ]
    )
    ml_pipeline = []
    dev_id = utils.get_str(bucket='mux-energia-telemedicao-b', 
                           org='fox-iot',
                           token= 'j5e67MfZPqCGIrepobO2iJs-nOB-4JEBoW_QBfd0Hu7ohNZRzv_Bi59L_2tQwWr-dhD2CMrzRlycabepUxjNKg==',
                           url= 'https://influxdb-analytics.dev.spinon.com.br')
                           
    for i in range(len(dev_id[:2])):
        id = utils.generate_param(dev_id[i])
        #utils.create_catalog(ml_model.all_outputs(), id, 'json')
        ml_pipeline.append(pipeline(
            pipe=ml_model,
            inputs={'pot_SA_add':'pot_SA_add_{}'.format(id)},
            outputs={'split':'split_{}'.format(id),
                     'train_data':'train_data_{}'.format(id),
                     'best_params':'best_params_{}'.format(id),
                     'best_model':'best_model_{}'.format(id),
                     'predictions_lgbm':'predictions_lgbm_{}'.format(id),
                     'metrics':'metrics_{}'.format(id),
                    },
            namespace="teste_ml_{}".format(i),
            parameters={"params:n_input":"params:n_input",
                        "params:n_out":"params:n_out",
                        "params:dev_id":"params:dev_id_{}".format(id),
            }
        ))

    return sum(ml_pipeline)