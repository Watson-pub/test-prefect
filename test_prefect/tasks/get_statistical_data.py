from prefect import task


@task
def get_statistical_data(data_df):
    combined_data = data_df[["global_num", "country"]].groupby(["country", data_df["confirmed_date"].dt.date]).count()
    return combined_data.reset_index().rename(columns={"global_num": "new_cases", "confirmed_date": "date"})
