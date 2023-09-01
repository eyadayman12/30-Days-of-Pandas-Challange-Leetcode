import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    product_prices = pd.DataFrame({
        'product_id' : [],
        'store' : [],
        'price' : []
    })

    for i in range(len(products)):

        product_id = products['product_id'][i]
        store1_price = products['store1'][i]
        store2_price = products['store2'][i]
        store3_price = products['store3'][i]

        product_prices.loc[len(product_prices.index)] = [product_id, 'store1', store1_price]
        product_prices.loc[len(product_prices.index)] = [product_id, 'store2', store2_price]
        product_prices.loc[len(product_prices.index)] = [product_id, 'store3', store3_price]

    
    return product_prices.dropna()