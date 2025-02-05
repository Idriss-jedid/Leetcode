import pandas as pd

def department_highest_salary(Employee: pd.DataFrame, Department: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(Employee, Department, left_on='departmentId', right_on='id', how='inner')
    max_salaries = merged.groupby('name_y')['salary'].max().reset_index()
    result = pd.merge(max_salaries, merged, on=['name_y', 'salary'], how='inner')
    result = result[['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    result = result.sort_values('Department')
    return result