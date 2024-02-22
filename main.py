import pandas as pd
from verify_files import verify_files


def main():
    try:
        verify_files()

        dataIF = "./data/IF.csv"
        dataWO = "./data/WO.csv"
        fulfill_data = pd.read_csv(dataIF)
        workorder_data = pd.read_csv(dataWO)
        fulfill_table = {}

        list_fulfill_item = list(fulfill_data._series["Item"])
        list_workorder_item = list(workorder_data._series["Item"])
        set_unique_item = set(list_fulfill_item + list_workorder_item)

        print(f"Unique items: {len(set_unique_item)}")

        list_fulfill_date = list(fulfill_data._series["Date"])
        list_workorder_date = list(workorder_data._series["Date"])
        set_unique_date = set(list_fulfill_date + list_workorder_date)

        print(f"Number of unique: {len(set_unique_date)}")

        for date in set_unique_date:
            print(f"Unique date: {date}")

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")


main()
