import pandas as p

data = p.read_csv(r'C:\Users\abc\Desktop\Exel\pivot.csv')

#to set rows and columns...

data_1 = data.pivot(index='Date',columns='City')
print(data_1)

#to print a particular column...

data_2 = data.pivot(index='Date',columns='City',values='Temperature')
print(data_2)

#Pivot Table...

import pandas as b

info = b.read_csv(r'C:\Users\abc\Desktop\Exel\pivottable.csv')
info_1 = info.pivot_table(index='Date',columns='City')
info_2 = info.pivot_table(index='Date',columns='City',aggfunc='sum')#aggfunc is sconsist of function like sum , diff etc...

#To set margin in Pivot table...

info_3 = info.pivot_table(index='Date',columns='City',margins=True)#Margin is used to set margins...
print(info)
print(info_1)
print(info_2)
print(info_3)

#Pivot Grouper(Grouper is used to group by the datas based on the condition)...

import pandas as g

tech = g.read_csv(r'C:\Users\abc\Desktop\Exel\pivottable1.csv')
tech['Date'] = g.to_datetime(tech['Date'])# Type Convertion
tech_1 = tech.pivot_table(index=g.Grouper(freq='M',key='Date'),columns='City')
print(tech_1)