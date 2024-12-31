import pandas as pd
import numpy as np
# Tạo DataFrame có chứa giá trị null
data = {'A': [1, 2, np.nan, 4],
 'B': [np.nan, 6, 7, 8],
 'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)
# Kiểm tra giá trị null trong DataFrame
print(df.isnull())
print(df.notnull())