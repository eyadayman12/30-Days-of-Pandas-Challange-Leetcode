import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    df = students.merge(subjects, how='cross')

    count_exams = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('subject_name', 'count')).reset_index()

    result = df.merge(count_exams, on=['student_id', 'subject_name'], how='left')
    result.fillna(0, inplace=True)
    result.sort_values(by=['student_id', 'subject_name'], inplace=True)
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]