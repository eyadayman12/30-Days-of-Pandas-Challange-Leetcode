def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    department.rename(columns = {'id' : 'departmentId'}, inplace=True)
    new_df = pd.merge(employee, department, on="departmentId", suffixes=('_employee', '_department'))

    result_df = pd.DataFrame({
    'Department' : [],
    'Employee' : [],
    "Salary" : []
    })

    for i in new_df['departmentId'].unique():
    
        temp = new_df[new_df['departmentId'] == i]
        temp = temp[temp['salary'] == temp['salary'].max()][['name_department', 'name_employee', 'salary']]
        temp.rename(columns={'name_department' : 'Department', 'name_employee' : 'Employee', 'salary' : 'Salary'}, inplace=True)
        
        result_df = pd.concat([result_df, temp])

    return result_df