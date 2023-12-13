import pandas as p

template = p.DataFrame({
    'Day':['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],
    'City':['Madurai','Madurai','Madurai','Madurai','Madurai','Madurai','Madurai'],
    'Temperature':[29,34,23,19,23,29,34],
    'Humidity':[10,23,34,54,45,10,23],
})
print(template)

with p.ExcelWriter('Pivottable2.xlsx') as writer :
    template.to_excel(writer,sheet_name='Pivottable2')