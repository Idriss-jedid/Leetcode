import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    bonus_bool = (employees["name"].str.get(0) != 'M') & (employees["employee_id"] % 2 == 1)
    employees["bonus"] = employees["salary"] * bonus_bool.astype(int)
    return employees[["employee_id", "bonus"]].sort_values(["employee_id"],ascending=True)