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

        set_unique_item = set(fulfill_data["Item"]).union(set(workorder_data["Item"]))
        set_unique_date = set(workorder_data["Date"]).union(set(workorder_data["Date"]))

        for date in set_unique_date:
            fulfill_table[date] = {}

            for item in set_unique_item:
                fulfill_table[date][item] = 0

                fulfill_table[date][item] += (
                    fulfill_data._series["Quantity"].eq(item).eq(date).sum()
                )

                fulfill_table[date][item] -= (
                    workorder_data._series["Quantity"].eq(item).eq(date).sum()
                )

                if fulfill_table[date][item] == 0:
                    del fulfill_table[date][item]

        keys = list(fulfill_table.keys())

        for key in keys:
            if fulfill_table[key] == {}:
                del fulfill_table[key]

        print(f"Final result of table: {fulfill_table}")

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")


main()
