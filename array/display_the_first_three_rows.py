# LeetCode #2879 - Display the First Three Rows (Easy)
# Pattern: df.head(3)
# Time: O(1), Space: O(1)

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
