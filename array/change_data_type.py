# LeetCode #2886 - Change Data Type (Easy)
# Pattern: .astype({'grade': int})
# Time: O(n), Space: O(n)

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype('int')
    return students
