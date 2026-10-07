# LeetCode #2884 - Modify Columns (Easy)
# Pattern: df['salary'] = df['salary'] * 2  # vectorised
# Time: O(n), Space: O(1)

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees
