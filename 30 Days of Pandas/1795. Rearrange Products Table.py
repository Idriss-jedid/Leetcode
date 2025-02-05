import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df_melted = products.melt(id_vars=['product_id'], var_name='store', value_name='price')
    df_cleaned = df_melted.dropna()
    return df_cleaned