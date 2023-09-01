import pandas as pd
import numpy as np

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

   return pd.DataFrame({'immediate_percentage': [round((np.sum(delivery['order_date'] == delivery['customer_pref_delivery_date'])/len(delivery))*100,2)]})