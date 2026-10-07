# LeetCode #2882 - Drop Duplicate Rows (Easy)
# Pattern: .drop_duplicates(subset=['email'], keep='first')
# Time: O(n), Space: O(n)

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset = ['email'])
    return customers
