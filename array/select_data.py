# LeetCode #2880 - Select Data (Easy)
# Pattern: boolean mask + .loc[row_condition, ['name','age']]
# Time: O(n), Space: O(1)

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    output = students[students['student_id'] == 101]
    return(output.drop(columns=['student_id']))
