import pandas as pd
population = pd.Series({'TP.Hồ Chí Minh':9411805,
'Hà Nội':8330830,
'Thanh Hóa':3720000,
'Nghệ An':3410000,
'Đồng Nai':3097107})
#Số liệu về top 5 diện tích tỉnh/thành Việt Nam
area=pd.Series({'Nghệ An':16493,
'Gia Lai':15536.9,
'Sơn La':14174.4,
'Đăk Lăk':13030.5,
'Thanh Hóa':11132.2})
print("Top 5 tỉnh/tp đông dân nhất Việt Nam 2023:\n",population)
print("Top 5 tỉnh/tp diện tích lớn nhất Việt Nam 2023:\n",area)