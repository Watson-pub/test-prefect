from datetime import date

from test_prefect.flow import get_flow


def main():
    flow = get_flow()
    state = flow.run({"start_date": date(2020, 2, 1), "filtered_column": "city", "value_to_filter_by": "Gangseo-gu"})
    return state.result[list(flow.terminal_tasks())[0]].result


if __name__ == "__main__":
    main()
