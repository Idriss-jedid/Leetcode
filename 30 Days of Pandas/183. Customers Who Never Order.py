import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result_table = customers[~customers["id"].isin(orders["customerId"])][["name"]]
    result_table = result_table.rename(columns={"name": "Customers"})
    return result_table