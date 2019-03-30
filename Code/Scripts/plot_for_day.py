from Code.Scripts.popularity_calculator import calculate_popularity,freq_of_popularity
import xlrd
import matplotlib.pyplot as plt
import pandas as pd


file_name = 'D:\\Users\\yashk\\Campaign-Assistant\\Data\\Annotated\\graph_day_input.xls'
data = pd.read_excel(file_name)
# print(data.head())
# print(data['day'].value_counts())
# or data['day']=='28'  or data['day']=='2'
data27 = data.loc[data['day']==27]
data28 = data.loc[data['day']==28]
data1 = data.loc[data['day']==1]
data2 = data.loc[data['day']==2]

# workbook = xlrd.open_workbook(file_name)
# sheet = workbook.sheet_by_index(0)
# rows = sheet.nrows
# print(rows)
# month = {}
# column: ann-0 month-1 day-2
