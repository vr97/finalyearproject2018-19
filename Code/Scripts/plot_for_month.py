from Code.Scripts.popularity_calculator import calculate_popularity,freq_of_popularity
import xlrd
import matplotlib.pyplot as plt

file_name = 'D:\\Users\\yashk\\Campaign-Assistant\\Data\\Annotated\\graph_month_input.xls'
workbook = xlrd.open_workbook(file_name)
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
print(rows)
month = {}
for i in range(1,rows):
    month_value = sheet.cell_value(i,1)
    if month_value not in month.keys():
        month[month_value] = [sheet.cell_value(i,0)]
    else:
        month[month_value].append(sheet.cell_value(i,0))
print(month[1])
print(month[2])
print(month[3])
x_axis = [1,2,3]
month1 = freq_of_popularity(month[1])
month2 = freq_of_popularity(month[2])
month3 = freq_of_popularity(month[3])
y_axis = [calculate_popularity(month1['pos'],month1['nut'],month1['neg'],month1['nut']),
          calculate_popularity(month2['pos'],month2['nut'],month2['neg'],month2['nut']),
          calculate_popularity(month3['pos'],month3['nut'],month3['neg'],month3['nut'])
          ]
print(x_axis)
print(y_axis)
plt.plot(x_axis,[item*100 for item in y_axis])
plt.show()