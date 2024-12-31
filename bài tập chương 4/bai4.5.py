import pandas as pd
#Tuples đại diện cho tỉnh thành phố - Năm tương ứng
index=[('Hà Nội',2015),('Hà Nội',2020),
 ('Nam Định',2015),('Nam Định',2020),
 ('Thanh Hóa',2015),('Thanh Hóa',2020),
 ('Đà Nẵng',2015),('Đà Nẵng',2020),
 ('Hồ Chí Minh',2015),('Hồ Chí Minh',2020)]
data=[ 7216000, 8246540,
 1850600, 1780330,
 3514200, 3664940,
 1028800, 1169480,
 8146300, 9227600]
vn_pop = pd.Series(data, index=index)
vn_pop