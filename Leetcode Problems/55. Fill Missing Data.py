# https://leetcode.com/problems/fill-missing-data/
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"]= products["quantity"].fillna(0)
    return products
