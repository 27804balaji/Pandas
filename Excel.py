import pandas as p

#This Function prints a value if the people column consist a (n.a.)...
def convert_people_cell(people):
    if people == "n.a.":
        people = input("Enter a Name :")
    return people

def convert_EPS_cell(value):
    if value == "n.a.":
        return None
    return value
excel = p.read_excel(r"C:\Users\abc\Desktop\Exel\Stock_1.xlsx",skiprows=1,converters={
    'People':convert_people_cell,
    'EPS':convert_EPS_cell

})
excel.to_excel("new_excel.xlsx",sheet_name="stocks",startcol=2,startrow=3,index=False)
print(excel)