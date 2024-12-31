import numpy as np
import pandas as pd
# Định nghĩa kiểu dữ liệu cho một Structured Array
dtype = [('name', 'U20'), ('age', int), ('height', float)]

data = np.array([('Minh', 22, 165.5),
('Lan', 40, 160.0),
('Linh', 31, 165.0),
('Lương',18,166.5),
('Thanh',50, 170.0)], dtype=dtype)
# Tạo DataFrame từ Structured Array
df = pd.DataFrame(data)
# In ra DataFrame
print(df)
print(data.dtype)