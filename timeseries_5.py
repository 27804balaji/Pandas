import pandas as p
import pytz #This module is used to perform timezone operations etc...
from datetime import datetime

data = p.read_csv(r'C:\Users\abc\Desktop\Exel\archive\Microsoft.csv' , index_col='Date',parse_dates= True)# parse_dates is used to convert the series into a datetime...
data.head(5)
#print(data.index)

# To declare the timezone
data = data.tz_localize(tz= 'America/New_York')
print(data.index)

#To convert the time zone into belrin timezone...
data = data.tz_convert(tz='Europe/Berlin')
print(data.head(5))

