from Code.Scripts.popularity_calculator import calculate_popularity,freq_of_popularity
import pandas as pd
import copy
import xlwt



file_name = 'D:\\Users\\yashk\\Campaign-Assistant\\Data\\Annotated\\graph_hour_input.xlsx'
data = pd.read_excel(file_name)

day1 = data.loc[data['day']==1]
hours = {}
for i in range(0,24):
    hours[i] = {'neg':0,'pos':0,'nut':0}
# print(hours)
for index, row in day1.iterrows():
    # print(row['ann'])
    if row['ann'] == -1:
        hours[row['hour']]['neg'] += 1
    elif row['ann'] == 0:
        hours[row['hour']]['nut'] += 1
    elif row['ann'] == 1:
        hours[row['hour']]['pos'] += 1
    else:
        pass
print(hours)
pop_hour = copy.deepcopy(hours)
for key,value in hours.items():
    # pos_a=0,nut_a=0,neg_a=0,nut_b=0
    try:
        pop_hour[key] = calculate_popularity(hours[key]['pos'],
                                             hours[key]['nut'],
                                             hours[key]['neg'],
                                             hours[key]['nut'])
    except:
        pop_hour[key] = 0.0
print(pop_hour)

wb = xlwt.Workbook()
sheet = wb.add_sheet('pop')

length = len(pop_hour)
row = 1
sheet.write(0,0,'hour')
sheet.write(0,1,'popularity')
for key,value in pop_hour.items():
    sheet.write(row,0,key)
    value_ = str(float(str(value))*100)
    sheet.write(row,1,value_)
    row+=1

wb.save('D:\\Users\\yashk\\Campaign-Assistant\\Data\\Annotated\\graph_hour_output_March_1.xls')
