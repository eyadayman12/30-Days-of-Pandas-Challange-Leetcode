import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    df = orders.groupby('customer_number')['order_number'].agg('count').reset_index()

    return df['customer_number'][df['order_number'] == df['order_number'].max()].to_frame()