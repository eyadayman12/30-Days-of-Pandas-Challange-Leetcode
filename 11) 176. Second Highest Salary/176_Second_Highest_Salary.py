import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    df = employee.drop_duplicates(subset=['salary']).sort_values(by='salary', ascending=False)

    if len(df) < 2:
        return pd.DataFrame({'SecondHighestSalary' : [None]})
    
    return pd.DataFrame({'SecondHighestSalary' : [df['salary'].iloc[1]]})