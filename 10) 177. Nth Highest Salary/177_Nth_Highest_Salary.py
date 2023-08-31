import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    df = employee.sort_values(by='salary', ascending=False).drop_duplicates(subset=['salary'])

    if N > len(df):
       return pd.DataFrame({f'getNthHighestSalary({N})' : []})

    return pd.DataFrame({f'getNthHighestSalary({N})' : [df['salary'].iloc[N-1]]})