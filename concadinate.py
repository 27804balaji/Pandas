import pandas as p

india_whether = p.DataFrame({
    
    'City':['Mumbai','Delhi','Chennai'],
    'Humidity':[10,23,34],
    'Temperature':[29,34,101]
    
})

uk_whether = p.DataFrame({
    
    'City':['London','Cambridge','BenTower'],
    'Humidity':[10,13,14],
    'Temperature':[9,14,10]
    
})

#Ignore index is used to print the continuetion of the index value...
concat = p.concat([india_whether,uk_whether],ignore_index=True) 
key = p.concat([india_whether,uk_whether],keys=['India','United Kindom'])

print(concat)
print(key)

#To apppend columns in our Dataframe...

WindSpeed = p.DataFrame({
    'City':['Mumbai','Chennai','Delhi','BenTower','Cambridge','London'],
    'Wind Speed':[3,6,9,1,2,3]
#To Align different rows from different dataframe...
},index=[0,2,1,5,3,4])

series = p.Series(['Rain','Dry','Humid','Snowy','Slight Rain','Humid'],name='Event')
concat_1 = p.concat([concat,WindSpeed],axis=1)

#To insert a colum in a dataframe...
concat_2 = p.concat([concat_1,series],axis=1)
#print(concat_2)

with p.ExcelWriter('Practice_concat.xlsx') as writer:
    india_whether.to_excel(writer,sheet_name='India Whether')
    uk_whether.to_excel(writer,sheet_name='UK Whether')
    concat.to_excel(writer,sheet_name='Concatination')
    key.to_excel(writer,sheet_name='Keys')
    WindSpeed.to_excel(writer,sheet_name='Wind Speed')
    concat_1.to_excel(writer,sheet_name='Concatination_1')
    concat_2.to_excel(writer,sheet_name='Final Result')