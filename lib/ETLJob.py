import sqlite3
import pandas as pd
import toml


"""
Load toml as config
"""
config = toml.load("../config/ETLJobConfig.toml")

"""
Function for reading a specific table from a database
"""
def read_table_df(table):
    db_connection = sqlite3.connect(config["folder"]["db"] + config["database"]["xyz"])
    table_data = pd.read_sql_query(f"select * from {table}", db_connection)
    return table_data

if __name__ == "__main__":
    """
    Load each table into a DataFrame
    """
    sales_df = read_table_df(config["table"]["sales"])
    orders_df = read_table_df(config["table"]["orders"])
    customers_df = read_table_df(config["table"]["customers"])
    items_df = read_table_df(config["table"]["items"])

    """
    Merge the DataFrames
    """
    sales_orders_df = sales_df.merge(orders_df, on= 'sales_id')
    sales_orders_items_df = sales_orders_df.merge(items_df, on = 'item_id')
    all_df = sales_orders_items_df.merge(customers_df, on = 'customer_id')

    """
    Filter & transform rows
    """
    age_filtered_df = all_df[(all_df["age"] >= 18) & (all_df["age"] <= 35)]
    non_empty_quantity_df = age_filtered_df.loc[all_df['quantity'].notnull()].astype({"quantity": int}).sort_values("customer_id", ascending=True)

    """
    Write the final DataFrame into CSV
    """
    non_empty_quantity_df.groupby(["customer_id", "age", "item_name"]).sum().reset_index().to_csv(config["folder"]["reports"] + "sales_report.csv", ";", columns = config["column"]["order"], index = False)
