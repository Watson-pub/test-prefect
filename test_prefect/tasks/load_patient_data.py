import pandas as pd
from prefect import task


@task
def load_patient_data(patient_data_location):
    patient_data = pd.read_csv(patient_data_location)
    patient_data["confirmed_date"] = pd.to_datetime(patient_data["confirmed_date"], infer_datetime_format=True)
    patient_data["country"] = patient_data["country"].astype("str")
    return patient_data
