import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee['salary'].drop_duplicates()
    employee = employee.sort_values(ascending=False)
    if 2 > len(employee) :
        return pd.DataFrame({'SecondHighestSalary':[None]})
    return pd.DataFrame({'SecondHighestSalary':[employee.iloc[1]]})
    