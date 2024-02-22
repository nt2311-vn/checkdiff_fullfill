import pandas as pd
from pandas.compat import sys


def calculate_differences():
    fulfill_data = pd.read_csv("./data/IF.csv")
    workorder_data = pd.read_csv("./data/WO.csv")

    result_table = {}
    reconcile_table = {}

    set_unique_item = set(fulfill_data["Item"]).union(set(workorder_data["Item"]))
    set_unique_date = sorted(
        set(fulfill_data["Date"]).union(set(workorder_data["Date"]))
    )

    print(
        f"There are total number of {len(set_unique_item)} item code, across {len(set_unique_date)} days to check"
    )

    for index, date in enumerate(set_unique_date, start=1):
        for item in set_unique_item:
            fulfill_qty = fulfill_data[
                (fulfill_data["Item"] == item) & (fulfill_data["Date"] == date)
            ]["Quantity"].sum()

            order_qty = workorder_data[
                (workorder_data["Item"] == item) & (workorder_data["Date"] == date)
            ]["Quantity"].sum()

            net_qty = fulfill_qty - order_qty

            if date not in reconcile_table:
                reconcile_table[date] = {}

            reconcile_table[date][item] = net_qty

            if net_qty != 0:
                if date not in result_table:
                    result_table[date] = {}
                result_table[date][item] = net_qty

        progress_percent = index / len(set_unique_date)
        bar_length = 60
        block = int(round(bar_length * progress_percent))
        text = "\rProgress:[{0}] {1:.2f}%".format(
            "#" * block + "-" * (bar_length - block), progress_percent * 100
        )
        sys.stdout.write(text)
        sys.stdout.flush()

    print()

    return (reconcile_table, result_table)
