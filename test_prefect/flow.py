from dagster import pipeline
from prefect import Parameter, Flow

from test_prefect.consts import DATA_PATH
from test_prefect.tasks.add_country_information import add_country_information
from test_prefect.tasks.get_statistical_data import get_statistical_data
from test_prefect.tasks.filter_date import filter_date
from test_prefect.tasks.filter_df import filter_df
from test_prefect.tasks.load_country_data import load_country_data
from test_prefect.tasks.load_patient_data import load_patient_data


def get_flow():
    with Flow("get_patient_graph") as flow:
        patient_data = load_patient_data(Parameter("patient_data_location",
                                                   default=DATA_PATH.joinpath("patient_data.csv")))
        patient_data = filter_df(patient_data, Parameter("filtered_column"), Parameter("value_to_filter_by"))
        patient_data = filter_date(patient_data, Parameter("start_date"))
        statistical_patient_date = get_statistical_data(patient_data)
        country_data_location = load_country_data(Parameter("country_data_location",
                                                            default=DATA_PATH.joinpath("country_data.csv")))
        add_country_information(statistical_patient_date, country_data_location)
    return flow
