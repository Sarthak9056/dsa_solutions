# LeetCode #2883 - Drop Missing Data (Easy)
# Pattern: .dropna(subset=['name'])
# Time: O(n), Space: O(n)

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset=['name'])
    return students
