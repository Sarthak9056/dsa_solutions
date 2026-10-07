# LeetCode #2878 - Get the Size of a DataFrame (Easy)
# Pattern: df.shape -> return [rows, cols]
# Time: O(1), Space: O(1)

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
