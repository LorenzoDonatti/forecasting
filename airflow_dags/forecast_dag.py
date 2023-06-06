from collections import defaultdict

from pathlib import Path

from airflow import DAG
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.version import version
from datetime import datetime, timedelta

from kedro.framework.session import KedroSession
from kedro.framework.project import configure_project


class KedroOperator(BaseOperator):

    @apply_defaults
    def __init__(
        self,
        package_name: str,
        pipeline_name: str,
        node_name: str,
        project_path: str,
        env: str,
        *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.package_name = package_name
        self.pipeline_name = pipeline_name
        self.node_name = node_name
        self.project_path = project_path
        self.env = env

    def execute(self, context):
        configure_project(self.package_name)
        with KedroSession.create(self.package_name,
                                 self.project_path,
                                 env=self.env) as session:
            session.run(self.pipeline_name, node_names=[self.node_name])

# Kedro settings required to run your pipeline
env = "local"
pipeline_name = "__default__"
project_path = Path.cwd()
package_name = "forecast"

# Default settings applied to all tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Using a DAG context manager, you don't have to specify the dag property of each task
with DAG(
    "forecast",
    start_date=datetime(2019, 1, 1),
    max_active_runs=3,
    schedule_interval=timedelta(minutes=30),  # https://airflow.apache.org/docs/stable/scheduler.html#dag-runs
    default_args=default_args,
    catchup=False # enable if you don't want historical dag runs to run
) as dag:

    tasks = {}

    tasks["teste-da-0-downfiles"] = KedroOperator(
        task_id="teste-da-0-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_0.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-1-downfiles"] = KedroOperator(
        task_id="teste-da-1-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_1.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-0-preprocessdata"] = KedroOperator(
        task_id="teste-dm-0-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_0.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-1-preprocessdata"] = KedroOperator(
        task_id="teste-dm-1-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_1.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-0-clean-energy"] = KedroOperator(
        task_id="teste-dm-0-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_0.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-1-clean-energy"] = KedroOperator(
        task_id="teste-dm-1-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_1.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-0-removeless24"] = KedroOperator(
        task_id="teste-dm-0-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_0.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-1-removeless24"] = KedroOperator(
        task_id="teste-dm-1-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_1.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-0-addfeatures"] = KedroOperator(
        task_id="teste-dm-0-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_0.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-1-addfeatures"] = KedroOperator(
        task_id="teste-dm-1-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_1.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-0-splitdata"] = KedroOperator(
        task_id="teste-ml-0-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_0.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-1-splitdata"] = KedroOperator(
        task_id="teste-ml-1-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_1.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-0-trainforecasting"] = KedroOperator(
        task_id="teste-ml-0-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_0.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-1-trainforecasting"] = KedroOperator(
        task_id="teste-ml-1-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_1.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-0-optimize"] = KedroOperator(
        task_id="teste-ml-0-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_0.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-1-optimize"] = KedroOperator(
        task_id="teste-ml-1-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_1.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-0-fitmodel"] = KedroOperator(
        task_id="teste-ml-0-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_0.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-1-fitmodel"] = KedroOperator(
        task_id="teste-ml-1-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_1.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-0-predict"] = KedroOperator(
        task_id="teste-ml-0-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_0.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-1-predict"] = KedroOperator(
        task_id="teste-ml-1-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_1.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-0-plotresults"] = KedroOperator(
        task_id="teste-ml-0-plotresults",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_0.plotresults",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-1-plotresults"] = KedroOperator(
        task_id="teste-ml-1-plotresults",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_1.plotresults",
        project_path=project_path,
        env=env,
    )



    tasks["teste-ml-1-optimize"] >> tasks["teste-ml-1-fitmodel"]

    tasks["teste-ml-1-trainforecasting"] >> tasks["teste-ml-1-fitmodel"]

    tasks["teste-ml-1-trainforecasting"] >> tasks["teste-ml-1-optimize"]

    tasks["teste-ml-1-predict"] >> tasks["teste-ml-1-plotresults"]

    tasks["teste-ml-1-splitdata"] >> tasks["teste-ml-1-plotresults"]

    tasks["teste-ml-1-splitdata"] >> tasks["teste-ml-1-optimize"]

    tasks["teste-ml-1-splitdata"] >> tasks["teste-ml-1-predict"]

    tasks["teste-ml-1-splitdata"] >> tasks["teste-ml-1-trainforecasting"]

    tasks["teste-ml-0-predict"] >> tasks["teste-ml-0-plotresults"]

    tasks["teste-ml-0-splitdata"] >> tasks["teste-ml-0-plotresults"]

    tasks["teste-ml-0-splitdata"] >> tasks["teste-ml-0-optimize"]

    tasks["teste-ml-0-splitdata"] >> tasks["teste-ml-0-predict"]

    tasks["teste-ml-0-splitdata"] >> tasks["teste-ml-0-trainforecasting"]

    tasks["teste-dm-0-clean-energy"] >> tasks["teste-dm-0-removeless24"]

    tasks["teste-dm-0-preprocessdata"] >> tasks["teste-dm-0-removeless24"]

    tasks["teste-dm-0-preprocessdata"] >> tasks["teste-dm-0-clean-energy"]

    tasks["teste-ml-0-trainforecasting"] >> tasks["teste-ml-0-optimize"]

    tasks["teste-ml-0-trainforecasting"] >> tasks["teste-ml-0-fitmodel"]

    tasks["teste-dm-0-addfeatures"] >> tasks["teste-ml-0-splitdata"]

    tasks["teste-dm-0-removeless24"] >> tasks["teste-dm-0-addfeatures"]

    tasks["teste-ml-0-fitmodel"] >> tasks["teste-ml-0-predict"]

    tasks["teste-da-0-downfiles"] >> tasks["teste-dm-0-preprocessdata"]

    tasks["teste-dm-1-preprocessdata"] >> tasks["teste-dm-1-clean-energy"]

    tasks["teste-dm-1-preprocessdata"] >> tasks["teste-dm-1-removeless24"]

    tasks["teste-ml-1-fitmodel"] >> tasks["teste-ml-1-predict"]

    tasks["teste-da-1-downfiles"] >> tasks["teste-dm-1-preprocessdata"]

    tasks["teste-dm-1-addfeatures"] >> tasks["teste-ml-1-splitdata"]

    tasks["teste-ml-0-optimize"] >> tasks["teste-ml-0-fitmodel"]

    tasks["teste-dm-1-removeless24"] >> tasks["teste-dm-1-addfeatures"]

    tasks["teste-dm-1-clean-energy"] >> tasks["teste-dm-1-removeless24"]
