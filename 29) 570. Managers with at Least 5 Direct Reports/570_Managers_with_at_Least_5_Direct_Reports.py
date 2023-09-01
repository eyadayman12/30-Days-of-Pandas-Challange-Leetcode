import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    emp = employee.groupby('managerId').size().reset_index(name='direct_reports')
    emp = emp['managerId'][emp['direct_reports'] >= 5]
    emp = list(emp)
    
    return pd.DataFrame({ 'name' : employee[employee['id'].isin(emp)]['name'].values})