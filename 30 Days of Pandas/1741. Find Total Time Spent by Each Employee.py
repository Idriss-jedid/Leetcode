import pandas as pd
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    gpemployees = employees.groupby(['event_day','emp_id'])[['in_time','out_time']].sum().reset_index()
    gpemployees['total_time'] = gpemployees['out_time'] - gpemployees['in_time']
    gpemployees.rename(columns={'event_day': 'day'}, inplace=True)
    gpemployees = gpemployees[['day','emp_id','total_time']]
    return gpemployees