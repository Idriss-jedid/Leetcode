import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    group1=teacher.groupby(["teacher_id","subject_id"])[["dept_id"]].count().reset_index()
    group2=group1.groupby(["teacher_id"])[["dept_id"]].count().reset_index()
    group2.rename(columns={"dept_id":"cnt"},inplace=True)
    return group2