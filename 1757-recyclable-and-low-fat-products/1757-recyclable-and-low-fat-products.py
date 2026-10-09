import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    findproducts=(products['low_fats']=='Y')& (products['recyclable']=='Y')
    return products.loc[findproducts,['product_id']]

    