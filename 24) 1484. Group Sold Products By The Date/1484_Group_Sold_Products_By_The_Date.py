import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    df = activities.drop_duplicates(subset=['sell_date', 'product']).groupby(['sell_date'])['product'].agg('count').reset_index().rename(columns={'product':'num_sold'})

    df2 = activities.groupby(['sell_date', 'product']).agg('count').reset_index()

    l = []
    empty = ''
    c = 0

    for i in df['num_sold']:
        print(type(i))
        for j in range(i):
            
            if empty == '':
                empty += df2['product'][c]
            else:
                empty = empty + ',' + df2['product'][c]
            
            c+=1

        l.append(empty)
        empty = ''

    df['products'] = l

    return df