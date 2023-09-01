import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    try:
        red_id = company['com_id'][company['name'] == 'RED'].values[0]
    except:
        return sales_person['name'].to_frame('name')
    
    sales = orders[orders['com_id'] == red_id]['sales_id'].to_list()

    return sales_person['name'][~sales_person['sales_id'].isin(sales)].to_frame('name')