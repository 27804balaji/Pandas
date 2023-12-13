import pandas as p

first_data = p.DataFrame({
    
    'City':['New York','Paris','Chicago'],
    'Temperature':[29,34,101],
})

second_data = p.DataFrame({
    
    'City':['New York','Paris','London'],
    'Humidity':[24,25,26],
})


third_data = p.DataFrame({
    
    'City':['New York','Paris','Cambridge'],
    'Wind Speed':[241,50,126],
})
merge = p.merge(first_data,second_data,on='City',how='outer')#'outer' means "Outer join"

#Using Indicator to indicate the where the value is from...
merge_1 = p.merge(merge,third_data,on='City',how='inner',indicator=True)#'inner' means "Inner join"
print(merge_1)

#Using Suffix...

x_data = p.DataFrame({
    'City':['New York','London','Chennai'],
    'Temperature':[23,34,45],
    'Humidity':[12,14,15]
})


y_data = p.DataFrame({
    'City':['New York','London','Chennai'],
    'Temperature':[45,34,23],
    'Humidity':[15,14,12]
})

z_data = p.merge(x_data,y_data,on='City',suffixes=('_first','_second'))
print(z_data)

with p.ExcelWriter('Merge.xlsx') as writer:
    first_data.to_excel(writer,sheet_name='First Data')
    second_data.to_excel(writer,sheet_name='Second Data')
    third_data.to_excel(writer,sheet_name='Third Data')
    merge_1.to_excel(writer,sheet_name='First Output')
    x_data.to_excel(writer,sheet_name='Suff First Data')
    y_data.to_excel(writer,sheet_name='Suff Second Data')
    z_data.to_excel(writer,sheet_name='Second Output')