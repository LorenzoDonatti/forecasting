FROM apache/airflow:2.5.3-python3.10

#COPY ./src/requirements.txt /tmp/requirements.txt

#RUN pip install --upgrade pip setuptools && pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./dist/forecast-0.1-py3-none-any.whl /tmp/forecast-0.1-py3-none-any.whl

RUN pip install --user /tmp/forecast-0.1-py3-none-any.whl