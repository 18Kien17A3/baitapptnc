import pandas as pd
#Ghép 2 DataFrame
A=pd.DataFrame([['A0','B0'],['A1','B1']],columns=['A','B'])
B=pd.DataFrame([['A2','B2'],['A3','B3']],columns=['A','B'])
print(A,'\n')
print(B)
print("\nNối A và B theo hàng: \n", pd.concat([A,B]))
print("\nNối A và B theo cột:\n", pd.concat([A,B], axis = 1))