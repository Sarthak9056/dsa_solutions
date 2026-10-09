# Leetode Problem Number - 2888

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    output = pd.concat([df1,df2], ignore_index= 'True')
    return output
