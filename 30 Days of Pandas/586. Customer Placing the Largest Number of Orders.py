import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    gb = orders.groupby("customer_number")["order_number"].count().reset_index()    
    return gb[gb["order_number"] == gb["order_number"].max()][["customer_number"]]
    
