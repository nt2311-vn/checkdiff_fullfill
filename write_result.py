import pandas as pd


def write_result(reconcile_data, result_data):
    items = sorted(set.union(*[set(v.keys()) for v in reconcile_data.values()]))

    reconcile_data_df = {
        item: {date: reconcile_data[date].get(item, 0) for date in reconcile_data}
        for item in items
    }

    df_reconcile = pd.DataFrame(reconcile_data_df).T
    df_reconcile.insert(0, "Item", df_reconcile.index)
    df_reconcile.to_csv("./result/result_reconcile.csv", index=False)

    workorder_data = pd.read_csv("./data/WO.csv")
    sorted_workorder = workorder_data.sort_values(by="Date Created", ascending=False)

    to_delete_woid = []

    for date, items in result_data.items():
        for item, diff in items.items():
            if diff < 0:
                match = sorted_workorder[
                    (sorted_workorder["Date"] == date)
                    & (sorted_workorder["Item"] == item)
                    & (sorted_workorder["Quantity"] == abs(diff))
                ].head(1)["Internal ID"]

                to_delete_woid.append(str(match.item()))

    print(f"To delete list: {to_delete_woid}")

    with open("result/result_diff.txt", "w") as file:
        file.write(",".join(to_delete_woid))
