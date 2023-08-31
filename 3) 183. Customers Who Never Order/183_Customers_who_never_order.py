import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    l = orders['customerId'].values
    filtered_customers = []

    for i in range(len(customers)):
        if customers['id'][i] not in l:
            filtered_customers.append(customers['name'][i])

    df = pd.DataFrame({
        'Customers': filtered_customers
    })
    return df