import pandas as p

'''
stock = p.DataFrame({
    'Ticker':['Google','WMT','MSFT','RIL','TATA'],
    'EPS':[27.82,4.61,-1,'n.a.',5.60],
    'Revenue':[25,34,21,1,-1],
    'Price':[845,65,64,1023,'n.a.'],
    'People':['Larry Page','Balaji','Bill Gates','Mukesh Ambani','Ratan Tata']
}) 
    
    

whether = p.DataFrame({
    'Date':['1/9/23','2/9/23','3/9/23','4/9/23','5/9/23'],
    'Wind SPeed':[10,23,34,54,45],
    'Temperature':[29,34,101,19,23],
    'Event':['Cloudy','Windy','Hot','Rainy','Sunny']
})


with p.ExcelWriter('Stock_Whether.xlsx') as writer:
    stock.to_excel(writer,sheet_name='Stocks',index=False)
    whether.to_excel(writer,sheet_name='Whether',index=False)
'''
#to find the Missing datas...
'''

event = p.read_csv(r'C:\Users\abc\Desktop\Exel\missing_whether_book1.csv',parse_dates=['Date'])
event.set_index('Date',inplace=True) #inplace is Mandatory
new_event = event.fillna({
    'Temperature' : 0,
    'Wind Speed' : 0,
    'Event' : 'No Event'
})

#In Better Way...
new_event = event.fillna({
    'Temperature' : event['Temperature'].ffill() ,
    'Wind Speed' : event['Wind Speed'].pad(),# pad() is used to copy the previous data...
    'Event' : event['Event'].ffill()
})#'ffill' and 'bfill' means "Forwrd Fill" and "Backwrd Fill"
print(new_event)
new_event = event.interpolate()# interpolate gives some sligt deviated datas...
new_event1 = event.dropna(how='all')# It willl drop all the rows and columns which has na values...
print(new_event)
print(new_event1)
'''

