from airflow.providers.discord.operators.discord_webhook import DiscordWebhookOperator

#https://discord.com/api/webhooks/1119305946166988951/6htQBg_8sicD337CjLvqn93DOQsbQAsJYd4WmWMGlaZwYSPWDmWat4SMzjuW1CsSVl35 
def send_discord_fail_notification(context):
    discord_webhook_task = DiscordWebhookOperator(
        task_id='discord_notification',
        #http_conn_id= 'airflow_teste',
        webhook_endpoint="webhooks/1119305946166988951/6htQBg_8sicD337CjLvqn93DOQsbQAsJYd4WmWMGlaZwYSPWDmWat4SMzjuW1CsSVl35",
        message=f":fox::x: Airflow Task '{context['task_instance'].task_id}' from DAG '{context['task_instance'].dag_id}' failed!",
        username='Fox_airflow_bot' 
    )
    discord_webhook_task.execute(context=context)

def send_discord_retry_notification(context):
    discord_webhook_task = DiscordWebhookOperator(
        task_id='discord_notification',
        #http_conn_id= 'airflow_teste',
        webhook_endpoint="webhooks/1119305946166988951/6htQBg_8sicD337CjLvqn93DOQsbQAsJYd4WmWMGlaZwYSPWDmWat4SMzjuW1CsSVl35",
        message=f":fox::warning: Airflow Task '{context['task_instance'].task_id}' from DAG '{context['task_instance'].dag_id}' up to retry!",
        username='Fox_airflow_bot'
    )
    discord_webhook_task.execute(context=context)

def send_discord_success_notification(context):
    discord_webhook_task = DiscordWebhookOperator(
        task_id='discord_notification',
        #http_conn_id= 'airflow_teste',
        webhook_endpoint="webhooks/1119305946166988951/6htQBg_8sicD337CjLvqn93DOQsbQAsJYd4WmWMGlaZwYSPWDmWat4SMzjuW1CsSVl35",
        message=f":fox::white_check_mark: Airflow Task '{context['task_instance'].task_id}' from DAG '{context['task_instance'].dag_id}' executed with no errors!",
        username='Fox_airflow_bot'
    )
    discord_webhook_task.execute(context=context)   