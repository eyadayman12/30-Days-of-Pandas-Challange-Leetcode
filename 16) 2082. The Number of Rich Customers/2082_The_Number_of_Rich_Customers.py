import pandas as pd
import numpy as np

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:

    return pd.DataFrame({'rich_count' : [np.sum(store.groupby('customer_id')['amount'].agg('max')>500)]})