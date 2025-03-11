FROM apache/airflow:2.7.3
COPY requirements.txt /requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow/app"

RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt