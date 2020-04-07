from prefect import task


@task
def add_country_information(statistical_data, country_data):
    return statistical_data.merge(country_data[["country", "population"]], on="country")
