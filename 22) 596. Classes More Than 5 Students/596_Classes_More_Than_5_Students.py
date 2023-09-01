import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    df = courses.groupby('class')['student'].agg('count').reset_index()

    return df['class'][df['student'] >= 5].to_frame()