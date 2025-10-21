import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    data = orders.merge(company, left_on=['com_id'], right_on=['com_id'])
    data = data.drop(columns=['order_id', 'order_date', 'com_id', 'amount', 'city'])

    output = sales_person[~sales_person.sales_id.isin(data.loc[data['name']=='RED', 'sales_id'])]
    output = output.drop(columns=['sales_id', 'salary', 'commission_rate', 'hire_date'])

    return output
    
sales_people = {
    'sales_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'],
    'salary': [100000, 12000, 65000, 25000, 5000],
    'commission_rate': [6, 5, 12, 25, 10],
    'hire_date': ['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007']
}

company = {
    'com_id': [1, 2, 3, 4],
    'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'],    
    'city': ['Boston','New York', 'Boston', 'Austin']
}

orders = {
    'order_id': [1, 2, 3, 4],
    'order_date': ['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014'],
    'com_id': [3, 4, 1, 1],
    'sales_id': [4, 5, 1, 4],
    'amount': [10000, 5000, 50000, 25000]
}

answer = pd.DataFrame(data={
    'name': ['Amy', 'Mark', 'Alex']
})

output=sales_person(pd.DataFrame(data=sales_people), pd.DataFrame(data=company), pd.DataFrame(data=orders))
correctRows = 0
for _, row in output.iterrows():
    for _, ans in answer.iterrows():
        correctColumns = 0
        for column in answer.columns:
            if row[column] == ans[column]:
                correctColumns += 1
        if correctColumns == len(answer.columns):
            correctRows += 1

print(correctRows == len(answer))
