# LeetCode #2877 - Create a DataFrame from List (Easy)
# Pattern: pd.DataFrame(list) then assign .columns
# Time: O(n), Space: O(n)

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id','age'])
