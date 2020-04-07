import pandas as pd
from prefect import task


@task
def load_country_data(country_data_location):
    country_data = pd.read_csv(country_data_location)
    country_data["population"] = country_data["population"].astype("int64")
    country_data["country"] = country_data["country"].astype("str")
    return country_data
