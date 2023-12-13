import pandas as p

file = p.read_csv(r"C:\Users\abc\Desktop\Exel\Stock.csv",skiprows=1)
#To print specific number of rows...
file = p.read_csv(r"C:\Users\abc\Desktop\Exel\Stock.csv",skiprows=1,nrows=2)
#To repace a (n.a.) value..
file = p.read_csv(r"C:\Users\abc\Desktop\Exel\Stock.csv",skiprows=1,na_values=["n.a."])
#INstead
file = p.read_csv(r"C:\Users\abc\Desktop\Exel\Stock.csv",skiprows=1,na_values={
    'EPS' : ['n.a.','-1'],
    'R':['-1'],
    'People':['n.a.']
})
file.to_csv('new.csv',columns=['Tickers','EPS'],index=False)
file.to_csv('new.csv',header=False,index=False)
print(file)

