import numpy as np
import pandas as pd
# Tạo DataFrame có chứa giá trị null
data = {'A': [1, 2, np.nan, 4],
'B': [np.nan, 6, 7, 8],
'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)
# In ra DataFrame trước khi thay thế giá trị NA
print("DataFrame trước khi thay thế:")
print(df)
# Sử dụng fillna() để thay thế giá trị NA bằng 0
df_filled = df.fillna(0)
# In ra DataFrame sau khi thay thế giá trị NA
print("\nDataFrame sau khi thay thế:")
print(df_filled)