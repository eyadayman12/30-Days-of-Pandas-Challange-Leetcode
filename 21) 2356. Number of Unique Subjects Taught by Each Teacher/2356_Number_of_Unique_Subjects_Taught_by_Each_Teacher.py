import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    return teacher.drop_duplicates(subset=['subject_id', 'teacher_id']).groupby('teacher_id')['subject_id'].agg('count').reset_index().rename(columns={'subject_id' : 'cnt'})