import pandas as pd
import numpy as np
idx_arr=[['a','a','b','b'],[1,2,1,2]]
data=np.random.rand(4,3) #Tạo mảng dữ liệu ngẫu nhiên.
#Tạo đối tượng MultiIndex từ mảng idx_arr
multi_index=pd.MultiIndex.from_arrays(idx_arr,
 names = ['Data1','Data2'])
#Tạo DataFrame df.
df=pd.DataFrame(data,index = multi_index,
 columns=['Value1', 'Value2','Value3'])
df