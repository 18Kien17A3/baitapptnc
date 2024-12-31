import pandas as pd
population_dict = {'Hà Nội':8330830,
 'Quảng Ninh':1358085,
 'Nam Định': 1836270,
 'Đà Nẵng':1195490,
 'TP.Hồ Chí Minh':9411805}
population = pd.Series(population_dict)
population
