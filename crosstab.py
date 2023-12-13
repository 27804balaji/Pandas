import pandas as p

data = p.read_excel(r"C:\Users\abc\Desktop\Exel\cricketer.xlsx")

# crosstab is used to display the list based on variables...
data_1 = p.crosstab(data.Country,data.Handedness,margins=True)#margins is used to print the total...
#print(data_1) 

#We can pass more variable...
data_2 = p.crosstab(data.Handedness,[data.Age,data.Country])
#print(data_2)

#To find percentage value normalize() is used...
data_3 = p.crosstab(data.Country,data.Handedness,normalize='index')
print(data_3)