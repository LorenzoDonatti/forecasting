FROM apache/airflow:2.5.3-python3.10

# Add a new user with sudo privileges
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         libgomp1 \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow

#COPY ./src/requirements.txt /tmp/requirements.txt
#RUN pip install --upgrade pip setuptools && pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./dist/forecast-0.1-py3-none-any.whl /tmp/forecast-0.1-py3-none-any.whl

RUN pip install --user /tmp/forecast-0.1-py3-none-any.whl

COPY ./dags /opt/airflow/dags
COPY ./logs /opt/airflow/logs
COPY ./conf /opt/airflow/conf
COPY ./data /opt/airflow/data

#RUN chmod -R +rw /opt/airflow/dags
#RUN chmod -R +rw /opt/airflow/conf
#RUN chmod -R +rw /opt/airflow/data