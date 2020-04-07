import prefect
from prefect import task


@task
def filter_df(df, filtered_column, value_to_filter_by):
    logger = prefect.context.get("logger")
    column_name = str(filtered_column)
    logger.info(f"filtering the column {column_name}, keeping only entries whose value is {value_to_filter_by}.")
    return df[df[column_name] == value_to_filter_by]
