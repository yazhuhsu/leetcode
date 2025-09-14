import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salary = employee.groupby(['departmentId'])['salary'].max()

    output = employee.merge(max_salary, left_on=['departmentId', 'salary'], right_on=['departmentId', 'salary'])
    output = output.merge(department, left_on='departmentId', right_on='id')
    output = output.drop(columns=['id_x', 'id_y', 'departmentId'])
    output = output.rename(columns={'name_x': 'Employee', 'salary': 'Salary', 'name_y': 'Department'})

    return output

employee = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
}
department = {
    'id': [1, 2],
    'name': ['IT', 'Sales']
}

answer = pd.DataFrame(data={
    'Department': ['IT', 'Sales', 'IT'],
    'Employee': ['Jim', 'Henry', 'Max'],
    'Salary': [90000, 80000, 90000]
})

output = department_highest_salary(pd.DataFrame(data=employee), pd.DataFrame(data=department))

correctRows = 0
for _, row in output.iterrows():
    for _, ans in answer.iterrows():
        correctColumns = 0
        for column in answer.columns:
            if row[column] == ans[column]:
                correctColumns += 1
        
        if correctColumns == len(answer.columns):
            break
    
    if correctColumns == len(answer.columns):
        correctRows += 1
    
if correctRows == len(answer):
    print(True)
else:
    print(False)