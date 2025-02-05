import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    company.rename(columns={'name': 'color'}, inplace=True)
    gb = pd.merge(sales_person, orders, how='inner', on='sales_id')
    gb2 = pd.merge(company, gb, how='inner', on='com_id')
    filtered_sales_person = sales_person[~sales_person["name"].isin(gb2[gb2["color"] == "RED"]["name"])]    
    return filtered_sales_person[["name"]]