# LeetCode #2881 - Create a New Column (Easy)
# Pattern: .assign(bonus=df['salary']*2)  # vectorised, no loops
# Time: O(n), Space: O(n)

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees
