
import pandas as p

data = p.read_csv(r'C:\Users\abc\Desktop\Exel\AppleHistoricalData.csv',index_col=0)

#To generate a date range...
range = p.date_range(start='21/11/2023',end='18/12/2023',freq='B')# Here the 'B' is represents the bussiness which mean Mon-Fri...
data.set_index(range,inplace=True)
print(data)

#To print some days values...

data_1 = data.sort_index().loc['2023-11-11':'2023-12-01'].plot()
print(data_1)

#To generate the stock of the saturday and sunday...

datas = data.asfreq('D',method='pad')# Convert time series to specified frequency based on the condition ex:'D'

print(datas)