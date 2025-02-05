import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    gb= employee.groupby(['managerId']).size().reset_index(name='count')
    gb.rename(columns={'managerId': 'id'}, inplace=True)
    return pd.merge(gb[gb["count"]>=5][['id']],employee,how='inner',on='id')[["name"]]