import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how='cross')
    attended_exams = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='nombre_d_examens')
    result_df = df.merge(attended_exams, on=['student_id', 'subject_name'], how='left')
    result_df['attended_exams'] = result_df['nombre_d_examens'].fillna(0)
    result_df = result_df.sort_values(['student_id', 'subject_name'])
    return result_df[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    return result_df