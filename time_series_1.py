import pandas as p


data = p.read_csv(r'C:\Users\abc\Desktop\Exel\HistoricalData.csv' , parse_dates=['Date'],index_col='Date')#parse_dates: Convert Columns into Datetime When Using pandas to Read CSV Files.

                                                                #DateTime Indexing...   

#To print specifc months stock...

data_1 = data["2023-12"].Close.median()#CLose is attribute which is avaliable in the csv file and we can perform all statistical operation such as mean,meidan,mode
print(data_1)

#we can print specific days stocks also...
data_2 = data.loc["2023-12-11"]
print(data_2)

#we can also set range for date...
datas = data.sort_index().loc["2023-10-10" : "2023-12-11"] # sort_index is used to sort the columns .... first low month date and second high month ate
print(datas)


                                                                #Resampling...

#I need to print data monthly wise...
info = data.High.resample('M').mean()# First select a column and use resample function and we can use mean,medin,mode also
print(info)

#We can also represent a graph with or without using matplotlib...

info_1 = data.Low.resample('W').mean().plot()
print(info_1)

#We can also represent a graph in a Bar diagram...

infos = data.Volume.resample('Q').mean().plot(kind='bar')
print(infos)
