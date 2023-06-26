FROM apache/airflow:2.5.3-python3.10

# Add a new user with sudo privileges
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         libgomp1 \
  && apt install libsystemd-dev -y \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
  
USER airflow

COPY ./dist/forecast-0.1-py3-none-any.whl /tmp/forecast-0.1-py3-none-any.whl
#COPY ./src/requirements.txt /tmp/requirements.txt

#RUN pip install --upgrade pip setuptools && pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --user /tmp/forecast-0.1-py3-none-any.whl

RUN pip install --user apache-airflow-providers-discord