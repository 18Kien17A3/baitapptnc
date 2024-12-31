import pandas as pd
import numpy as np
index=pd.MultiIndex.from_product([[2020,2021,2022],[1,2,3]],
 names=['Năm','Lần thi'])
columns=pd.MultiIndex.from_product([['Bình','Lan','Vân'],
 ['Toán','Lý','Hóa']],
 names=['Học sinh','Môn học'])
#Tạo dữ liệu mẫu, là mảng kích thước 9x9 với các giá trị ngẫu nhiên từ 5-10
data=np.random.randint(5,10,(9,9))
'''Tạo DataFrame score với dữ liệu ngẫu nhiên từ mảng data kích thước 9x9 trong
đó các chỉ mục hàng và cột được thiết lập'''
score=pd.DataFrame(data,index=index, columns=columns)
score