import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    non_bonus_emp = employees[(employees['employee_id'] % 2 == 0) | (employees['name'].str.startswith('M'))][['employee_id', 'salary']]

    non_bonus_emp['salary'] = 0

    results_df = employees.merge(non_bonus_emp[['employee_id', 'salary']], on="employee_id", how="left", suffixes=('_original', '_new'))

    results_df['salary_new'] = results_df['salary_new'].fillna(results_df['salary_original'])

    results_df.drop(['name', 'salary_original'], axis=1, inplace=True)
    results_df.rename(columns={'salary_new' : 'bonus'}, inplace=True)
    results_df.sort_values(by='employee_id', inplace=True)
    #results_df['bonus'] = results_df['bonus'].astype('int32')

    return results_df