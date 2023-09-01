import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    salaries = [0,0,0]
    salaries[0] = np.sum(accounts['income'] < 20000)
    salaries[1] = np.sum( (accounts['income'] >= 20000) & (accounts['income'] <= 50000))
    salaries[2] = np.sum(accounts['income']>50000)

    return pd.DataFrame({
        'Category' : ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count' : salaries 
    })