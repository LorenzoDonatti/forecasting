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
pipeline_name = "ml_model"
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

    tasks["splitdata"] = KedroOperator(
        task_id="splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["trainforecasting"] = KedroOperator(
        task_id="trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["optimize"] = KedroOperator(
        task_id="optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="optimize",
        project_path=project_path,
        env=env,
    )

    tasks["fitmodel"] = KedroOperator(
        task_id="fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["predict"] = KedroOperator(
        task_id="predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="predict",
        project_path=project_path,
        env=env,
    )

    tasks["plotresults"] = KedroOperator(
        task_id="plotresults",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="plotresults",
        project_path=project_path,
        env=env,
    )



    tasks["splitdata"] >> tasks["trainforecasting"]

    tasks["splitdata"] >> tasks["optimize"]

    tasks["splitdata"] >> tasks["fitmodel"]

    tasks["splitdata"] >> tasks["predict"]

    tasks["splitdata"] >> tasks["plotresults"]

    tasks["trainforecasting"] >> tasks["optimize"]

    tasks["trainforecasting"] >> tasks["fitmodel"]

    tasks["optimize"] >> tasks["fitmodel"]

    tasks["fitmodel"] >> tasks["predict"]

    tasks["predict"] >> tasks["plotresults"]
