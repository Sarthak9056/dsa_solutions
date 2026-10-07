# LeetCode #2885 - Rename Columns (Easy)
# Pattern: .rename(columns={'id':'student_id', ...})
# Time: O(n), Space: O(n)

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'})
    return students
