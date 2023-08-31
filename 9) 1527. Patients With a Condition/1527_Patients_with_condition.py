import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    pattern1 = '^DIAB1'
    df1 = patients[patients['conditions'].str.match(pattern1)]
    pattern2 = '^[a-zA-Z0-9\s]*\s+DIAB1'
    df2 = patients[patients['conditions'].str.match(pattern2)]
    df = pd.concat([df1,df2])
    
    return df