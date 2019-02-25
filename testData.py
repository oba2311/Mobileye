import pandas as pd

data = pd.read_csv('./sensor (2).txt', sep=" ", header=None)
# data.columns = ['ID','Country',	'Illumination',	'road_type','severity',	'Driver_name']

print(data.head())

