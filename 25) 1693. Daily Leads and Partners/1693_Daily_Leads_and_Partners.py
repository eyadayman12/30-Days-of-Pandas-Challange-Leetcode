import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:

    df = daily_sales.drop('partner_id', axis=1).drop_duplicates()
    result_df = df.groupby(['date_id', 'make_name'])['lead_id'].agg('count').reset_index().rename(columns={'lead_id' : 'unique_leads'})

    df = daily_sales.drop('lead_id', axis=1).drop_duplicates()
    unique_partners = df.groupby(['date_id', 'make_name'])['partner_id'].agg('count').values

    result_df['unique_partners'] = unique_partners

    return result_df