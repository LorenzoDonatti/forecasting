"""
This is a boilerplate pipeline 'data_aquisition'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import downfiles

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=downfiles,
                inputs=["params:links", "params:outputs"],
                outputs=None,
                name="downfiles",
            ),
        ]
    )
