import pandas as p
import matplotlib.pyplot as m

data = p.read_csv(r'C:\Users\abc\Desktop\Exel\Date_andCity.csv')
group = data.groupby('City')
print(group)

# To access seperately...
for city,city_df in group:
    print(city)
    print(city_df) 

# To access specificly...
print(group.get_group('London'))
#We can find sum,diff,mean,median,mode etc...
print(group.max())

#To find all the sum,diff,mean,median,mode etc...
print(group.describe())

#To find graph
g = group.plot()
m.show()