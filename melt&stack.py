import pandas as p

#Melt...

data = p.read_csv(r'C:\Users\abc\Desktop\Exel\pivottable2.csv')
data_1  = p.melt(data,id_vars=['Day'],var_name='City',value_name='Temperature') # id_vars represents that the thing should be in the 'x' axis...
#print(data_1)

#Stack...

info = p.read_excel(r'C:\Users\abc\Desktop\Exel\stack.xlsx',header=[0,1])# header is used to print a particular rows in the excel work book...
#print(info)
stack = info.stack()
sack = info.stack(level=1)#level is used to change the actual rows in columns...
#print(sack)
new_sack = sack.stack(dropna=1)#dropna method is used to avoid the NaN,NaT values...
#print(new_sack)

#Unstack...(Unstack is used to reverse back the stacked dataframe)

un = p.read_excel(r'C:\Users\abc\Desktop\Exel\stack_1.xlsx',header=[0,1])
u = un.stack(level=1)
print(u)
