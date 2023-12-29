import pandas as p

data = p.read_csv(r'C:\Users\abc\Desktop\Exel\archive\archive (1)\FaceBook-Meta.csv' , parse_dates=['Date'] , index_col='Date')
#Shifting...
data_1 = data['Previous Day Open'] = data['Open'].shift(1) # shift() function is used to shift value to the next (or) prev field...
data_2 = data['Previous Day Open'] = data['Open'].shift(-1)
print(data_1.head(5),data_2.head(5))

#Small experiment...
datas = data['1 Day changes'] = data['Open'] - data['Previous Day Open']
print(datas.head(20))

d = data['5 Days Percentage'] = (data['Open'] - data['Open'].shift(5))*100/data['Open'].shift(5)
print(d.head(20))