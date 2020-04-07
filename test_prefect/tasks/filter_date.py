import pandas as pd
from prefect import task


@task
def filter_date(patient_data, start_date):
    return patient_data[patient_data["confirmed_date"] >= pd.to_datetime(start_date)]
