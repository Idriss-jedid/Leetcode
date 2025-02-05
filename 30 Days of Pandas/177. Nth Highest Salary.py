import pandas as pd

def nth_highest_salary(employees: pd.DataFrame, N: int) -> pd.DataFrame:
    employees = employees['salary'].drop_duplicates()
    employees = employees.sort_values(ascending=False)
    column = 'getNthHighestSalary('+str(N)+')'
    if N > len(employees) or N<=0:
        return pd.DataFrame({column:[None]})
    return pd.DataFrame({column:[employees.iloc[N-1]]})