import pandas as p
import numpy as n
data = p.read_csv(r'C:\Users\abc\Desktop\Exel\city_whether.csv')
data = data.set_index('Date')

new_data = data.replace([-999,-888,-777],n.nan)

#instead...
new = data.replace({
    'Temperature':[-999,-888,-777 ],
    'Wind Speed':[-999,-888,-777 ],
    'Event':'0'
},n.nan)

# Another Way
specific = data.replace({
    -999 : n.nan,
    -888 : n.nan,
    -777 : n.nan,
    'No Event':'Sunny'
})

#Regex method...
new = data.replace({
    'Temperature':'[A-Za-z]',
    'Wind Speed':'[A-Za-z]'
    
},'',regex=True)
print(new )
print(new_data)

