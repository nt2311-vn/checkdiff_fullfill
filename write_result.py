import pandas as pd


def write_result(reconcile_data):
    items = sorted(set.union(*[set(v.keys()) for v in reconcile_data.values()]))

    reconcile_data_df = {
        item: {date: reconcile_data[date].get(item, 0) for date in reconcile_data}
        for item in items
    }

    df_reconcile = pd.DataFrame(reconcile_data_df).T
    df_reconcile.insert(0, "Item", df_reconcile.index)
    df_reconcile.to_csv("./result/result_reconcile.csv", index=False)
