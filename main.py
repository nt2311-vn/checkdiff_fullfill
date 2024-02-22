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
        set_unique_date = set(fulfill_data["Date"]).union(set(workorder_data["Date"]))

        for date in set_unique_date:
            fulfill_table[date] = {}

            for item in set_unique_item:
                fulfill_qty = fulfill_data[
                    (fulfill_data["Item"] == item) & (fulfill_data["Date"] == date)
                ]["Quantity"].sum()

                order_qty = workorder_data[
                    (workorder_data["Item"] == item) & (workorder_data["Date"] == date)
                ]["Quantity"].sum()

                net_qty = fulfill_qty - order_qty

                if net_qty != 0:
                    fulfill_table[date][item] = net_qty

        keys = list(fulfill_table.keys())

        for key in keys:
            if fulfill_table[key] == {}:
                del fulfill_table[key]

        print(f"Final result of table: {fulfill_table}")

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")


if __name__ == "__main__":
    main()
