
#To replace a list of values...
import pandas as p
import numpy as n

student = p.DataFrame({
    'Score':['exceptional','good','average','poor','exceptional'],
    'Student':['Balaji','Kishore','Jeevan','Asty','Delvin']
})

student = student.replace(['poor','average','good','exceptional'],[1,2,3,4])
print(student)