# https://leetcode.com/problems/drop-missing-data/
import pandas as pd
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    x = students.dropna(subset = ['name'])
    return x
