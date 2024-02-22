import pandas as pd


def calculate_differences():
    fulfill_data = pd.read_csv("./data/IF.csv")
    workorder_data = pd.read_csv("./data/WO.csv")

    result_table = {}
    reconcile_table = {}

    set_unique_item = set(fulfill_data["Item"]).union(set(workorder_data["Item"]))
    set_unique_date = set(fulfill_data["Date"]).union(set(workorder_data["Date"]))

    for date in set_unique_date:
        reconcile_table[date] = {}

        for item in set_unique_item:
            fulfill_qty = fulfill_data[
                (fulfill_data["Item"] == item) & (fulfill_data["Date"] == date)
            ]["Quantity"].sum()

            order_qty = workorder_data[
                (workorder_data["Item"] == item) & (workorder_data["Date"] == date)
            ]["Quantity"].sum()

            net_qty = fulfill_qty - order_qty

            if net_qty == 0:
                reconcile_table[date][item] = net_qty
            else:
                reconcile_table[date][item] = net_qty
                result_table[date] = {}
                result_table[date][item] = net_qty

    return (reconcile_table, result_table)
