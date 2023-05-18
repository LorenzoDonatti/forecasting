"""
This is a boilerplate pipeline 'ml_model'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import splitdata, trainforecasting, optimize, fitmodel, predict, plotresults


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=splitdata,
                inputs="pot_SA_norm",
                outputs="split",
                name="splitdata",
            ),
            node(
                func=trainforecasting,
                inputs="split",
                outputs="train_data",
                name="trainforecasting",
            ),
            node(
                func=optimize,
                inputs=["train_data", "split"],
                outputs="best_params",
                name="optimize",
            ),
            node(
                func=fitmodel,
                inputs=["train_data", "best_params"],
                outputs="best_model@pkl",
                name="fitmodel",
            ),
            node(
                func=predict,
                inputs=["best_model@pkl","split"],
                outputs=["predictions_lgbm","metrics", "mlf_metrics"],
                name="predict",
            ),
            node(
                func=plotresults,
                inputs=["predictions_lgbm", "split"],
                outputs=None,
                name="plotresults",
            ),
        ]
    )