from collections import defaultdict

from pathlib import Path

from airflow import DAG
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.version import version
from datetime import datetime, timedelta

from kedro.framework.session import KedroSession
from kedro.framework.project import configure_project

import airflow_utils
 
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
    #'on_success_callback': airflow_utils.send_discord_success_notification,
    #'on_retry_callback': airflow_utils.send_discord_retry_notification,
    #'on_failure_callback': airflow_utils.send_discord_fail_notification,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Using a DAG context manager, you don't have to specify the dag property of each task
with DAG(
    "forecast",
    start_date=datetime(2023, 1, 1),
    max_active_runs=2,
    concurrency=128,
    max_active_tasks=128,
    schedule_interval=timedelta(minutes=600),  # https://airflow.apache.org/docs/stable/scheduler.html#dag-runs
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

    tasks["teste-da-10-downfiles"] = KedroOperator(
        task_id="teste-da-10-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_10.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-11-downfiles"] = KedroOperator(
        task_id="teste-da-11-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_11.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-12-downfiles"] = KedroOperator(
        task_id="teste-da-12-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_12.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-13-downfiles"] = KedroOperator(
        task_id="teste-da-13-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_13.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-14-downfiles"] = KedroOperator(
        task_id="teste-da-14-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_14.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-15-downfiles"] = KedroOperator(
        task_id="teste-da-15-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_15.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-16-downfiles"] = KedroOperator(
        task_id="teste-da-16-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_16.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-17-downfiles"] = KedroOperator(
        task_id="teste-da-17-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_17.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-18-downfiles"] = KedroOperator(
        task_id="teste-da-18-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_18.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-19-downfiles"] = KedroOperator(
        task_id="teste-da-19-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_19.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-2-downfiles"] = KedroOperator(
        task_id="teste-da-2-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_2.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-20-downfiles"] = KedroOperator(
        task_id="teste-da-20-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_20.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-21-downfiles"] = KedroOperator(
        task_id="teste-da-21-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_21.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-22-downfiles"] = KedroOperator(
        task_id="teste-da-22-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_22.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-23-downfiles"] = KedroOperator(
        task_id="teste-da-23-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_23.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-24-downfiles"] = KedroOperator(
        task_id="teste-da-24-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_24.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-25-downfiles"] = KedroOperator(
        task_id="teste-da-25-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_25.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-26-downfiles"] = KedroOperator(
        task_id="teste-da-26-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_26.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-27-downfiles"] = KedroOperator(
        task_id="teste-da-27-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_27.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-28-downfiles"] = KedroOperator(
        task_id="teste-da-28-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_28.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-29-downfiles"] = KedroOperator(
        task_id="teste-da-29-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_29.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-3-downfiles"] = KedroOperator(
        task_id="teste-da-3-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_3.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-30-downfiles"] = KedroOperator(
        task_id="teste-da-30-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_30.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-31-downfiles"] = KedroOperator(
        task_id="teste-da-31-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_31.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-32-downfiles"] = KedroOperator(
        task_id="teste-da-32-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_32.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-33-downfiles"] = KedroOperator(
        task_id="teste-da-33-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_33.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-34-downfiles"] = KedroOperator(
        task_id="teste-da-34-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_34.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-35-downfiles"] = KedroOperator(
        task_id="teste-da-35-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_35.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-36-downfiles"] = KedroOperator(
        task_id="teste-da-36-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_36.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-37-downfiles"] = KedroOperator(
        task_id="teste-da-37-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_37.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-38-downfiles"] = KedroOperator(
        task_id="teste-da-38-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_38.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-39-downfiles"] = KedroOperator(
        task_id="teste-da-39-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_39.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-4-downfiles"] = KedroOperator(
        task_id="teste-da-4-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_4.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-40-downfiles"] = KedroOperator(
        task_id="teste-da-40-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_40.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-41-downfiles"] = KedroOperator(
        task_id="teste-da-41-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_41.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-42-downfiles"] = KedroOperator(
        task_id="teste-da-42-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_42.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-43-downfiles"] = KedroOperator(
        task_id="teste-da-43-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_43.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-44-downfiles"] = KedroOperator(
        task_id="teste-da-44-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_44.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-45-downfiles"] = KedroOperator(
        task_id="teste-da-45-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_45.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-46-downfiles"] = KedroOperator(
        task_id="teste-da-46-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_46.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-47-downfiles"] = KedroOperator(
        task_id="teste-da-47-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_47.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-48-downfiles"] = KedroOperator(
        task_id="teste-da-48-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_48.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-49-downfiles"] = KedroOperator(
        task_id="teste-da-49-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_49.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-5-downfiles"] = KedroOperator(
        task_id="teste-da-5-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_5.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-6-downfiles"] = KedroOperator(
        task_id="teste-da-6-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_6.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-7-downfiles"] = KedroOperator(
        task_id="teste-da-7-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_7.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-8-downfiles"] = KedroOperator(
        task_id="teste-da-8-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_8.downfiles",
        project_path=project_path,
        env=env,
    )

    tasks["teste-da-9-downfiles"] = KedroOperator(
        task_id="teste-da-9-downfiles",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_da_9.downfiles",
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

    tasks["teste-dm-10-preprocessdata"] = KedroOperator(
        task_id="teste-dm-10-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_10.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-11-preprocessdata"] = KedroOperator(
        task_id="teste-dm-11-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_11.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-12-preprocessdata"] = KedroOperator(
        task_id="teste-dm-12-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_12.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-13-preprocessdata"] = KedroOperator(
        task_id="teste-dm-13-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_13.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-14-preprocessdata"] = KedroOperator(
        task_id="teste-dm-14-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_14.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-15-preprocessdata"] = KedroOperator(
        task_id="teste-dm-15-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_15.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-16-preprocessdata"] = KedroOperator(
        task_id="teste-dm-16-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_16.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-17-preprocessdata"] = KedroOperator(
        task_id="teste-dm-17-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_17.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-18-preprocessdata"] = KedroOperator(
        task_id="teste-dm-18-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_18.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-19-preprocessdata"] = KedroOperator(
        task_id="teste-dm-19-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_19.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-2-preprocessdata"] = KedroOperator(
        task_id="teste-dm-2-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_2.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-20-preprocessdata"] = KedroOperator(
        task_id="teste-dm-20-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_20.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-21-preprocessdata"] = KedroOperator(
        task_id="teste-dm-21-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_21.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-22-preprocessdata"] = KedroOperator(
        task_id="teste-dm-22-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_22.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-23-preprocessdata"] = KedroOperator(
        task_id="teste-dm-23-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_23.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-24-preprocessdata"] = KedroOperator(
        task_id="teste-dm-24-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_24.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-25-preprocessdata"] = KedroOperator(
        task_id="teste-dm-25-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_25.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-26-preprocessdata"] = KedroOperator(
        task_id="teste-dm-26-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_26.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-27-preprocessdata"] = KedroOperator(
        task_id="teste-dm-27-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_27.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-28-preprocessdata"] = KedroOperator(
        task_id="teste-dm-28-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_28.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-29-preprocessdata"] = KedroOperator(
        task_id="teste-dm-29-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_29.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-3-preprocessdata"] = KedroOperator(
        task_id="teste-dm-3-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_3.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-30-preprocessdata"] = KedroOperator(
        task_id="teste-dm-30-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_30.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-31-preprocessdata"] = KedroOperator(
        task_id="teste-dm-31-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_31.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-32-preprocessdata"] = KedroOperator(
        task_id="teste-dm-32-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_32.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-33-preprocessdata"] = KedroOperator(
        task_id="teste-dm-33-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_33.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-34-preprocessdata"] = KedroOperator(
        task_id="teste-dm-34-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_34.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-35-preprocessdata"] = KedroOperator(
        task_id="teste-dm-35-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_35.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-36-preprocessdata"] = KedroOperator(
        task_id="teste-dm-36-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_36.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-37-preprocessdata"] = KedroOperator(
        task_id="teste-dm-37-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_37.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-38-preprocessdata"] = KedroOperator(
        task_id="teste-dm-38-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_38.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-39-preprocessdata"] = KedroOperator(
        task_id="teste-dm-39-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_39.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-4-preprocessdata"] = KedroOperator(
        task_id="teste-dm-4-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_4.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-40-preprocessdata"] = KedroOperator(
        task_id="teste-dm-40-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_40.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-41-preprocessdata"] = KedroOperator(
        task_id="teste-dm-41-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_41.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-42-preprocessdata"] = KedroOperator(
        task_id="teste-dm-42-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_42.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-43-preprocessdata"] = KedroOperator(
        task_id="teste-dm-43-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_43.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-44-preprocessdata"] = KedroOperator(
        task_id="teste-dm-44-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_44.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-45-preprocessdata"] = KedroOperator(
        task_id="teste-dm-45-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_45.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-46-preprocessdata"] = KedroOperator(
        task_id="teste-dm-46-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_46.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-47-preprocessdata"] = KedroOperator(
        task_id="teste-dm-47-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_47.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-48-preprocessdata"] = KedroOperator(
        task_id="teste-dm-48-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_48.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-49-preprocessdata"] = KedroOperator(
        task_id="teste-dm-49-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_49.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-5-preprocessdata"] = KedroOperator(
        task_id="teste-dm-5-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_5.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-6-preprocessdata"] = KedroOperator(
        task_id="teste-dm-6-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_6.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-7-preprocessdata"] = KedroOperator(
        task_id="teste-dm-7-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_7.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-8-preprocessdata"] = KedroOperator(
        task_id="teste-dm-8-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_8.preprocessdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-9-preprocessdata"] = KedroOperator(
        task_id="teste-dm-9-preprocessdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_9.preprocessdata",
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

    tasks["teste-dm-10-clean-energy"] = KedroOperator(
        task_id="teste-dm-10-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_10.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-11-clean-energy"] = KedroOperator(
        task_id="teste-dm-11-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_11.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-12-clean-energy"] = KedroOperator(
        task_id="teste-dm-12-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_12.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-13-clean-energy"] = KedroOperator(
        task_id="teste-dm-13-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_13.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-14-clean-energy"] = KedroOperator(
        task_id="teste-dm-14-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_14.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-15-clean-energy"] = KedroOperator(
        task_id="teste-dm-15-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_15.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-16-clean-energy"] = KedroOperator(
        task_id="teste-dm-16-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_16.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-17-clean-energy"] = KedroOperator(
        task_id="teste-dm-17-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_17.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-18-clean-energy"] = KedroOperator(
        task_id="teste-dm-18-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_18.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-19-clean-energy"] = KedroOperator(
        task_id="teste-dm-19-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_19.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-2-clean-energy"] = KedroOperator(
        task_id="teste-dm-2-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_2.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-20-clean-energy"] = KedroOperator(
        task_id="teste-dm-20-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_20.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-21-clean-energy"] = KedroOperator(
        task_id="teste-dm-21-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_21.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-22-clean-energy"] = KedroOperator(
        task_id="teste-dm-22-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_22.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-23-clean-energy"] = KedroOperator(
        task_id="teste-dm-23-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_23.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-24-clean-energy"] = KedroOperator(
        task_id="teste-dm-24-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_24.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-25-clean-energy"] = KedroOperator(
        task_id="teste-dm-25-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_25.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-26-clean-energy"] = KedroOperator(
        task_id="teste-dm-26-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_26.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-27-clean-energy"] = KedroOperator(
        task_id="teste-dm-27-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_27.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-28-clean-energy"] = KedroOperator(
        task_id="teste-dm-28-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_28.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-29-clean-energy"] = KedroOperator(
        task_id="teste-dm-29-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_29.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-3-clean-energy"] = KedroOperator(
        task_id="teste-dm-3-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_3.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-30-clean-energy"] = KedroOperator(
        task_id="teste-dm-30-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_30.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-31-clean-energy"] = KedroOperator(
        task_id="teste-dm-31-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_31.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-32-clean-energy"] = KedroOperator(
        task_id="teste-dm-32-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_32.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-33-clean-energy"] = KedroOperator(
        task_id="teste-dm-33-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_33.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-34-clean-energy"] = KedroOperator(
        task_id="teste-dm-34-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_34.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-35-clean-energy"] = KedroOperator(
        task_id="teste-dm-35-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_35.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-36-clean-energy"] = KedroOperator(
        task_id="teste-dm-36-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_36.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-37-clean-energy"] = KedroOperator(
        task_id="teste-dm-37-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_37.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-38-clean-energy"] = KedroOperator(
        task_id="teste-dm-38-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_38.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-39-clean-energy"] = KedroOperator(
        task_id="teste-dm-39-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_39.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-4-clean-energy"] = KedroOperator(
        task_id="teste-dm-4-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_4.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-40-clean-energy"] = KedroOperator(
        task_id="teste-dm-40-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_40.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-41-clean-energy"] = KedroOperator(
        task_id="teste-dm-41-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_41.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-42-clean-energy"] = KedroOperator(
        task_id="teste-dm-42-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_42.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-43-clean-energy"] = KedroOperator(
        task_id="teste-dm-43-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_43.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-44-clean-energy"] = KedroOperator(
        task_id="teste-dm-44-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_44.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-45-clean-energy"] = KedroOperator(
        task_id="teste-dm-45-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_45.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-46-clean-energy"] = KedroOperator(
        task_id="teste-dm-46-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_46.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-47-clean-energy"] = KedroOperator(
        task_id="teste-dm-47-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_47.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-48-clean-energy"] = KedroOperator(
        task_id="teste-dm-48-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_48.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-49-clean-energy"] = KedroOperator(
        task_id="teste-dm-49-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_49.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-5-clean-energy"] = KedroOperator(
        task_id="teste-dm-5-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_5.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-6-clean-energy"] = KedroOperator(
        task_id="teste-dm-6-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_6.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-7-clean-energy"] = KedroOperator(
        task_id="teste-dm-7-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_7.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-8-clean-energy"] = KedroOperator(
        task_id="teste-dm-8-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_8.clean_energy",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-9-clean-energy"] = KedroOperator(
        task_id="teste-dm-9-clean-energy",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_9.clean_energy",
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

    tasks["teste-dm-10-removeless24"] = KedroOperator(
        task_id="teste-dm-10-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_10.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-11-removeless24"] = KedroOperator(
        task_id="teste-dm-11-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_11.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-12-removeless24"] = KedroOperator(
        task_id="teste-dm-12-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_12.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-13-removeless24"] = KedroOperator(
        task_id="teste-dm-13-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_13.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-14-removeless24"] = KedroOperator(
        task_id="teste-dm-14-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_14.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-15-removeless24"] = KedroOperator(
        task_id="teste-dm-15-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_15.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-16-removeless24"] = KedroOperator(
        task_id="teste-dm-16-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_16.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-17-removeless24"] = KedroOperator(
        task_id="teste-dm-17-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_17.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-18-removeless24"] = KedroOperator(
        task_id="teste-dm-18-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_18.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-19-removeless24"] = KedroOperator(
        task_id="teste-dm-19-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_19.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-2-removeless24"] = KedroOperator(
        task_id="teste-dm-2-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_2.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-20-removeless24"] = KedroOperator(
        task_id="teste-dm-20-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_20.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-21-removeless24"] = KedroOperator(
        task_id="teste-dm-21-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_21.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-22-removeless24"] = KedroOperator(
        task_id="teste-dm-22-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_22.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-23-removeless24"] = KedroOperator(
        task_id="teste-dm-23-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_23.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-24-removeless24"] = KedroOperator(
        task_id="teste-dm-24-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_24.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-25-removeless24"] = KedroOperator(
        task_id="teste-dm-25-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_25.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-26-removeless24"] = KedroOperator(
        task_id="teste-dm-26-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_26.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-27-removeless24"] = KedroOperator(
        task_id="teste-dm-27-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_27.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-28-removeless24"] = KedroOperator(
        task_id="teste-dm-28-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_28.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-29-removeless24"] = KedroOperator(
        task_id="teste-dm-29-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_29.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-3-removeless24"] = KedroOperator(
        task_id="teste-dm-3-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_3.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-30-removeless24"] = KedroOperator(
        task_id="teste-dm-30-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_30.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-31-removeless24"] = KedroOperator(
        task_id="teste-dm-31-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_31.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-32-removeless24"] = KedroOperator(
        task_id="teste-dm-32-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_32.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-33-removeless24"] = KedroOperator(
        task_id="teste-dm-33-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_33.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-34-removeless24"] = KedroOperator(
        task_id="teste-dm-34-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_34.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-35-removeless24"] = KedroOperator(
        task_id="teste-dm-35-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_35.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-36-removeless24"] = KedroOperator(
        task_id="teste-dm-36-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_36.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-37-removeless24"] = KedroOperator(
        task_id="teste-dm-37-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_37.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-38-removeless24"] = KedroOperator(
        task_id="teste-dm-38-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_38.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-39-removeless24"] = KedroOperator(
        task_id="teste-dm-39-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_39.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-4-removeless24"] = KedroOperator(
        task_id="teste-dm-4-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_4.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-40-removeless24"] = KedroOperator(
        task_id="teste-dm-40-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_40.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-41-removeless24"] = KedroOperator(
        task_id="teste-dm-41-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_41.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-42-removeless24"] = KedroOperator(
        task_id="teste-dm-42-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_42.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-43-removeless24"] = KedroOperator(
        task_id="teste-dm-43-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_43.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-44-removeless24"] = KedroOperator(
        task_id="teste-dm-44-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_44.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-45-removeless24"] = KedroOperator(
        task_id="teste-dm-45-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_45.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-46-removeless24"] = KedroOperator(
        task_id="teste-dm-46-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_46.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-47-removeless24"] = KedroOperator(
        task_id="teste-dm-47-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_47.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-48-removeless24"] = KedroOperator(
        task_id="teste-dm-48-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_48.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-49-removeless24"] = KedroOperator(
        task_id="teste-dm-49-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_49.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-5-removeless24"] = KedroOperator(
        task_id="teste-dm-5-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_5.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-6-removeless24"] = KedroOperator(
        task_id="teste-dm-6-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_6.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-7-removeless24"] = KedroOperator(
        task_id="teste-dm-7-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_7.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-8-removeless24"] = KedroOperator(
        task_id="teste-dm-8-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_8.removeless24",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-9-removeless24"] = KedroOperator(
        task_id="teste-dm-9-removeless24",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_9.removeless24",
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

    tasks["teste-dm-10-addfeatures"] = KedroOperator(
        task_id="teste-dm-10-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_10.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-11-addfeatures"] = KedroOperator(
        task_id="teste-dm-11-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_11.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-12-addfeatures"] = KedroOperator(
        task_id="teste-dm-12-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_12.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-13-addfeatures"] = KedroOperator(
        task_id="teste-dm-13-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_13.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-14-addfeatures"] = KedroOperator(
        task_id="teste-dm-14-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_14.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-15-addfeatures"] = KedroOperator(
        task_id="teste-dm-15-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_15.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-16-addfeatures"] = KedroOperator(
        task_id="teste-dm-16-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_16.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-17-addfeatures"] = KedroOperator(
        task_id="teste-dm-17-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_17.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-18-addfeatures"] = KedroOperator(
        task_id="teste-dm-18-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_18.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-19-addfeatures"] = KedroOperator(
        task_id="teste-dm-19-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_19.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-2-addfeatures"] = KedroOperator(
        task_id="teste-dm-2-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_2.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-20-addfeatures"] = KedroOperator(
        task_id="teste-dm-20-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_20.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-21-addfeatures"] = KedroOperator(
        task_id="teste-dm-21-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_21.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-22-addfeatures"] = KedroOperator(
        task_id="teste-dm-22-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_22.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-23-addfeatures"] = KedroOperator(
        task_id="teste-dm-23-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_23.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-24-addfeatures"] = KedroOperator(
        task_id="teste-dm-24-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_24.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-25-addfeatures"] = KedroOperator(
        task_id="teste-dm-25-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_25.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-26-addfeatures"] = KedroOperator(
        task_id="teste-dm-26-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_26.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-27-addfeatures"] = KedroOperator(
        task_id="teste-dm-27-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_27.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-28-addfeatures"] = KedroOperator(
        task_id="teste-dm-28-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_28.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-29-addfeatures"] = KedroOperator(
        task_id="teste-dm-29-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_29.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-3-addfeatures"] = KedroOperator(
        task_id="teste-dm-3-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_3.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-30-addfeatures"] = KedroOperator(
        task_id="teste-dm-30-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_30.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-31-addfeatures"] = KedroOperator(
        task_id="teste-dm-31-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_31.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-32-addfeatures"] = KedroOperator(
        task_id="teste-dm-32-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_32.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-33-addfeatures"] = KedroOperator(
        task_id="teste-dm-33-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_33.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-34-addfeatures"] = KedroOperator(
        task_id="teste-dm-34-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_34.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-35-addfeatures"] = KedroOperator(
        task_id="teste-dm-35-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_35.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-36-addfeatures"] = KedroOperator(
        task_id="teste-dm-36-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_36.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-37-addfeatures"] = KedroOperator(
        task_id="teste-dm-37-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_37.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-38-addfeatures"] = KedroOperator(
        task_id="teste-dm-38-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_38.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-39-addfeatures"] = KedroOperator(
        task_id="teste-dm-39-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_39.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-4-addfeatures"] = KedroOperator(
        task_id="teste-dm-4-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_4.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-40-addfeatures"] = KedroOperator(
        task_id="teste-dm-40-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_40.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-41-addfeatures"] = KedroOperator(
        task_id="teste-dm-41-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_41.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-42-addfeatures"] = KedroOperator(
        task_id="teste-dm-42-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_42.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-43-addfeatures"] = KedroOperator(
        task_id="teste-dm-43-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_43.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-44-addfeatures"] = KedroOperator(
        task_id="teste-dm-44-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_44.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-45-addfeatures"] = KedroOperator(
        task_id="teste-dm-45-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_45.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-46-addfeatures"] = KedroOperator(
        task_id="teste-dm-46-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_46.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-47-addfeatures"] = KedroOperator(
        task_id="teste-dm-47-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_47.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-48-addfeatures"] = KedroOperator(
        task_id="teste-dm-48-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_48.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-49-addfeatures"] = KedroOperator(
        task_id="teste-dm-49-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_49.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-5-addfeatures"] = KedroOperator(
        task_id="teste-dm-5-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_5.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-6-addfeatures"] = KedroOperator(
        task_id="teste-dm-6-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_6.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-7-addfeatures"] = KedroOperator(
        task_id="teste-dm-7-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_7.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-8-addfeatures"] = KedroOperator(
        task_id="teste-dm-8-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_8.addfeatures",
        project_path=project_path,
        env=env,
    )

    tasks["teste-dm-9-addfeatures"] = KedroOperator(
        task_id="teste-dm-9-addfeatures",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_dm_9.addfeatures",
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

    tasks["teste-ml-10-splitdata"] = KedroOperator(
        task_id="teste-ml-10-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_10.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-11-splitdata"] = KedroOperator(
        task_id="teste-ml-11-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_11.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-12-splitdata"] = KedroOperator(
        task_id="teste-ml-12-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_12.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-13-splitdata"] = KedroOperator(
        task_id="teste-ml-13-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_13.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-14-splitdata"] = KedroOperator(
        task_id="teste-ml-14-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_14.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-15-splitdata"] = KedroOperator(
        task_id="teste-ml-15-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_15.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-16-splitdata"] = KedroOperator(
        task_id="teste-ml-16-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_16.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-17-splitdata"] = KedroOperator(
        task_id="teste-ml-17-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_17.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-18-splitdata"] = KedroOperator(
        task_id="teste-ml-18-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_18.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-19-splitdata"] = KedroOperator(
        task_id="teste-ml-19-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_19.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-2-splitdata"] = KedroOperator(
        task_id="teste-ml-2-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_2.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-20-splitdata"] = KedroOperator(
        task_id="teste-ml-20-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_20.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-21-splitdata"] = KedroOperator(
        task_id="teste-ml-21-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_21.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-22-splitdata"] = KedroOperator(
        task_id="teste-ml-22-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_22.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-23-splitdata"] = KedroOperator(
        task_id="teste-ml-23-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_23.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-24-splitdata"] = KedroOperator(
        task_id="teste-ml-24-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_24.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-25-splitdata"] = KedroOperator(
        task_id="teste-ml-25-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_25.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-26-splitdata"] = KedroOperator(
        task_id="teste-ml-26-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_26.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-27-splitdata"] = KedroOperator(
        task_id="teste-ml-27-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_27.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-28-splitdata"] = KedroOperator(
        task_id="teste-ml-28-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_28.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-29-splitdata"] = KedroOperator(
        task_id="teste-ml-29-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_29.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-3-splitdata"] = KedroOperator(
        task_id="teste-ml-3-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_3.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-30-splitdata"] = KedroOperator(
        task_id="teste-ml-30-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_30.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-31-splitdata"] = KedroOperator(
        task_id="teste-ml-31-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_31.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-32-splitdata"] = KedroOperator(
        task_id="teste-ml-32-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_32.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-33-splitdata"] = KedroOperator(
        task_id="teste-ml-33-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_33.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-34-splitdata"] = KedroOperator(
        task_id="teste-ml-34-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_34.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-35-splitdata"] = KedroOperator(
        task_id="teste-ml-35-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_35.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-36-splitdata"] = KedroOperator(
        task_id="teste-ml-36-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_36.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-37-splitdata"] = KedroOperator(
        task_id="teste-ml-37-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_37.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-38-splitdata"] = KedroOperator(
        task_id="teste-ml-38-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_38.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-39-splitdata"] = KedroOperator(
        task_id="teste-ml-39-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_39.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-4-splitdata"] = KedroOperator(
        task_id="teste-ml-4-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_4.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-40-splitdata"] = KedroOperator(
        task_id="teste-ml-40-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_40.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-41-splitdata"] = KedroOperator(
        task_id="teste-ml-41-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_41.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-42-splitdata"] = KedroOperator(
        task_id="teste-ml-42-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_42.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-43-splitdata"] = KedroOperator(
        task_id="teste-ml-43-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_43.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-44-splitdata"] = KedroOperator(
        task_id="teste-ml-44-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_44.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-45-splitdata"] = KedroOperator(
        task_id="teste-ml-45-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_45.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-46-splitdata"] = KedroOperator(
        task_id="teste-ml-46-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_46.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-47-splitdata"] = KedroOperator(
        task_id="teste-ml-47-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_47.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-48-splitdata"] = KedroOperator(
        task_id="teste-ml-48-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_48.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-49-splitdata"] = KedroOperator(
        task_id="teste-ml-49-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_49.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-5-splitdata"] = KedroOperator(
        task_id="teste-ml-5-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_5.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-6-splitdata"] = KedroOperator(
        task_id="teste-ml-6-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_6.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-7-splitdata"] = KedroOperator(
        task_id="teste-ml-7-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_7.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-8-splitdata"] = KedroOperator(
        task_id="teste-ml-8-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_8.splitdata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-9-splitdata"] = KedroOperator(
        task_id="teste-ml-9-splitdata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_9.splitdata",
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

    tasks["teste-ml-10-trainforecasting"] = KedroOperator(
        task_id="teste-ml-10-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_10.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-11-trainforecasting"] = KedroOperator(
        task_id="teste-ml-11-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_11.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-12-trainforecasting"] = KedroOperator(
        task_id="teste-ml-12-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_12.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-13-trainforecasting"] = KedroOperator(
        task_id="teste-ml-13-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_13.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-14-trainforecasting"] = KedroOperator(
        task_id="teste-ml-14-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_14.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-15-trainforecasting"] = KedroOperator(
        task_id="teste-ml-15-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_15.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-16-trainforecasting"] = KedroOperator(
        task_id="teste-ml-16-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_16.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-17-trainforecasting"] = KedroOperator(
        task_id="teste-ml-17-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_17.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-18-trainforecasting"] = KedroOperator(
        task_id="teste-ml-18-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_18.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-19-trainforecasting"] = KedroOperator(
        task_id="teste-ml-19-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_19.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-2-trainforecasting"] = KedroOperator(
        task_id="teste-ml-2-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_2.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-20-trainforecasting"] = KedroOperator(
        task_id="teste-ml-20-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_20.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-21-trainforecasting"] = KedroOperator(
        task_id="teste-ml-21-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_21.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-22-trainforecasting"] = KedroOperator(
        task_id="teste-ml-22-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_22.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-23-trainforecasting"] = KedroOperator(
        task_id="teste-ml-23-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_23.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-24-trainforecasting"] = KedroOperator(
        task_id="teste-ml-24-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_24.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-25-trainforecasting"] = KedroOperator(
        task_id="teste-ml-25-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_25.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-26-trainforecasting"] = KedroOperator(
        task_id="teste-ml-26-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_26.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-27-trainforecasting"] = KedroOperator(
        task_id="teste-ml-27-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_27.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-28-trainforecasting"] = KedroOperator(
        task_id="teste-ml-28-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_28.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-29-trainforecasting"] = KedroOperator(
        task_id="teste-ml-29-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_29.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-3-trainforecasting"] = KedroOperator(
        task_id="teste-ml-3-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_3.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-30-trainforecasting"] = KedroOperator(
        task_id="teste-ml-30-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_30.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-31-trainforecasting"] = KedroOperator(
        task_id="teste-ml-31-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_31.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-32-trainforecasting"] = KedroOperator(
        task_id="teste-ml-32-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_32.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-33-trainforecasting"] = KedroOperator(
        task_id="teste-ml-33-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_33.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-34-trainforecasting"] = KedroOperator(
        task_id="teste-ml-34-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_34.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-35-trainforecasting"] = KedroOperator(
        task_id="teste-ml-35-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_35.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-36-trainforecasting"] = KedroOperator(
        task_id="teste-ml-36-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_36.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-37-trainforecasting"] = KedroOperator(
        task_id="teste-ml-37-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_37.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-38-trainforecasting"] = KedroOperator(
        task_id="teste-ml-38-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_38.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-39-trainforecasting"] = KedroOperator(
        task_id="teste-ml-39-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_39.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-4-trainforecasting"] = KedroOperator(
        task_id="teste-ml-4-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_4.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-40-trainforecasting"] = KedroOperator(
        task_id="teste-ml-40-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_40.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-41-trainforecasting"] = KedroOperator(
        task_id="teste-ml-41-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_41.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-42-trainforecasting"] = KedroOperator(
        task_id="teste-ml-42-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_42.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-43-trainforecasting"] = KedroOperator(
        task_id="teste-ml-43-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_43.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-44-trainforecasting"] = KedroOperator(
        task_id="teste-ml-44-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_44.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-45-trainforecasting"] = KedroOperator(
        task_id="teste-ml-45-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_45.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-46-trainforecasting"] = KedroOperator(
        task_id="teste-ml-46-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_46.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-47-trainforecasting"] = KedroOperator(
        task_id="teste-ml-47-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_47.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-48-trainforecasting"] = KedroOperator(
        task_id="teste-ml-48-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_48.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-49-trainforecasting"] = KedroOperator(
        task_id="teste-ml-49-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_49.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-5-trainforecasting"] = KedroOperator(
        task_id="teste-ml-5-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_5.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-6-trainforecasting"] = KedroOperator(
        task_id="teste-ml-6-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_6.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-7-trainforecasting"] = KedroOperator(
        task_id="teste-ml-7-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_7.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-8-trainforecasting"] = KedroOperator(
        task_id="teste-ml-8-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_8.trainforecasting",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-9-trainforecasting"] = KedroOperator(
        task_id="teste-ml-9-trainforecasting",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_9.trainforecasting",
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

    tasks["teste-ml-10-optimize"] = KedroOperator(
        task_id="teste-ml-10-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_10.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-11-optimize"] = KedroOperator(
        task_id="teste-ml-11-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_11.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-12-optimize"] = KedroOperator(
        task_id="teste-ml-12-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_12.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-13-optimize"] = KedroOperator(
        task_id="teste-ml-13-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_13.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-14-optimize"] = KedroOperator(
        task_id="teste-ml-14-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_14.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-15-optimize"] = KedroOperator(
        task_id="teste-ml-15-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_15.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-16-optimize"] = KedroOperator(
        task_id="teste-ml-16-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_16.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-17-optimize"] = KedroOperator(
        task_id="teste-ml-17-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_17.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-18-optimize"] = KedroOperator(
        task_id="teste-ml-18-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_18.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-19-optimize"] = KedroOperator(
        task_id="teste-ml-19-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_19.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-2-optimize"] = KedroOperator(
        task_id="teste-ml-2-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_2.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-20-optimize"] = KedroOperator(
        task_id="teste-ml-20-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_20.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-21-optimize"] = KedroOperator(
        task_id="teste-ml-21-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_21.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-22-optimize"] = KedroOperator(
        task_id="teste-ml-22-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_22.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-23-optimize"] = KedroOperator(
        task_id="teste-ml-23-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_23.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-24-optimize"] = KedroOperator(
        task_id="teste-ml-24-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_24.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-25-optimize"] = KedroOperator(
        task_id="teste-ml-25-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_25.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-26-optimize"] = KedroOperator(
        task_id="teste-ml-26-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_26.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-27-optimize"] = KedroOperator(
        task_id="teste-ml-27-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_27.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-28-optimize"] = KedroOperator(
        task_id="teste-ml-28-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_28.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-29-optimize"] = KedroOperator(
        task_id="teste-ml-29-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_29.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-3-optimize"] = KedroOperator(
        task_id="teste-ml-3-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_3.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-30-optimize"] = KedroOperator(
        task_id="teste-ml-30-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_30.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-31-optimize"] = KedroOperator(
        task_id="teste-ml-31-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_31.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-32-optimize"] = KedroOperator(
        task_id="teste-ml-32-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_32.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-33-optimize"] = KedroOperator(
        task_id="teste-ml-33-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_33.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-34-optimize"] = KedroOperator(
        task_id="teste-ml-34-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_34.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-35-optimize"] = KedroOperator(
        task_id="teste-ml-35-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_35.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-36-optimize"] = KedroOperator(
        task_id="teste-ml-36-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_36.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-37-optimize"] = KedroOperator(
        task_id="teste-ml-37-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_37.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-38-optimize"] = KedroOperator(
        task_id="teste-ml-38-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_38.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-39-optimize"] = KedroOperator(
        task_id="teste-ml-39-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_39.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-4-optimize"] = KedroOperator(
        task_id="teste-ml-4-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_4.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-40-optimize"] = KedroOperator(
        task_id="teste-ml-40-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_40.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-41-optimize"] = KedroOperator(
        task_id="teste-ml-41-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_41.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-42-optimize"] = KedroOperator(
        task_id="teste-ml-42-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_42.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-43-optimize"] = KedroOperator(
        task_id="teste-ml-43-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_43.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-44-optimize"] = KedroOperator(
        task_id="teste-ml-44-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_44.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-45-optimize"] = KedroOperator(
        task_id="teste-ml-45-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_45.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-46-optimize"] = KedroOperator(
        task_id="teste-ml-46-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_46.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-47-optimize"] = KedroOperator(
        task_id="teste-ml-47-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_47.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-48-optimize"] = KedroOperator(
        task_id="teste-ml-48-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_48.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-49-optimize"] = KedroOperator(
        task_id="teste-ml-49-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_49.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-5-optimize"] = KedroOperator(
        task_id="teste-ml-5-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_5.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-6-optimize"] = KedroOperator(
        task_id="teste-ml-6-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_6.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-7-optimize"] = KedroOperator(
        task_id="teste-ml-7-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_7.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-8-optimize"] = KedroOperator(
        task_id="teste-ml-8-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_8.optimize",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-9-optimize"] = KedroOperator(
        task_id="teste-ml-9-optimize",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_9.optimize",
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

    tasks["teste-ml-10-fitmodel"] = KedroOperator(
        task_id="teste-ml-10-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_10.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-11-fitmodel"] = KedroOperator(
        task_id="teste-ml-11-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_11.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-12-fitmodel"] = KedroOperator(
        task_id="teste-ml-12-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_12.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-13-fitmodel"] = KedroOperator(
        task_id="teste-ml-13-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_13.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-14-fitmodel"] = KedroOperator(
        task_id="teste-ml-14-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_14.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-15-fitmodel"] = KedroOperator(
        task_id="teste-ml-15-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_15.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-16-fitmodel"] = KedroOperator(
        task_id="teste-ml-16-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_16.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-17-fitmodel"] = KedroOperator(
        task_id="teste-ml-17-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_17.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-18-fitmodel"] = KedroOperator(
        task_id="teste-ml-18-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_18.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-19-fitmodel"] = KedroOperator(
        task_id="teste-ml-19-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_19.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-2-fitmodel"] = KedroOperator(
        task_id="teste-ml-2-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_2.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-20-fitmodel"] = KedroOperator(
        task_id="teste-ml-20-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_20.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-21-fitmodel"] = KedroOperator(
        task_id="teste-ml-21-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_21.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-22-fitmodel"] = KedroOperator(
        task_id="teste-ml-22-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_22.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-23-fitmodel"] = KedroOperator(
        task_id="teste-ml-23-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_23.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-24-fitmodel"] = KedroOperator(
        task_id="teste-ml-24-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_24.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-25-fitmodel"] = KedroOperator(
        task_id="teste-ml-25-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_25.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-26-fitmodel"] = KedroOperator(
        task_id="teste-ml-26-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_26.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-27-fitmodel"] = KedroOperator(
        task_id="teste-ml-27-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_27.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-28-fitmodel"] = KedroOperator(
        task_id="teste-ml-28-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_28.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-29-fitmodel"] = KedroOperator(
        task_id="teste-ml-29-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_29.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-3-fitmodel"] = KedroOperator(
        task_id="teste-ml-3-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_3.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-30-fitmodel"] = KedroOperator(
        task_id="teste-ml-30-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_30.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-31-fitmodel"] = KedroOperator(
        task_id="teste-ml-31-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_31.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-32-fitmodel"] = KedroOperator(
        task_id="teste-ml-32-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_32.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-33-fitmodel"] = KedroOperator(
        task_id="teste-ml-33-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_33.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-34-fitmodel"] = KedroOperator(
        task_id="teste-ml-34-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_34.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-35-fitmodel"] = KedroOperator(
        task_id="teste-ml-35-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_35.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-36-fitmodel"] = KedroOperator(
        task_id="teste-ml-36-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_36.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-37-fitmodel"] = KedroOperator(
        task_id="teste-ml-37-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_37.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-38-fitmodel"] = KedroOperator(
        task_id="teste-ml-38-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_38.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-39-fitmodel"] = KedroOperator(
        task_id="teste-ml-39-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_39.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-4-fitmodel"] = KedroOperator(
        task_id="teste-ml-4-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_4.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-40-fitmodel"] = KedroOperator(
        task_id="teste-ml-40-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_40.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-41-fitmodel"] = KedroOperator(
        task_id="teste-ml-41-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_41.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-42-fitmodel"] = KedroOperator(
        task_id="teste-ml-42-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_42.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-43-fitmodel"] = KedroOperator(
        task_id="teste-ml-43-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_43.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-44-fitmodel"] = KedroOperator(
        task_id="teste-ml-44-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_44.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-45-fitmodel"] = KedroOperator(
        task_id="teste-ml-45-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_45.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-46-fitmodel"] = KedroOperator(
        task_id="teste-ml-46-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_46.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-47-fitmodel"] = KedroOperator(
        task_id="teste-ml-47-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_47.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-48-fitmodel"] = KedroOperator(
        task_id="teste-ml-48-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_48.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-49-fitmodel"] = KedroOperator(
        task_id="teste-ml-49-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_49.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-5-fitmodel"] = KedroOperator(
        task_id="teste-ml-5-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_5.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-6-fitmodel"] = KedroOperator(
        task_id="teste-ml-6-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_6.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-7-fitmodel"] = KedroOperator(
        task_id="teste-ml-7-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_7.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-8-fitmodel"] = KedroOperator(
        task_id="teste-ml-8-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_8.fitmodel",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-9-fitmodel"] = KedroOperator(
        task_id="teste-ml-9-fitmodel",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_9.fitmodel",
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

    tasks["teste-ml-10-predict"] = KedroOperator(
        task_id="teste-ml-10-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_10.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-11-predict"] = KedroOperator(
        task_id="teste-ml-11-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_11.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-12-predict"] = KedroOperator(
        task_id="teste-ml-12-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_12.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-13-predict"] = KedroOperator(
        task_id="teste-ml-13-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_13.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-14-predict"] = KedroOperator(
        task_id="teste-ml-14-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_14.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-15-predict"] = KedroOperator(
        task_id="teste-ml-15-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_15.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-16-predict"] = KedroOperator(
        task_id="teste-ml-16-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_16.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-17-predict"] = KedroOperator(
        task_id="teste-ml-17-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_17.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-18-predict"] = KedroOperator(
        task_id="teste-ml-18-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_18.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-19-predict"] = KedroOperator(
        task_id="teste-ml-19-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_19.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-2-predict"] = KedroOperator(
        task_id="teste-ml-2-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_2.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-20-predict"] = KedroOperator(
        task_id="teste-ml-20-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_20.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-21-predict"] = KedroOperator(
        task_id="teste-ml-21-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_21.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-22-predict"] = KedroOperator(
        task_id="teste-ml-22-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_22.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-23-predict"] = KedroOperator(
        task_id="teste-ml-23-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_23.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-24-predict"] = KedroOperator(
        task_id="teste-ml-24-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_24.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-25-predict"] = KedroOperator(
        task_id="teste-ml-25-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_25.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-26-predict"] = KedroOperator(
        task_id="teste-ml-26-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_26.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-27-predict"] = KedroOperator(
        task_id="teste-ml-27-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_27.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-28-predict"] = KedroOperator(
        task_id="teste-ml-28-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_28.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-29-predict"] = KedroOperator(
        task_id="teste-ml-29-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_29.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-3-predict"] = KedroOperator(
        task_id="teste-ml-3-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_3.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-30-predict"] = KedroOperator(
        task_id="teste-ml-30-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_30.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-31-predict"] = KedroOperator(
        task_id="teste-ml-31-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_31.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-32-predict"] = KedroOperator(
        task_id="teste-ml-32-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_32.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-33-predict"] = KedroOperator(
        task_id="teste-ml-33-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_33.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-34-predict"] = KedroOperator(
        task_id="teste-ml-34-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_34.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-35-predict"] = KedroOperator(
        task_id="teste-ml-35-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_35.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-36-predict"] = KedroOperator(
        task_id="teste-ml-36-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_36.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-37-predict"] = KedroOperator(
        task_id="teste-ml-37-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_37.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-38-predict"] = KedroOperator(
        task_id="teste-ml-38-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_38.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-39-predict"] = KedroOperator(
        task_id="teste-ml-39-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_39.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-4-predict"] = KedroOperator(
        task_id="teste-ml-4-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_4.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-40-predict"] = KedroOperator(
        task_id="teste-ml-40-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_40.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-41-predict"] = KedroOperator(
        task_id="teste-ml-41-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_41.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-42-predict"] = KedroOperator(
        task_id="teste-ml-42-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_42.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-43-predict"] = KedroOperator(
        task_id="teste-ml-43-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_43.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-44-predict"] = KedroOperator(
        task_id="teste-ml-44-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_44.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-45-predict"] = KedroOperator(
        task_id="teste-ml-45-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_45.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-46-predict"] = KedroOperator(
        task_id="teste-ml-46-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_46.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-47-predict"] = KedroOperator(
        task_id="teste-ml-47-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_47.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-48-predict"] = KedroOperator(
        task_id="teste-ml-48-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_48.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-49-predict"] = KedroOperator(
        task_id="teste-ml-49-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_49.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-5-predict"] = KedroOperator(
        task_id="teste-ml-5-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_5.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-6-predict"] = KedroOperator(
        task_id="teste-ml-6-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_6.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-7-predict"] = KedroOperator(
        task_id="teste-ml-7-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_7.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-8-predict"] = KedroOperator(
        task_id="teste-ml-8-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_8.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-9-predict"] = KedroOperator(
        task_id="teste-ml-9-predict",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_9.predict",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-0-writedata"] = KedroOperator(
        task_id="teste-ml-0-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_0.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-1-writedata"] = KedroOperator(
        task_id="teste-ml-1-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_1.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-10-writedata"] = KedroOperator(
        task_id="teste-ml-10-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_10.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-11-writedata"] = KedroOperator(
        task_id="teste-ml-11-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_11.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-12-writedata"] = KedroOperator(
        task_id="teste-ml-12-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_12.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-13-writedata"] = KedroOperator(
        task_id="teste-ml-13-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_13.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-14-writedata"] = KedroOperator(
        task_id="teste-ml-14-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_14.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-15-writedata"] = KedroOperator(
        task_id="teste-ml-15-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_15.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-16-writedata"] = KedroOperator(
        task_id="teste-ml-16-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_16.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-17-writedata"] = KedroOperator(
        task_id="teste-ml-17-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_17.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-18-writedata"] = KedroOperator(
        task_id="teste-ml-18-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_18.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-19-writedata"] = KedroOperator(
        task_id="teste-ml-19-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_19.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-2-writedata"] = KedroOperator(
        task_id="teste-ml-2-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_2.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-20-writedata"] = KedroOperator(
        task_id="teste-ml-20-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_20.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-21-writedata"] = KedroOperator(
        task_id="teste-ml-21-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_21.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-22-writedata"] = KedroOperator(
        task_id="teste-ml-22-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_22.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-23-writedata"] = KedroOperator(
        task_id="teste-ml-23-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_23.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-24-writedata"] = KedroOperator(
        task_id="teste-ml-24-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_24.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-25-writedata"] = KedroOperator(
        task_id="teste-ml-25-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_25.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-26-writedata"] = KedroOperator(
        task_id="teste-ml-26-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_26.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-27-writedata"] = KedroOperator(
        task_id="teste-ml-27-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_27.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-28-writedata"] = KedroOperator(
        task_id="teste-ml-28-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_28.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-29-writedata"] = KedroOperator(
        task_id="teste-ml-29-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_29.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-3-writedata"] = KedroOperator(
        task_id="teste-ml-3-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_3.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-30-writedata"] = KedroOperator(
        task_id="teste-ml-30-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_30.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-31-writedata"] = KedroOperator(
        task_id="teste-ml-31-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_31.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-32-writedata"] = KedroOperator(
        task_id="teste-ml-32-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_32.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-33-writedata"] = KedroOperator(
        task_id="teste-ml-33-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_33.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-34-writedata"] = KedroOperator(
        task_id="teste-ml-34-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_34.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-35-writedata"] = KedroOperator(
        task_id="teste-ml-35-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_35.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-36-writedata"] = KedroOperator(
        task_id="teste-ml-36-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_36.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-37-writedata"] = KedroOperator(
        task_id="teste-ml-37-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_37.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-38-writedata"] = KedroOperator(
        task_id="teste-ml-38-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_38.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-39-writedata"] = KedroOperator(
        task_id="teste-ml-39-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_39.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-4-writedata"] = KedroOperator(
        task_id="teste-ml-4-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_4.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-40-writedata"] = KedroOperator(
        task_id="teste-ml-40-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_40.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-41-writedata"] = KedroOperator(
        task_id="teste-ml-41-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_41.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-42-writedata"] = KedroOperator(
        task_id="teste-ml-42-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_42.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-43-writedata"] = KedroOperator(
        task_id="teste-ml-43-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_43.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-44-writedata"] = KedroOperator(
        task_id="teste-ml-44-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_44.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-45-writedata"] = KedroOperator(
        task_id="teste-ml-45-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_45.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-46-writedata"] = KedroOperator(
        task_id="teste-ml-46-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_46.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-47-writedata"] = KedroOperator(
        task_id="teste-ml-47-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_47.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-48-writedata"] = KedroOperator(
        task_id="teste-ml-48-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_48.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-49-writedata"] = KedroOperator(
        task_id="teste-ml-49-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_49.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-5-writedata"] = KedroOperator(
        task_id="teste-ml-5-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_5.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-6-writedata"] = KedroOperator(
        task_id="teste-ml-6-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_6.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-7-writedata"] = KedroOperator(
        task_id="teste-ml-7-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_7.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-8-writedata"] = KedroOperator(
        task_id="teste-ml-8-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_8.writedata",
        project_path=project_path,
        env=env,
    )

    tasks["teste-ml-9-writedata"] = KedroOperator(
        task_id="teste-ml-9-writedata",
        package_name=package_name,
        pipeline_name=pipeline_name,
        node_name="teste_ml_9.writedata",
        project_path=project_path,
        env=env,
    )



    tasks["teste-da-40-downfiles"] >> tasks["teste-dm-40-preprocessdata"]

    tasks["teste-da-40-downfiles"] >> tasks["teste-ml-40-writedata"]

    tasks["teste-ml-31-trainforecasting"] >> tasks["teste-ml-31-optimize"]

    tasks["teste-ml-31-trainforecasting"] >> tasks["teste-ml-31-fitmodel"]

    tasks["teste-ml-31-splitdata"] >> tasks["teste-ml-31-optimize"]

    tasks["teste-ml-31-splitdata"] >> tasks["teste-ml-31-trainforecasting"]

    tasks["teste-ml-31-splitdata"] >> tasks["teste-ml-31-predict"]

    tasks["teste-ml-43-splitdata"] >> tasks["teste-ml-43-optimize"]

    tasks["teste-ml-43-splitdata"] >> tasks["teste-ml-43-predict"]

    tasks["teste-ml-43-splitdata"] >> tasks["teste-ml-43-trainforecasting"]

    tasks["teste-ml-43-trainforecasting"] >> tasks["teste-ml-43-optimize"]

    tasks["teste-ml-43-trainforecasting"] >> tasks["teste-ml-43-fitmodel"]

    tasks["teste-dm-36-preprocessdata"] >> tasks["teste-dm-36-clean-energy"]

    tasks["teste-dm-37-clean-energy"] >> tasks["teste-dm-37-removeless24"]

    tasks["teste-ml-19-trainforecasting"] >> tasks["teste-ml-19-fitmodel"]

    tasks["teste-ml-19-trainforecasting"] >> tasks["teste-ml-19-optimize"]

    tasks["teste-ml-19-optimize"] >> tasks["teste-ml-19-fitmodel"]

    tasks["teste-da-28-downfiles"] >> tasks["teste-dm-28-preprocessdata"]

    tasks["teste-da-28-downfiles"] >> tasks["teste-ml-28-writedata"]

    tasks["teste-ml-20-splitdata"] >> tasks["teste-ml-20-optimize"]

    tasks["teste-ml-20-splitdata"] >> tasks["teste-ml-20-trainforecasting"]

    tasks["teste-ml-20-splitdata"] >> tasks["teste-ml-20-predict"]

    tasks["teste-ml-20-trainforecasting"] >> tasks["teste-ml-20-optimize"]

    tasks["teste-ml-20-trainforecasting"] >> tasks["teste-ml-20-fitmodel"]

    tasks["teste-dm-47-removeless24"] >> tasks["teste-dm-47-addfeatures"]

    tasks["teste-dm-3-preprocessdata"] >> tasks["teste-dm-3-clean-energy"]

    tasks["teste-da-16-downfiles"] >> tasks["teste-ml-16-writedata"]

    tasks["teste-da-16-downfiles"] >> tasks["teste-dm-16-preprocessdata"]

    tasks["teste-ml-16-predict"] >> tasks["teste-ml-16-writedata"]

    tasks["teste-dm-49-addfeatures"] >> tasks["teste-ml-49-splitdata"]

    tasks["teste-ml-32-splitdata"] >> tasks["teste-ml-32-trainforecasting"]

    tasks["teste-ml-32-splitdata"] >> tasks["teste-ml-32-predict"]

    tasks["teste-ml-32-splitdata"] >> tasks["teste-ml-32-optimize"]

    tasks["teste-dm-10-addfeatures"] >> tasks["teste-ml-10-splitdata"]

    tasks["teste-ml-5-optimize"] >> tasks["teste-ml-5-fitmodel"]

    tasks["teste-ml-5-trainforecasting"] >> tasks["teste-ml-5-fitmodel"]

    tasks["teste-ml-5-trainforecasting"] >> tasks["teste-ml-5-optimize"]

    tasks["teste-ml-32-predict"] >> tasks["teste-ml-32-writedata"]

    tasks["teste-da-32-downfiles"] >> tasks["teste-ml-32-writedata"]

    tasks["teste-da-32-downfiles"] >> tasks["teste-dm-32-preprocessdata"]

    tasks["teste-dm-15-preprocessdata"] >> tasks["teste-dm-15-clean-energy"]

    tasks["teste-dm-13-addfeatures"] >> tasks["teste-ml-13-splitdata"]

    tasks["teste-ml-41-splitdata"] >> tasks["teste-ml-41-trainforecasting"]

    tasks["teste-ml-41-splitdata"] >> tasks["teste-ml-41-predict"]

    tasks["teste-ml-41-splitdata"] >> tasks["teste-ml-41-optimize"]

    tasks["teste-dm-4-preprocessdata"] >> tasks["teste-dm-4-clean-energy"]

    tasks["teste-ml-22-optimize"] >> tasks["teste-ml-22-fitmodel"]

    tasks["teste-ml-22-trainforecasting"] >> tasks["teste-ml-22-fitmodel"]

    tasks["teste-ml-22-trainforecasting"] >> tasks["teste-ml-22-optimize"]

    tasks["teste-dm-42-preprocessdata"] >> tasks["teste-dm-42-clean-energy"]

    tasks["teste-dm-33-preprocessdata"] >> tasks["teste-dm-33-clean-energy"]

    tasks["teste-dm-32-clean-energy"] >> tasks["teste-dm-32-removeless24"]

    tasks["teste-dm-16-removeless24"] >> tasks["teste-dm-16-addfeatures"]

    tasks["teste-ml-25-splitdata"] >> tasks["teste-ml-25-trainforecasting"]

    tasks["teste-ml-25-splitdata"] >> tasks["teste-ml-25-optimize"]

    tasks["teste-ml-25-splitdata"] >> tasks["teste-ml-25-predict"]

    tasks["teste-ml-16-trainforecasting"] >> tasks["teste-ml-16-optimize"]

    tasks["teste-ml-16-trainforecasting"] >> tasks["teste-ml-16-fitmodel"]

    tasks["teste-ml-16-splitdata"] >> tasks["teste-ml-16-optimize"]

    tasks["teste-ml-16-splitdata"] >> tasks["teste-ml-16-predict"]

    tasks["teste-ml-16-splitdata"] >> tasks["teste-ml-16-trainforecasting"]

    tasks["teste-ml-35-trainforecasting"] >> tasks["teste-ml-35-fitmodel"]

    tasks["teste-ml-35-trainforecasting"] >> tasks["teste-ml-35-optimize"]

    tasks["teste-ml-35-optimize"] >> tasks["teste-ml-35-fitmodel"]

    tasks["teste-dm-20-removeless24"] >> tasks["teste-dm-20-addfeatures"]

    tasks["teste-ml-5-splitdata"] >> tasks["teste-ml-5-trainforecasting"]

    tasks["teste-ml-5-splitdata"] >> tasks["teste-ml-5-optimize"]

    tasks["teste-ml-5-splitdata"] >> tasks["teste-ml-5-predict"]

    tasks["teste-dm-42-clean-energy"] >> tasks["teste-dm-42-removeless24"]

    tasks["teste-ml-15-fitmodel"] >> tasks["teste-ml-15-predict"]

    tasks["teste-ml-15-splitdata"] >> tasks["teste-ml-15-predict"]

    tasks["teste-ml-15-splitdata"] >> tasks["teste-ml-15-optimize"]

    tasks["teste-ml-15-splitdata"] >> tasks["teste-ml-15-trainforecasting"]

    tasks["teste-ml-0-optimize"] >> tasks["teste-ml-0-fitmodel"]

    tasks["teste-ml-0-trainforecasting"] >> tasks["teste-ml-0-fitmodel"]

    tasks["teste-ml-0-trainforecasting"] >> tasks["teste-ml-0-optimize"]

    tasks["teste-ml-18-splitdata"] >> tasks["teste-ml-18-trainforecasting"]

    tasks["teste-ml-18-splitdata"] >> tasks["teste-ml-18-predict"]

    tasks["teste-ml-18-splitdata"] >> tasks["teste-ml-18-optimize"]

    tasks["teste-ml-30-trainforecasting"] >> tasks["teste-ml-30-fitmodel"]

    tasks["teste-ml-30-trainforecasting"] >> tasks["teste-ml-30-optimize"]

    tasks["teste-ml-30-optimize"] >> tasks["teste-ml-30-fitmodel"]

    tasks["teste-ml-19-splitdata"] >> tasks["teste-ml-19-trainforecasting"]

    tasks["teste-ml-19-splitdata"] >> tasks["teste-ml-19-predict"]

    tasks["teste-ml-19-splitdata"] >> tasks["teste-ml-19-optimize"]

    tasks["teste-dm-40-preprocessdata"] >> tasks["teste-dm-40-clean-energy"]

    tasks["teste-dm-1-removeless24"] >> tasks["teste-dm-1-addfeatures"]

    tasks["teste-dm-6-preprocessdata"] >> tasks["teste-dm-6-clean-energy"]

    tasks["teste-da-30-downfiles"] >> tasks["teste-dm-30-preprocessdata"]

    tasks["teste-da-30-downfiles"] >> tasks["teste-ml-30-writedata"]

    tasks["teste-ml-45-trainforecasting"] >> tasks["teste-ml-45-fitmodel"]

    tasks["teste-ml-45-trainforecasting"] >> tasks["teste-ml-45-optimize"]

    tasks["teste-ml-45-optimize"] >> tasks["teste-ml-45-fitmodel"]

    tasks["teste-ml-0-splitdata"] >> tasks["teste-ml-0-trainforecasting"]

    tasks["teste-ml-0-splitdata"] >> tasks["teste-ml-0-predict"]

    tasks["teste-ml-0-splitdata"] >> tasks["teste-ml-0-optimize"]

    tasks["teste-ml-40-optimize"] >> tasks["teste-ml-40-fitmodel"]

    tasks["teste-ml-40-trainforecasting"] >> tasks["teste-ml-40-fitmodel"]

    tasks["teste-ml-40-trainforecasting"] >> tasks["teste-ml-40-optimize"]

    tasks["teste-da-45-downfiles"] >> tasks["teste-dm-45-preprocessdata"]

    tasks["teste-da-45-downfiles"] >> tasks["teste-ml-45-writedata"]

    tasks["teste-da-18-downfiles"] >> tasks["teste-dm-18-preprocessdata"]

    tasks["teste-da-18-downfiles"] >> tasks["teste-ml-18-writedata"]

    tasks["teste-da-34-downfiles"] >> tasks["teste-dm-34-preprocessdata"]

    tasks["teste-da-34-downfiles"] >> tasks["teste-ml-34-writedata"]

    tasks["teste-dm-26-addfeatures"] >> tasks["teste-ml-26-splitdata"]

    tasks["teste-da-3-downfiles"] >> tasks["teste-ml-3-writedata"]

    tasks["teste-da-3-downfiles"] >> tasks["teste-dm-3-preprocessdata"]

    tasks["teste-ml-3-predict"] >> tasks["teste-ml-3-writedata"]

    tasks["teste-da-35-downfiles"] >> tasks["teste-dm-35-preprocessdata"]

    tasks["teste-da-35-downfiles"] >> tasks["teste-ml-35-writedata"]

    tasks["teste-ml-38-optimize"] >> tasks["teste-ml-38-fitmodel"]

    tasks["teste-ml-38-trainforecasting"] >> tasks["teste-ml-38-fitmodel"]

    tasks["teste-ml-38-trainforecasting"] >> tasks["teste-ml-38-optimize"]

    tasks["teste-ml-21-trainforecasting"] >> tasks["teste-ml-21-fitmodel"]

    tasks["teste-ml-21-trainforecasting"] >> tasks["teste-ml-21-optimize"]

    tasks["teste-ml-21-optimize"] >> tasks["teste-ml-21-fitmodel"]

    tasks["teste-dm-36-removeless24"] >> tasks["teste-dm-36-addfeatures"]

    tasks["teste-ml-1-predict"] >> tasks["teste-ml-1-writedata"]

    tasks["teste-da-1-downfiles"] >> tasks["teste-ml-1-writedata"]

    tasks["teste-da-1-downfiles"] >> tasks["teste-dm-1-preprocessdata"]

    tasks["teste-da-44-downfiles"] >> tasks["teste-ml-44-writedata"]

    tasks["teste-da-44-downfiles"] >> tasks["teste-dm-44-preprocessdata"]

    tasks["teste-ml-44-predict"] >> tasks["teste-ml-44-writedata"]

    tasks["teste-dm-45-addfeatures"] >> tasks["teste-ml-45-splitdata"]

    tasks["teste-dm-23-preprocessdata"] >> tasks["teste-dm-23-clean-energy"]

    tasks["teste-ml-0-fitmodel"] >> tasks["teste-ml-0-predict"]

    tasks["teste-dm-37-removeless24"] >> tasks["teste-dm-37-addfeatures"]

    tasks["teste-dm-12-addfeatures"] >> tasks["teste-ml-12-splitdata"]

    tasks["teste-ml-1-trainforecasting"] >> tasks["teste-ml-1-optimize"]

    tasks["teste-ml-1-trainforecasting"] >> tasks["teste-ml-1-fitmodel"]

    tasks["teste-ml-1-splitdata"] >> tasks["teste-ml-1-optimize"]

    tasks["teste-ml-1-splitdata"] >> tasks["teste-ml-1-predict"]

    tasks["teste-ml-1-splitdata"] >> tasks["teste-ml-1-trainforecasting"]

    tasks["teste-dm-33-clean-energy"] >> tasks["teste-dm-33-removeless24"]

    tasks["teste-ml-39-trainforecasting"] >> tasks["teste-ml-39-optimize"]

    tasks["teste-ml-39-trainforecasting"] >> tasks["teste-ml-39-fitmodel"]

    tasks["teste-ml-39-splitdata"] >> tasks["teste-ml-39-optimize"]

    tasks["teste-ml-39-splitdata"] >> tasks["teste-ml-39-trainforecasting"]

    tasks["teste-ml-39-splitdata"] >> tasks["teste-ml-39-predict"]

    tasks["teste-dm-35-preprocessdata"] >> tasks["teste-dm-35-clean-energy"]

    tasks["teste-dm-40-removeless24"] >> tasks["teste-dm-40-addfeatures"]

    tasks["teste-dm-24-clean-energy"] >> tasks["teste-dm-24-removeless24"]

    tasks["teste-dm-21-clean-energy"] >> tasks["teste-dm-21-removeless24"]

    tasks["teste-dm-29-addfeatures"] >> tasks["teste-ml-29-splitdata"]

    tasks["teste-ml-32-fitmodel"] >> tasks["teste-ml-32-predict"]

    tasks["teste-ml-4-predict"] >> tasks["teste-ml-4-writedata"]

    tasks["teste-da-4-downfiles"] >> tasks["teste-ml-4-writedata"]

    tasks["teste-da-4-downfiles"] >> tasks["teste-dm-4-preprocessdata"]

    tasks["teste-da-29-downfiles"] >> tasks["teste-dm-29-preprocessdata"]

    tasks["teste-da-29-downfiles"] >> tasks["teste-ml-29-writedata"]

    tasks["teste-ml-42-optimize"] >> tasks["teste-ml-42-fitmodel"]

    tasks["teste-ml-42-trainforecasting"] >> tasks["teste-ml-42-fitmodel"]

    tasks["teste-ml-42-trainforecasting"] >> tasks["teste-ml-42-optimize"]

    tasks["teste-dm-7-addfeatures"] >> tasks["teste-ml-7-splitdata"]

    tasks["teste-ml-16-fitmodel"] >> tasks["teste-ml-16-predict"]

    tasks["teste-ml-7-trainforecasting"] >> tasks["teste-ml-7-optimize"]

    tasks["teste-ml-7-trainforecasting"] >> tasks["teste-ml-7-fitmodel"]

    tasks["teste-ml-7-splitdata"] >> tasks["teste-ml-7-optimize"]

    tasks["teste-ml-7-splitdata"] >> tasks["teste-ml-7-trainforecasting"]

    tasks["teste-ml-7-splitdata"] >> tasks["teste-ml-7-predict"]

    tasks["teste-da-41-downfiles"] >> tasks["teste-ml-41-writedata"]

    tasks["teste-da-41-downfiles"] >> tasks["teste-dm-41-preprocessdata"]

    tasks["teste-ml-41-predict"] >> tasks["teste-ml-41-writedata"]

    tasks["teste-dm-11-preprocessdata"] >> tasks["teste-dm-11-clean-energy"]

    tasks["teste-dm-0-addfeatures"] >> tasks["teste-ml-0-splitdata"]

    tasks["teste-ml-24-optimize"] >> tasks["teste-ml-24-fitmodel"]

    tasks["teste-ml-24-trainforecasting"] >> tasks["teste-ml-24-fitmodel"]

    tasks["teste-ml-24-trainforecasting"] >> tasks["teste-ml-24-optimize"]

    tasks["teste-dm-22-preprocessdata"] >> tasks["teste-dm-22-clean-energy"]

    tasks["teste-dm-4-clean-energy"] >> tasks["teste-dm-4-removeless24"]

    tasks["teste-ml-9-optimize"] >> tasks["teste-ml-9-fitmodel"]

    tasks["teste-ml-9-trainforecasting"] >> tasks["teste-ml-9-fitmodel"]

    tasks["teste-ml-9-trainforecasting"] >> tasks["teste-ml-9-optimize"]

    tasks["teste-da-25-downfiles"] >> tasks["teste-dm-25-preprocessdata"]

    tasks["teste-da-25-downfiles"] >> tasks["teste-ml-25-writedata"]

    tasks["teste-dm-13-preprocessdata"] >> tasks["teste-dm-13-clean-energy"]

    tasks["teste-ml-45-splitdata"] >> tasks["teste-ml-45-predict"]

    tasks["teste-ml-45-splitdata"] >> tasks["teste-ml-45-optimize"]

    tasks["teste-ml-45-splitdata"] >> tasks["teste-ml-45-trainforecasting"]

    tasks["teste-ml-45-fitmodel"] >> tasks["teste-ml-45-predict"]

    tasks["teste-da-36-downfiles"] >> tasks["teste-dm-36-preprocessdata"]

    tasks["teste-da-36-downfiles"] >> tasks["teste-ml-36-writedata"]

    tasks["teste-dm-46-addfeatures"] >> tasks["teste-ml-46-splitdata"]

    tasks["teste-dm-4-removeless24"] >> tasks["teste-dm-4-addfeatures"]

    tasks["teste-ml-18-predict"] >> tasks["teste-ml-18-writedata"]

    tasks["teste-dm-43-addfeatures"] >> tasks["teste-ml-43-splitdata"]

    tasks["teste-ml-12-splitdata"] >> tasks["teste-ml-12-trainforecasting"]

    tasks["teste-ml-12-splitdata"] >> tasks["teste-ml-12-predict"]

    tasks["teste-ml-12-splitdata"] >> tasks["teste-ml-12-optimize"]

    tasks["teste-dm-17-clean-energy"] >> tasks["teste-dm-17-removeless24"]

    tasks["teste-dm-33-removeless24"] >> tasks["teste-dm-33-addfeatures"]

    tasks["teste-ml-0-predict"] >> tasks["teste-ml-0-writedata"]

    tasks["teste-da-0-downfiles"] >> tasks["teste-ml-0-writedata"]

    tasks["teste-da-0-downfiles"] >> tasks["teste-dm-0-preprocessdata"]

    tasks["teste-da-2-downfiles"] >> tasks["teste-ml-2-writedata"]

    tasks["teste-da-2-downfiles"] >> tasks["teste-dm-2-preprocessdata"]

    tasks["teste-ml-2-predict"] >> tasks["teste-ml-2-writedata"]

    tasks["teste-da-8-downfiles"] >> tasks["teste-ml-8-writedata"]

    tasks["teste-da-8-downfiles"] >> tasks["teste-dm-8-preprocessdata"]

    tasks["teste-ml-8-predict"] >> tasks["teste-ml-8-writedata"]

    tasks["teste-da-13-downfiles"] >> tasks["teste-dm-13-preprocessdata"]

    tasks["teste-da-13-downfiles"] >> tasks["teste-ml-13-writedata"]

    tasks["teste-ml-20-optimize"] >> tasks["teste-ml-20-fitmodel"]

    tasks["teste-dm-10-removeless24"] >> tasks["teste-dm-10-addfeatures"]

    tasks["teste-ml-49-optimize"] >> tasks["teste-ml-49-fitmodel"]

    tasks["teste-ml-49-trainforecasting"] >> tasks["teste-ml-49-fitmodel"]

    tasks["teste-ml-49-trainforecasting"] >> tasks["teste-ml-49-optimize"]

    tasks["teste-ml-35-splitdata"] >> tasks["teste-ml-35-trainforecasting"]

    tasks["teste-ml-35-splitdata"] >> tasks["teste-ml-35-optimize"]

    tasks["teste-ml-35-splitdata"] >> tasks["teste-ml-35-predict"]

    tasks["teste-dm-13-removeless24"] >> tasks["teste-dm-13-addfeatures"]

    tasks["teste-dm-22-clean-energy"] >> tasks["teste-dm-22-removeless24"]

    tasks["teste-da-42-downfiles"] >> tasks["teste-ml-42-writedata"]

    tasks["teste-da-42-downfiles"] >> tasks["teste-dm-42-preprocessdata"]

    tasks["teste-ml-42-predict"] >> tasks["teste-ml-42-writedata"]

    tasks["teste-ml-47-fitmodel"] >> tasks["teste-ml-47-predict"]

    tasks["teste-ml-47-splitdata"] >> tasks["teste-ml-47-predict"]

    tasks["teste-ml-47-splitdata"] >> tasks["teste-ml-47-trainforecasting"]

    tasks["teste-ml-47-splitdata"] >> tasks["teste-ml-47-optimize"]

    tasks["teste-dm-19-clean-energy"] >> tasks["teste-dm-19-removeless24"]

    tasks["teste-dm-39-removeless24"] >> tasks["teste-dm-39-addfeatures"]

    tasks["teste-ml-7-optimize"] >> tasks["teste-ml-7-fitmodel"]

    tasks["teste-da-43-downfiles"] >> tasks["teste-ml-43-writedata"]

    tasks["teste-da-43-downfiles"] >> tasks["teste-dm-43-preprocessdata"]

    tasks["teste-ml-43-predict"] >> tasks["teste-ml-43-writedata"]

    tasks["teste-da-37-downfiles"] >> tasks["teste-ml-37-writedata"]

    tasks["teste-da-37-downfiles"] >> tasks["teste-dm-37-preprocessdata"]

    tasks["teste-ml-37-predict"] >> tasks["teste-ml-37-writedata"]

    tasks["teste-dm-28-addfeatures"] >> tasks["teste-ml-28-splitdata"]

    tasks["teste-dm-46-removeless24"] >> tasks["teste-dm-46-addfeatures"]

    tasks["teste-dm-25-preprocessdata"] >> tasks["teste-dm-25-clean-energy"]

    tasks["teste-dm-48-clean-energy"] >> tasks["teste-dm-48-removeless24"]

    tasks["teste-ml-27-splitdata"] >> tasks["teste-ml-27-optimize"]

    tasks["teste-ml-27-splitdata"] >> tasks["teste-ml-27-predict"]

    tasks["teste-ml-27-splitdata"] >> tasks["teste-ml-27-trainforecasting"]

    tasks["teste-ml-27-trainforecasting"] >> tasks["teste-ml-27-optimize"]

    tasks["teste-ml-27-trainforecasting"] >> tasks["teste-ml-27-fitmodel"]

    tasks["teste-dm-24-preprocessdata"] >> tasks["teste-dm-24-clean-energy"]

    tasks["teste-dm-16-addfeatures"] >> tasks["teste-ml-16-splitdata"]

    tasks["teste-dm-16-preprocessdata"] >> tasks["teste-dm-16-clean-energy"]

    tasks["teste-ml-13-splitdata"] >> tasks["teste-ml-13-trainforecasting"]

    tasks["teste-ml-13-splitdata"] >> tasks["teste-ml-13-optimize"]

    tasks["teste-ml-13-splitdata"] >> tasks["teste-ml-13-predict"]

    tasks["teste-dm-36-clean-energy"] >> tasks["teste-dm-36-removeless24"]

    tasks["teste-dm-43-preprocessdata"] >> tasks["teste-dm-43-clean-energy"]

    tasks["teste-da-9-downfiles"] >> tasks["teste-ml-9-writedata"]

    tasks["teste-da-9-downfiles"] >> tasks["teste-dm-9-preprocessdata"]

    tasks["teste-ml-9-predict"] >> tasks["teste-ml-9-writedata"]

    tasks["teste-dm-31-addfeatures"] >> tasks["teste-ml-31-splitdata"]

    tasks["teste-ml-15-trainforecasting"] >> tasks["teste-ml-15-optimize"]

    tasks["teste-ml-15-trainforecasting"] >> tasks["teste-ml-15-fitmodel"]

    tasks["teste-dm-26-removeless24"] >> tasks["teste-dm-26-addfeatures"]

    tasks["teste-dm-30-clean-energy"] >> tasks["teste-dm-30-removeless24"]

    tasks["teste-ml-29-optimize"] >> tasks["teste-ml-29-fitmodel"]

    tasks["teste-ml-29-trainforecasting"] >> tasks["teste-ml-29-fitmodel"]

    tasks["teste-ml-29-trainforecasting"] >> tasks["teste-ml-29-optimize"]

    tasks["teste-ml-42-splitdata"] >> tasks["teste-ml-42-optimize"]

    tasks["teste-ml-42-splitdata"] >> tasks["teste-ml-42-predict"]

    tasks["teste-ml-42-splitdata"] >> tasks["teste-ml-42-trainforecasting"]

    tasks["teste-ml-43-fitmodel"] >> tasks["teste-ml-43-predict"]

    tasks["teste-dm-29-removeless24"] >> tasks["teste-dm-29-addfeatures"]

    tasks["teste-dm-12-removeless24"] >> tasks["teste-dm-12-addfeatures"]

    tasks["teste-dm-6-clean-energy"] >> tasks["teste-dm-6-removeless24"]

    tasks["teste-ml-37-trainforecasting"] >> tasks["teste-ml-37-optimize"]

    tasks["teste-ml-37-trainforecasting"] >> tasks["teste-ml-37-fitmodel"]

    tasks["teste-ml-37-splitdata"] >> tasks["teste-ml-37-optimize"]

    tasks["teste-ml-37-splitdata"] >> tasks["teste-ml-37-predict"]

    tasks["teste-ml-37-splitdata"] >> tasks["teste-ml-37-trainforecasting"]

    tasks["teste-dm-11-addfeatures"] >> tasks["teste-ml-11-splitdata"]

    tasks["teste-dm-44-addfeatures"] >> tasks["teste-ml-44-splitdata"]

    tasks["teste-ml-8-splitdata"] >> tasks["teste-ml-8-optimize"]

    tasks["teste-ml-8-splitdata"] >> tasks["teste-ml-8-predict"]

    tasks["teste-ml-8-splitdata"] >> tasks["teste-ml-8-trainforecasting"]

    tasks["teste-ml-8-trainforecasting"] >> tasks["teste-ml-8-optimize"]

    tasks["teste-ml-8-trainforecasting"] >> tasks["teste-ml-8-fitmodel"]

    tasks["teste-ml-11-trainforecasting"] >> tasks["teste-ml-11-optimize"]

    tasks["teste-ml-11-trainforecasting"] >> tasks["teste-ml-11-fitmodel"]

    tasks["teste-ml-11-splitdata"] >> tasks["teste-ml-11-optimize"]

    tasks["teste-ml-11-splitdata"] >> tasks["teste-ml-11-trainforecasting"]

    tasks["teste-ml-11-splitdata"] >> tasks["teste-ml-11-predict"]

    tasks["teste-dm-3-removeless24"] >> tasks["teste-dm-3-addfeatures"]

    tasks["teste-dm-23-clean-energy"] >> tasks["teste-dm-23-removeless24"]

    tasks["teste-ml-49-splitdata"] >> tasks["teste-ml-49-optimize"]

    tasks["teste-ml-49-splitdata"] >> tasks["teste-ml-49-trainforecasting"]

    tasks["teste-ml-49-splitdata"] >> tasks["teste-ml-49-predict"]

    tasks["teste-ml-6-splitdata"] >> tasks["teste-ml-6-trainforecasting"]

    tasks["teste-ml-6-splitdata"] >> tasks["teste-ml-6-optimize"]

    tasks["teste-ml-6-splitdata"] >> tasks["teste-ml-6-predict"]

    tasks["teste-ml-11-optimize"] >> tasks["teste-ml-11-fitmodel"]

    tasks["teste-ml-42-fitmodel"] >> tasks["teste-ml-42-predict"]

    tasks["teste-ml-7-fitmodel"] >> tasks["teste-ml-7-predict"]

    tasks["teste-ml-40-predict"] >> tasks["teste-ml-40-writedata"]

    tasks["teste-da-6-downfiles"] >> tasks["teste-ml-6-writedata"]

    tasks["teste-da-6-downfiles"] >> tasks["teste-dm-6-preprocessdata"]

    tasks["teste-ml-6-predict"] >> tasks["teste-ml-6-writedata"]

    tasks["teste-da-22-downfiles"] >> tasks["teste-dm-22-preprocessdata"]

    tasks["teste-da-22-downfiles"] >> tasks["teste-ml-22-writedata"]

    tasks["teste-da-26-downfiles"] >> tasks["teste-dm-26-preprocessdata"]

    tasks["teste-da-26-downfiles"] >> tasks["teste-ml-26-writedata"]

    tasks["teste-dm-12-preprocessdata"] >> tasks["teste-dm-12-clean-energy"]

    tasks["teste-dm-0-clean-energy"] >> tasks["teste-dm-0-removeless24"]

    tasks["teste-dm-25-clean-energy"] >> tasks["teste-dm-25-removeless24"]

    tasks["teste-ml-49-fitmodel"] >> tasks["teste-ml-49-predict"]

    tasks["teste-ml-3-splitdata"] >> tasks["teste-ml-3-trainforecasting"]

    tasks["teste-ml-3-splitdata"] >> tasks["teste-ml-3-optimize"]

    tasks["teste-ml-3-splitdata"] >> tasks["teste-ml-3-predict"]

    tasks["teste-dm-38-removeless24"] >> tasks["teste-dm-38-addfeatures"]

    tasks["teste-dm-31-removeless24"] >> tasks["teste-dm-31-addfeatures"]

    tasks["teste-ml-12-fitmodel"] >> tasks["teste-ml-12-predict"]

    tasks["teste-ml-47-optimize"] >> tasks["teste-ml-47-fitmodel"]

    tasks["teste-ml-47-trainforecasting"] >> tasks["teste-ml-47-fitmodel"]

    tasks["teste-ml-47-trainforecasting"] >> tasks["teste-ml-47-optimize"]

    tasks["teste-ml-10-fitmodel"] >> tasks["teste-ml-10-predict"]

    tasks["teste-ml-10-splitdata"] >> tasks["teste-ml-10-predict"]

    tasks["teste-ml-10-splitdata"] >> tasks["teste-ml-10-trainforecasting"]

    tasks["teste-ml-10-splitdata"] >> tasks["teste-ml-10-optimize"]

    tasks["teste-ml-28-splitdata"] >> tasks["teste-ml-28-optimize"]

    tasks["teste-ml-28-splitdata"] >> tasks["teste-ml-28-trainforecasting"]

    tasks["teste-ml-28-splitdata"] >> tasks["teste-ml-28-predict"]

    tasks["teste-ml-28-trainforecasting"] >> tasks["teste-ml-28-optimize"]

    tasks["teste-ml-28-trainforecasting"] >> tasks["teste-ml-28-fitmodel"]

    tasks["teste-dm-36-addfeatures"] >> tasks["teste-ml-36-splitdata"]

    tasks["teste-ml-25-trainforecasting"] >> tasks["teste-ml-25-fitmodel"]

    tasks["teste-ml-25-trainforecasting"] >> tasks["teste-ml-25-optimize"]

    tasks["teste-ml-25-optimize"] >> tasks["teste-ml-25-fitmodel"]

    tasks["teste-ml-48-optimize"] >> tasks["teste-ml-48-fitmodel"]

    tasks["teste-ml-48-trainforecasting"] >> tasks["teste-ml-48-fitmodel"]

    tasks["teste-ml-48-trainforecasting"] >> tasks["teste-ml-48-optimize"]

    tasks["teste-dm-9-addfeatures"] >> tasks["teste-ml-9-splitdata"]

    tasks["teste-dm-27-removeless24"] >> tasks["teste-dm-27-addfeatures"]

    tasks["teste-dm-7-clean-energy"] >> tasks["teste-dm-7-removeless24"]

    tasks["teste-da-31-downfiles"] >> tasks["teste-dm-31-preprocessdata"]

    tasks["teste-da-31-downfiles"] >> tasks["teste-ml-31-writedata"]

    tasks["teste-dm-41-removeless24"] >> tasks["teste-dm-41-addfeatures"]

    tasks["teste-ml-2-splitdata"] >> tasks["teste-ml-2-trainforecasting"]

    tasks["teste-ml-2-splitdata"] >> tasks["teste-ml-2-predict"]

    tasks["teste-ml-2-splitdata"] >> tasks["teste-ml-2-optimize"]

    tasks["teste-da-14-downfiles"] >> tasks["teste-dm-14-preprocessdata"]

    tasks["teste-da-14-downfiles"] >> tasks["teste-ml-14-writedata"]

    tasks["teste-dm-27-preprocessdata"] >> tasks["teste-dm-27-clean-energy"]

    tasks["teste-dm-8-addfeatures"] >> tasks["teste-ml-8-splitdata"]

    tasks["teste-ml-14-predict"] >> tasks["teste-ml-14-writedata"]

    tasks["teste-ml-17-fitmodel"] >> tasks["teste-ml-17-predict"]

    tasks["teste-ml-17-splitdata"] >> tasks["teste-ml-17-predict"]

    tasks["teste-ml-17-splitdata"] >> tasks["teste-ml-17-optimize"]

    tasks["teste-ml-17-splitdata"] >> tasks["teste-ml-17-trainforecasting"]

    tasks["teste-dm-41-preprocessdata"] >> tasks["teste-dm-41-clean-energy"]

    tasks["teste-ml-24-fitmodel"] >> tasks["teste-ml-24-predict"]

    tasks["teste-ml-24-splitdata"] >> tasks["teste-ml-24-predict"]

    tasks["teste-ml-24-splitdata"] >> tasks["teste-ml-24-optimize"]

    tasks["teste-ml-24-splitdata"] >> tasks["teste-ml-24-trainforecasting"]

    tasks["teste-dm-3-addfeatures"] >> tasks["teste-ml-3-splitdata"]

    tasks["teste-ml-48-fitmodel"] >> tasks["teste-ml-48-predict"]

    tasks["teste-ml-48-splitdata"] >> tasks["teste-ml-48-predict"]

    tasks["teste-ml-48-splitdata"] >> tasks["teste-ml-48-trainforecasting"]

    tasks["teste-ml-48-splitdata"] >> tasks["teste-ml-48-optimize"]

    tasks["teste-ml-27-fitmodel"] >> tasks["teste-ml-27-predict"]

    tasks["teste-ml-33-splitdata"] >> tasks["teste-ml-33-trainforecasting"]

    tasks["teste-ml-33-splitdata"] >> tasks["teste-ml-33-optimize"]

    tasks["teste-ml-33-splitdata"] >> tasks["teste-ml-33-predict"]

    tasks["teste-ml-28-optimize"] >> tasks["teste-ml-28-fitmodel"]

    tasks["teste-da-48-downfiles"] >> tasks["teste-ml-48-writedata"]

    tasks["teste-da-48-downfiles"] >> tasks["teste-dm-48-preprocessdata"]

    tasks["teste-ml-48-predict"] >> tasks["teste-ml-48-writedata"]

    tasks["teste-dm-17-removeless24"] >> tasks["teste-dm-17-addfeatures"]

    tasks["teste-ml-35-predict"] >> tasks["teste-ml-35-writedata"]

    tasks["teste-ml-30-splitdata"] >> tasks["teste-ml-30-optimize"]

    tasks["teste-ml-30-splitdata"] >> tasks["teste-ml-30-predict"]

    tasks["teste-ml-30-splitdata"] >> tasks["teste-ml-30-trainforecasting"]

    tasks["teste-dm-21-removeless24"] >> tasks["teste-dm-21-addfeatures"]

    tasks["teste-dm-1-preprocessdata"] >> tasks["teste-dm-1-clean-energy"]

    tasks["teste-dm-29-clean-energy"] >> tasks["teste-dm-29-removeless24"]

    tasks["teste-dm-35-clean-energy"] >> tasks["teste-dm-35-removeless24"]

    tasks["teste-da-46-downfiles"] >> tasks["teste-dm-46-preprocessdata"]

    tasks["teste-da-46-downfiles"] >> tasks["teste-ml-46-writedata"]

    tasks["teste-dm-1-addfeatures"] >> tasks["teste-ml-1-splitdata"]

    tasks["teste-dm-34-addfeatures"] >> tasks["teste-ml-34-splitdata"]

    tasks["teste-ml-3-trainforecasting"] >> tasks["teste-ml-3-optimize"]

    tasks["teste-ml-3-trainforecasting"] >> tasks["teste-ml-3-fitmodel"]

    tasks["teste-ml-22-splitdata"] >> tasks["teste-ml-22-trainforecasting"]

    tasks["teste-ml-22-splitdata"] >> tasks["teste-ml-22-optimize"]

    tasks["teste-ml-22-splitdata"] >> tasks["teste-ml-22-predict"]

    tasks["teste-ml-4-splitdata"] >> tasks["teste-ml-4-optimize"]

    tasks["teste-ml-4-splitdata"] >> tasks["teste-ml-4-trainforecasting"]

    tasks["teste-ml-4-splitdata"] >> tasks["teste-ml-4-predict"]

    tasks["teste-ml-4-trainforecasting"] >> tasks["teste-ml-4-optimize"]

    tasks["teste-ml-4-trainforecasting"] >> tasks["teste-ml-4-fitmodel"]

    tasks["teste-ml-36-splitdata"] >> tasks["teste-ml-36-trainforecasting"]

    tasks["teste-ml-36-splitdata"] >> tasks["teste-ml-36-predict"]

    tasks["teste-ml-36-splitdata"] >> tasks["teste-ml-36-optimize"]

    tasks["teste-ml-31-predict"] >> tasks["teste-ml-31-writedata"]

    tasks["teste-ml-10-trainforecasting"] >> tasks["teste-ml-10-fitmodel"]

    tasks["teste-ml-10-trainforecasting"] >> tasks["teste-ml-10-optimize"]

    tasks["teste-ml-10-optimize"] >> tasks["teste-ml-10-fitmodel"]

    tasks["teste-dm-46-clean-energy"] >> tasks["teste-dm-46-removeless24"]

    tasks["teste-ml-1-fitmodel"] >> tasks["teste-ml-1-predict"]

    tasks["teste-ml-39-optimize"] >> tasks["teste-ml-39-fitmodel"]

    tasks["teste-dm-22-removeless24"] >> tasks["teste-dm-22-addfeatures"]

    tasks["teste-da-7-downfiles"] >> tasks["teste-dm-7-preprocessdata"]

    tasks["teste-da-7-downfiles"] >> tasks["teste-ml-7-writedata"]

    tasks["teste-dm-2-preprocessdata"] >> tasks["teste-dm-2-clean-energy"]

    tasks["teste-ml-13-trainforecasting"] >> tasks["teste-ml-13-optimize"]

    tasks["teste-ml-13-trainforecasting"] >> tasks["teste-ml-13-fitmodel"]

    tasks["teste-ml-26-splitdata"] >> tasks["teste-ml-26-trainforecasting"]

    tasks["teste-ml-26-splitdata"] >> tasks["teste-ml-26-predict"]

    tasks["teste-ml-26-splitdata"] >> tasks["teste-ml-26-optimize"]

    tasks["teste-da-10-downfiles"] >> tasks["teste-ml-10-writedata"]

    tasks["teste-da-10-downfiles"] >> tasks["teste-dm-10-preprocessdata"]

    tasks["teste-ml-10-predict"] >> tasks["teste-ml-10-writedata"]

    tasks["teste-dm-42-removeless24"] >> tasks["teste-dm-42-addfeatures"]

    tasks["teste-dm-22-addfeatures"] >> tasks["teste-ml-22-splitdata"]

    tasks["teste-ml-26-fitmodel"] >> tasks["teste-ml-26-predict"]

    tasks["teste-dm-20-addfeatures"] >> tasks["teste-ml-20-splitdata"]

    tasks["teste-ml-39-fitmodel"] >> tasks["teste-ml-39-predict"]

    tasks["teste-ml-17-trainforecasting"] >> tasks["teste-ml-17-optimize"]

    tasks["teste-ml-17-trainforecasting"] >> tasks["teste-ml-17-fitmodel"]

    tasks["teste-ml-44-fitmodel"] >> tasks["teste-ml-44-predict"]

    tasks["teste-ml-44-splitdata"] >> tasks["teste-ml-44-predict"]

    tasks["teste-ml-44-splitdata"] >> tasks["teste-ml-44-optimize"]

    tasks["teste-ml-44-splitdata"] >> tasks["teste-ml-44-trainforecasting"]

    tasks["teste-dm-44-preprocessdata"] >> tasks["teste-dm-44-clean-energy"]

    tasks["teste-ml-46-splitdata"] >> tasks["teste-ml-46-trainforecasting"]

    tasks["teste-ml-46-splitdata"] >> tasks["teste-ml-46-optimize"]

    tasks["teste-ml-46-splitdata"] >> tasks["teste-ml-46-predict"]

    tasks["teste-ml-9-splitdata"] >> tasks["teste-ml-9-optimize"]

    tasks["teste-ml-9-splitdata"] >> tasks["teste-ml-9-predict"]

    tasks["teste-ml-9-splitdata"] >> tasks["teste-ml-9-trainforecasting"]

    tasks["teste-dm-35-removeless24"] >> tasks["teste-dm-35-addfeatures"]

    tasks["teste-dm-44-removeless24"] >> tasks["teste-dm-44-addfeatures"]

    tasks["teste-dm-39-preprocessdata"] >> tasks["teste-dm-39-clean-energy"]

    tasks["teste-dm-17-preprocessdata"] >> tasks["teste-dm-17-clean-energy"]

    tasks["teste-dm-32-addfeatures"] >> tasks["teste-ml-32-splitdata"]

    tasks["teste-ml-40-splitdata"] >> tasks["teste-ml-40-trainforecasting"]

    tasks["teste-ml-40-splitdata"] >> tasks["teste-ml-40-predict"]

    tasks["teste-ml-40-splitdata"] >> tasks["teste-ml-40-optimize"]

    tasks["teste-dm-18-addfeatures"] >> tasks["teste-ml-18-splitdata"]

    tasks["teste-ml-17-predict"] >> tasks["teste-ml-17-writedata"]

    tasks["teste-da-17-downfiles"] >> tasks["teste-ml-17-writedata"]

    tasks["teste-da-17-downfiles"] >> tasks["teste-dm-17-preprocessdata"]

    tasks["teste-dm-45-clean-energy"] >> tasks["teste-dm-45-removeless24"]

    tasks["teste-dm-5-preprocessdata"] >> tasks["teste-dm-5-clean-energy"]

    tasks["teste-dm-45-removeless24"] >> tasks["teste-dm-45-addfeatures"]

    tasks["teste-dm-8-preprocessdata"] >> tasks["teste-dm-8-clean-energy"]

    tasks["teste-ml-46-predict"] >> tasks["teste-ml-46-writedata"]

    tasks["teste-dm-10-clean-energy"] >> tasks["teste-dm-10-removeless24"]

    tasks["teste-dm-40-addfeatures"] >> tasks["teste-ml-40-splitdata"]

    tasks["teste-dm-31-preprocessdata"] >> tasks["teste-dm-31-clean-energy"]

    tasks["teste-dm-26-preprocessdata"] >> tasks["teste-dm-26-clean-energy"]

    tasks["teste-da-15-downfiles"] >> tasks["teste-dm-15-preprocessdata"]

    tasks["teste-da-15-downfiles"] >> tasks["teste-ml-15-writedata"]

    tasks["teste-dm-14-removeless24"] >> tasks["teste-dm-14-addfeatures"]

    tasks["teste-ml-29-predict"] >> tasks["teste-ml-29-writedata"]

    tasks["teste-dm-42-addfeatures"] >> tasks["teste-ml-42-splitdata"]

    tasks["teste-dm-39-clean-energy"] >> tasks["teste-dm-39-removeless24"]

    tasks["teste-dm-3-clean-energy"] >> tasks["teste-dm-3-removeless24"]

    tasks["teste-ml-39-predict"] >> tasks["teste-ml-39-writedata"]

    tasks["teste-da-39-downfiles"] >> tasks["teste-ml-39-writedata"]

    tasks["teste-da-39-downfiles"] >> tasks["teste-dm-39-preprocessdata"]

    tasks["teste-da-5-downfiles"] >> tasks["teste-dm-5-preprocessdata"]

    tasks["teste-da-5-downfiles"] >> tasks["teste-ml-5-writedata"]

    tasks["teste-dm-19-removeless24"] >> tasks["teste-dm-19-addfeatures"]

    tasks["teste-ml-22-fitmodel"] >> tasks["teste-ml-22-predict"]

    tasks["teste-dm-21-preprocessdata"] >> tasks["teste-dm-21-clean-energy"]

    tasks["teste-ml-37-fitmodel"] >> tasks["teste-ml-37-predict"]

    tasks["teste-ml-1-optimize"] >> tasks["teste-ml-1-fitmodel"]

    tasks["teste-ml-17-optimize"] >> tasks["teste-ml-17-fitmodel"]

    tasks["teste-dm-2-addfeatures"] >> tasks["teste-ml-2-splitdata"]

    tasks["teste-dm-47-preprocessdata"] >> tasks["teste-dm-47-clean-energy"]

    tasks["teste-dm-12-clean-energy"] >> tasks["teste-dm-12-removeless24"]

    tasks["teste-ml-13-fitmodel"] >> tasks["teste-ml-13-predict"]

    tasks["teste-ml-9-fitmodel"] >> tasks["teste-ml-9-predict"]

    tasks["teste-ml-23-trainforecasting"] >> tasks["teste-ml-23-fitmodel"]

    tasks["teste-ml-23-trainforecasting"] >> tasks["teste-ml-23-optimize"]

    tasks["teste-ml-23-optimize"] >> tasks["teste-ml-23-fitmodel"]

    tasks["teste-ml-36-optimize"] >> tasks["teste-ml-36-fitmodel"]

    tasks["teste-ml-36-trainforecasting"] >> tasks["teste-ml-36-fitmodel"]

    tasks["teste-ml-36-trainforecasting"] >> tasks["teste-ml-36-optimize"]

    tasks["teste-ml-47-predict"] >> tasks["teste-ml-47-writedata"]

    tasks["teste-da-47-downfiles"] >> tasks["teste-ml-47-writedata"]

    tasks["teste-da-47-downfiles"] >> tasks["teste-dm-47-preprocessdata"]

    tasks["teste-ml-8-fitmodel"] >> tasks["teste-ml-8-predict"]

    tasks["teste-ml-26-optimize"] >> tasks["teste-ml-26-fitmodel"]

    tasks["teste-ml-26-trainforecasting"] >> tasks["teste-ml-26-fitmodel"]

    tasks["teste-ml-26-trainforecasting"] >> tasks["teste-ml-26-optimize"]

    tasks["teste-ml-33-trainforecasting"] >> tasks["teste-ml-33-optimize"]

    tasks["teste-ml-33-trainforecasting"] >> tasks["teste-ml-33-fitmodel"]

    tasks["teste-da-33-downfiles"] >> tasks["teste-dm-33-preprocessdata"]

    tasks["teste-da-33-downfiles"] >> tasks["teste-ml-33-writedata"]

    tasks["teste-ml-30-fitmodel"] >> tasks["teste-ml-30-predict"]

    tasks["teste-ml-26-predict"] >> tasks["teste-ml-26-writedata"]

    tasks["teste-dm-49-removeless24"] >> tasks["teste-dm-49-addfeatures"]

    tasks["teste-ml-44-trainforecasting"] >> tasks["teste-ml-44-optimize"]

    tasks["teste-ml-44-trainforecasting"] >> tasks["teste-ml-44-fitmodel"]

    tasks["teste-dm-30-addfeatures"] >> tasks["teste-ml-30-splitdata"]

    tasks["teste-da-23-downfiles"] >> tasks["teste-ml-23-writedata"]

    tasks["teste-da-23-downfiles"] >> tasks["teste-dm-23-preprocessdata"]

    tasks["teste-ml-23-predict"] >> tasks["teste-ml-23-writedata"]

    tasks["teste-ml-27-optimize"] >> tasks["teste-ml-27-fitmodel"]

    tasks["teste-dm-23-removeless24"] >> tasks["teste-dm-23-addfeatures"]

    tasks["teste-ml-13-optimize"] >> tasks["teste-ml-13-fitmodel"]

    tasks["teste-ml-41-fitmodel"] >> tasks["teste-ml-41-predict"]

    tasks["teste-ml-46-trainforecasting"] >> tasks["teste-ml-46-optimize"]

    tasks["teste-ml-46-trainforecasting"] >> tasks["teste-ml-46-fitmodel"]

    tasks["teste-dm-28-removeless24"] >> tasks["teste-dm-28-addfeatures"]

    tasks["teste-ml-5-fitmodel"] >> tasks["teste-ml-5-predict"]

    tasks["teste-ml-38-splitdata"] >> tasks["teste-ml-38-trainforecasting"]

    tasks["teste-ml-38-splitdata"] >> tasks["teste-ml-38-predict"]

    tasks["teste-ml-38-splitdata"] >> tasks["teste-ml-38-optimize"]

    tasks["teste-ml-18-fitmodel"] >> tasks["teste-ml-18-predict"]

    tasks["teste-ml-6-optimize"] >> tasks["teste-ml-6-fitmodel"]

    tasks["teste-ml-6-trainforecasting"] >> tasks["teste-ml-6-fitmodel"]

    tasks["teste-ml-6-trainforecasting"] >> tasks["teste-ml-6-optimize"]

    tasks["teste-dm-19-addfeatures"] >> tasks["teste-ml-19-splitdata"]

    tasks["teste-ml-23-splitdata"] >> tasks["teste-ml-23-trainforecasting"]

    tasks["teste-ml-23-splitdata"] >> tasks["teste-ml-23-predict"]

    tasks["teste-ml-23-splitdata"] >> tasks["teste-ml-23-optimize"]

    tasks["teste-ml-40-fitmodel"] >> tasks["teste-ml-40-predict"]

    tasks["teste-dm-18-removeless24"] >> tasks["teste-dm-18-addfeatures"]

    tasks["teste-ml-11-predict"] >> tasks["teste-ml-11-writedata"]

    tasks["teste-da-11-downfiles"] >> tasks["teste-ml-11-writedata"]

    tasks["teste-da-11-downfiles"] >> tasks["teste-dm-11-preprocessdata"]

    tasks["teste-da-38-downfiles"] >> tasks["teste-dm-38-preprocessdata"]

    tasks["teste-da-38-downfiles"] >> tasks["teste-ml-38-writedata"]

    tasks["teste-dm-43-removeless24"] >> tasks["teste-dm-43-addfeatures"]

    tasks["teste-ml-33-fitmodel"] >> tasks["teste-ml-33-predict"]

    tasks["teste-ml-14-trainforecasting"] >> tasks["teste-ml-14-optimize"]

    tasks["teste-ml-14-trainforecasting"] >> tasks["teste-ml-14-fitmodel"]

    tasks["teste-ml-14-splitdata"] >> tasks["teste-ml-14-optimize"]

    tasks["teste-ml-14-splitdata"] >> tasks["teste-ml-14-trainforecasting"]

    tasks["teste-ml-14-splitdata"] >> tasks["teste-ml-14-predict"]

    tasks["teste-dm-5-addfeatures"] >> tasks["teste-ml-5-splitdata"]

    tasks["teste-ml-16-optimize"] >> tasks["teste-ml-16-fitmodel"]

    tasks["teste-dm-41-clean-energy"] >> tasks["teste-dm-41-removeless24"]

    tasks["teste-ml-49-predict"] >> tasks["teste-ml-49-writedata"]

    tasks["teste-da-49-downfiles"] >> tasks["teste-ml-49-writedata"]

    tasks["teste-da-49-downfiles"] >> tasks["teste-dm-49-preprocessdata"]

    tasks["teste-dm-10-preprocessdata"] >> tasks["teste-dm-10-clean-energy"]

    tasks["teste-ml-4-optimize"] >> tasks["teste-ml-4-fitmodel"]

    tasks["teste-ml-33-optimize"] >> tasks["teste-ml-33-fitmodel"]

    tasks["teste-ml-13-predict"] >> tasks["teste-ml-13-writedata"]

    tasks["teste-dm-18-preprocessdata"] >> tasks["teste-dm-18-clean-energy"]

    tasks["teste-da-27-downfiles"] >> tasks["teste-dm-27-preprocessdata"]

    tasks["teste-da-27-downfiles"] >> tasks["teste-ml-27-writedata"]

    tasks["teste-dm-25-removeless24"] >> tasks["teste-dm-25-addfeatures"]

    tasks["teste-da-21-downfiles"] >> tasks["teste-dm-21-preprocessdata"]

    tasks["teste-da-21-downfiles"] >> tasks["teste-ml-21-writedata"]

    tasks["teste-ml-2-fitmodel"] >> tasks["teste-ml-2-predict"]

    tasks["teste-dm-21-addfeatures"] >> tasks["teste-ml-21-splitdata"]

    tasks["teste-ml-41-trainforecasting"] >> tasks["teste-ml-41-optimize"]

    tasks["teste-ml-41-trainforecasting"] >> tasks["teste-ml-41-fitmodel"]

    tasks["teste-dm-13-clean-energy"] >> tasks["teste-dm-13-removeless24"]

    tasks["teste-dm-5-clean-energy"] >> tasks["teste-dm-5-removeless24"]

    tasks["teste-dm-2-removeless24"] >> tasks["teste-dm-2-addfeatures"]

    tasks["teste-ml-23-fitmodel"] >> tasks["teste-ml-23-predict"]

    tasks["teste-ml-36-fitmodel"] >> tasks["teste-ml-36-predict"]

    tasks["teste-dm-9-clean-energy"] >> tasks["teste-dm-9-removeless24"]

    tasks["teste-dm-8-removeless24"] >> tasks["teste-dm-8-addfeatures"]

    tasks["teste-dm-32-preprocessdata"] >> tasks["teste-dm-32-clean-energy"]

    tasks["teste-dm-38-clean-energy"] >> tasks["teste-dm-38-removeless24"]

    tasks["teste-ml-21-splitdata"] >> tasks["teste-ml-21-optimize"]

    tasks["teste-ml-21-splitdata"] >> tasks["teste-ml-21-predict"]

    tasks["teste-ml-21-splitdata"] >> tasks["teste-ml-21-trainforecasting"]

    tasks["teste-ml-8-optimize"] >> tasks["teste-ml-8-fitmodel"]

    tasks["teste-dm-24-addfeatures"] >> tasks["teste-ml-24-splitdata"]

    tasks["teste-ml-38-fitmodel"] >> tasks["teste-ml-38-predict"]

    tasks["teste-ml-14-optimize"] >> tasks["teste-ml-14-fitmodel"]

    tasks["teste-dm-38-preprocessdata"] >> tasks["teste-dm-38-clean-energy"]

    tasks["teste-dm-14-addfeatures"] >> tasks["teste-ml-14-splitdata"]

    tasks["teste-ml-32-trainforecasting"] >> tasks["teste-ml-32-optimize"]

    tasks["teste-ml-32-trainforecasting"] >> tasks["teste-ml-32-fitmodel"]

    tasks["teste-dm-45-preprocessdata"] >> tasks["teste-dm-45-clean-energy"]

    tasks["teste-dm-25-addfeatures"] >> tasks["teste-ml-25-splitdata"]

    tasks["teste-ml-5-predict"] >> tasks["teste-ml-5-writedata"]

    tasks["teste-ml-33-predict"] >> tasks["teste-ml-33-writedata"]

    tasks["teste-dm-15-removeless24"] >> tasks["teste-dm-15-addfeatures"]

    tasks["teste-dm-9-preprocessdata"] >> tasks["teste-dm-9-clean-energy"]

    tasks["teste-dm-28-clean-energy"] >> tasks["teste-dm-28-removeless24"]

    tasks["teste-ml-29-splitdata"] >> tasks["teste-ml-29-predict"]

    tasks["teste-ml-29-splitdata"] >> tasks["teste-ml-29-optimize"]

    tasks["teste-ml-29-splitdata"] >> tasks["teste-ml-29-trainforecasting"]

    tasks["teste-ml-29-fitmodel"] >> tasks["teste-ml-29-predict"]

    tasks["teste-dm-37-addfeatures"] >> tasks["teste-ml-37-splitdata"]

    tasks["teste-ml-30-predict"] >> tasks["teste-ml-30-writedata"]

    tasks["teste-dm-6-removeless24"] >> tasks["teste-dm-6-addfeatures"]

    tasks["teste-ml-3-fitmodel"] >> tasks["teste-ml-3-predict"]

    tasks["teste-ml-12-trainforecasting"] >> tasks["teste-ml-12-fitmodel"]

    tasks["teste-ml-12-trainforecasting"] >> tasks["teste-ml-12-optimize"]

    tasks["teste-ml-12-optimize"] >> tasks["teste-ml-12-fitmodel"]

    tasks["teste-ml-20-fitmodel"] >> tasks["teste-ml-20-predict"]

    tasks["teste-dm-34-preprocessdata"] >> tasks["teste-dm-34-clean-energy"]

    tasks["teste-dm-8-clean-energy"] >> tasks["teste-dm-8-removeless24"]

    tasks["teste-ml-46-optimize"] >> tasks["teste-ml-46-fitmodel"]

    tasks["teste-dm-17-addfeatures"] >> tasks["teste-ml-17-splitdata"]

    tasks["teste-ml-14-fitmodel"] >> tasks["teste-ml-14-predict"]

    tasks["teste-dm-5-removeless24"] >> tasks["teste-dm-5-addfeatures"]

    tasks["teste-dm-2-clean-energy"] >> tasks["teste-dm-2-removeless24"]

    tasks["teste-ml-34-trainforecasting"] >> tasks["teste-ml-34-fitmodel"]

    tasks["teste-ml-34-trainforecasting"] >> tasks["teste-ml-34-optimize"]

    tasks["teste-ml-34-optimize"] >> tasks["teste-ml-34-fitmodel"]

    tasks["teste-dm-11-clean-energy"] >> tasks["teste-dm-11-removeless24"]

    tasks["teste-ml-38-predict"] >> tasks["teste-ml-38-writedata"]

    tasks["teste-ml-11-fitmodel"] >> tasks["teste-ml-11-predict"]

    tasks["teste-dm-0-preprocessdata"] >> tasks["teste-dm-0-clean-energy"]

    tasks["teste-dm-23-addfeatures"] >> tasks["teste-ml-23-splitdata"]

    tasks["teste-da-20-downfiles"] >> tasks["teste-dm-20-preprocessdata"]

    tasks["teste-da-20-downfiles"] >> tasks["teste-ml-20-writedata"]

    tasks["teste-ml-3-optimize"] >> tasks["teste-ml-3-fitmodel"]

    tasks["teste-ml-34-predict"] >> tasks["teste-ml-34-writedata"]

    tasks["teste-dm-1-clean-energy"] >> tasks["teste-dm-1-removeless24"]

    tasks["teste-dm-47-addfeatures"] >> tasks["teste-ml-47-splitdata"]

    tasks["teste-dm-6-addfeatures"] >> tasks["teste-ml-6-splitdata"]

    tasks["teste-dm-15-addfeatures"] >> tasks["teste-ml-15-splitdata"]

    tasks["teste-dm-0-removeless24"] >> tasks["teste-dm-0-addfeatures"]

    tasks["teste-ml-32-optimize"] >> tasks["teste-ml-32-fitmodel"]

    tasks["teste-ml-44-optimize"] >> tasks["teste-ml-44-fitmodel"]

    tasks["teste-ml-27-predict"] >> tasks["teste-ml-27-writedata"]

    tasks["teste-dm-35-addfeatures"] >> tasks["teste-ml-35-splitdata"]

    tasks["teste-dm-34-clean-energy"] >> tasks["teste-dm-34-removeless24"]

    tasks["teste-dm-4-addfeatures"] >> tasks["teste-ml-4-splitdata"]

    tasks["teste-dm-39-addfeatures"] >> tasks["teste-ml-39-splitdata"]

    tasks["teste-ml-19-fitmodel"] >> tasks["teste-ml-19-predict"]

    tasks["teste-dm-41-addfeatures"] >> tasks["teste-ml-41-splitdata"]

    tasks["teste-ml-31-optimize"] >> tasks["teste-ml-31-fitmodel"]

    tasks["teste-dm-44-clean-energy"] >> tasks["teste-dm-44-removeless24"]

    tasks["teste-ml-4-fitmodel"] >> tasks["teste-ml-4-predict"]

    tasks["teste-ml-46-fitmodel"] >> tasks["teste-ml-46-predict"]

    tasks["teste-ml-21-fitmodel"] >> tasks["teste-ml-21-predict"]

    tasks["teste-dm-30-removeless24"] >> tasks["teste-dm-30-addfeatures"]

    tasks["teste-da-24-downfiles"] >> tasks["teste-ml-24-writedata"]

    tasks["teste-da-24-downfiles"] >> tasks["teste-dm-24-preprocessdata"]

    tasks["teste-ml-24-predict"] >> tasks["teste-ml-24-writedata"]

    tasks["teste-dm-27-addfeatures"] >> tasks["teste-ml-27-splitdata"]

    tasks["teste-dm-14-preprocessdata"] >> tasks["teste-dm-14-clean-energy"]

    tasks["teste-ml-41-optimize"] >> tasks["teste-ml-41-fitmodel"]

    tasks["teste-dm-46-preprocessdata"] >> tasks["teste-dm-46-clean-energy"]

    tasks["teste-da-19-downfiles"] >> tasks["teste-ml-19-writedata"]

    tasks["teste-da-19-downfiles"] >> tasks["teste-dm-19-preprocessdata"]

    tasks["teste-ml-19-predict"] >> tasks["teste-ml-19-writedata"]

    tasks["teste-dm-27-clean-energy"] >> tasks["teste-dm-27-removeless24"]

    tasks["teste-dm-49-preprocessdata"] >> tasks["teste-dm-49-clean-energy"]

    tasks["teste-ml-18-trainforecasting"] >> tasks["teste-ml-18-optimize"]

    tasks["teste-ml-18-trainforecasting"] >> tasks["teste-ml-18-fitmodel"]

    tasks["teste-ml-31-fitmodel"] >> tasks["teste-ml-31-predict"]

    tasks["teste-ml-36-predict"] >> tasks["teste-ml-36-writedata"]

    tasks["teste-dm-14-clean-energy"] >> tasks["teste-dm-14-removeless24"]

    tasks["teste-dm-7-removeless24"] >> tasks["teste-dm-7-addfeatures"]

    tasks["teste-ml-15-predict"] >> tasks["teste-ml-15-writedata"]

    tasks["teste-dm-20-clean-energy"] >> tasks["teste-dm-20-removeless24"]

    tasks["teste-dm-15-clean-energy"] >> tasks["teste-dm-15-removeless24"]

    tasks["teste-ml-45-predict"] >> tasks["teste-ml-45-writedata"]

    tasks["teste-ml-25-predict"] >> tasks["teste-ml-25-writedata"]

    tasks["teste-dm-29-preprocessdata"] >> tasks["teste-dm-29-clean-energy"]

    tasks["teste-dm-30-preprocessdata"] >> tasks["teste-dm-30-clean-energy"]

    tasks["teste-ml-34-fitmodel"] >> tasks["teste-ml-34-predict"]

    tasks["teste-ml-34-splitdata"] >> tasks["teste-ml-34-predict"]

    tasks["teste-ml-34-splitdata"] >> tasks["teste-ml-34-trainforecasting"]

    tasks["teste-ml-34-splitdata"] >> tasks["teste-ml-34-optimize"]

    tasks["teste-dm-38-addfeatures"] >> tasks["teste-ml-38-splitdata"]

    tasks["teste-ml-28-predict"] >> tasks["teste-ml-28-writedata"]

    tasks["teste-dm-49-clean-energy"] >> tasks["teste-dm-49-removeless24"]

    tasks["teste-dm-48-preprocessdata"] >> tasks["teste-dm-48-clean-energy"]

    tasks["teste-dm-24-removeless24"] >> tasks["teste-dm-24-addfeatures"]

    tasks["teste-ml-18-optimize"] >> tasks["teste-ml-18-fitmodel"]

    tasks["teste-ml-2-optimize"] >> tasks["teste-ml-2-fitmodel"]

    tasks["teste-ml-2-trainforecasting"] >> tasks["teste-ml-2-fitmodel"]

    tasks["teste-ml-2-trainforecasting"] >> tasks["teste-ml-2-optimize"]

    tasks["teste-dm-19-preprocessdata"] >> tasks["teste-dm-19-clean-energy"]

    tasks["teste-dm-11-removeless24"] >> tasks["teste-dm-11-addfeatures"]

    tasks["teste-da-12-downfiles"] >> tasks["teste-ml-12-writedata"]

    tasks["teste-da-12-downfiles"] >> tasks["teste-dm-12-preprocessdata"]

    tasks["teste-ml-12-predict"] >> tasks["teste-ml-12-writedata"]

    tasks["teste-ml-20-predict"] >> tasks["teste-ml-20-writedata"]

    tasks["teste-dm-28-preprocessdata"] >> tasks["teste-dm-28-clean-energy"]

    tasks["teste-ml-6-fitmodel"] >> tasks["teste-ml-6-predict"]

    tasks["teste-dm-31-clean-energy"] >> tasks["teste-dm-31-removeless24"]

    tasks["teste-dm-43-clean-energy"] >> tasks["teste-dm-43-removeless24"]

    tasks["teste-dm-32-removeless24"] >> tasks["teste-dm-32-addfeatures"]

    tasks["teste-ml-15-optimize"] >> tasks["teste-ml-15-fitmodel"]

    tasks["teste-dm-9-removeless24"] >> tasks["teste-dm-9-addfeatures"]

    tasks["teste-dm-7-preprocessdata"] >> tasks["teste-dm-7-clean-energy"]

    tasks["teste-dm-20-preprocessdata"] >> tasks["teste-dm-20-clean-energy"]

    tasks["teste-dm-26-clean-energy"] >> tasks["teste-dm-26-removeless24"]

    tasks["teste-dm-37-preprocessdata"] >> tasks["teste-dm-37-clean-energy"]

    tasks["teste-ml-28-fitmodel"] >> tasks["teste-ml-28-predict"]

    tasks["teste-ml-7-predict"] >> tasks["teste-ml-7-writedata"]

    tasks["teste-dm-16-clean-energy"] >> tasks["teste-dm-16-removeless24"]

    tasks["teste-ml-21-predict"] >> tasks["teste-ml-21-writedata"]

    tasks["teste-ml-35-fitmodel"] >> tasks["teste-ml-35-predict"]

    tasks["teste-ml-37-optimize"] >> tasks["teste-ml-37-fitmodel"]

    tasks["teste-dm-34-removeless24"] >> tasks["teste-dm-34-addfeatures"]

    tasks["teste-dm-33-addfeatures"] >> tasks["teste-ml-33-splitdata"]

    tasks["teste-ml-22-predict"] >> tasks["teste-ml-22-writedata"]

    tasks["teste-dm-48-addfeatures"] >> tasks["teste-ml-48-splitdata"]

    tasks["teste-ml-25-fitmodel"] >> tasks["teste-ml-25-predict"]

    tasks["teste-dm-18-clean-energy"] >> tasks["teste-dm-18-removeless24"]

    tasks["teste-dm-48-removeless24"] >> tasks["teste-dm-48-addfeatures"]

    tasks["teste-ml-43-optimize"] >> tasks["teste-ml-43-fitmodel"]

    tasks["teste-dm-40-clean-energy"] >> tasks["teste-dm-40-removeless24"]

    tasks["teste-dm-47-clean-energy"] >> tasks["teste-dm-47-removeless24"]