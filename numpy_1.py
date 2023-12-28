#Introduction To Numpy...

import numpy as n

a = n.array([[1,2,3,4],[9,8,7,6]])
b = n.array([[3,2,1],[1,2,3]])


#to get the dimension
print(a.ndim,"is the Dimension")
print(b.ndim,"is the Dimension")

#to get the shape
print(a.shape,"is the Shape")
print(b.shape,"is the Shape")

#to find type
print(a.dtype,"is the Type")
print(b.dtype,"is the Type")

#to find the size
print(a.itemsize,"is the Size")
print(b.itemsize,"is the Size")

#to get Specific element
print('to get Specific element...')
print(a[0,2]) # 0 represents row and 2 represents column
print(b[1,2])

#to get specific row
print('to get specific row...')
print(a[0,:])

#to get specific row
print('to get specific row')
print(b[:,1])

#to get little more specific
print('to get little more specific...')
print(a[0,0:3:2]) # here 0 represents the row , next 0 represent the starting index , 3 represents the ending index , 2 represents the skipping it 2 elements...
print(b[1,0:3:2])

#to alter a specific element
print('to alter a specific element...') 
a[0,3] = 2
print(f'After altering {a}')
print(f'{a[0,3] } is altered')
b[1,2] = 3
print(f'{b[1,2]} is altered')
print(f'After altering {b}')

#to alter the entire column
print('to alter the entire column...')
a[:,2] = 3
print(f'{a[:,2] } is altered')
print('After altering :',a)

#to alter the entire row
print('to alter the entire row...')
b[1,:] = 2
print(f'{b[1,:]} is altered')
print('After altering :',b)

#to All zero's matrix
print("to All zero's matrix...")
print(n.zeros((2,3)))


#to All one's matrix
print("to All one's matrix...")
print(n.ones((3,1)))

#to get all other numbers
print('to get all other numbers...')
print(n.full((2,2),100))

#to get all other numbers(full_like)
print('to get all other numbers(full_like)...')
print(n.full_like(a,4))#other method
print(n.full(a.shape,4))

#Random integer numbers
print('Random integer numbers...')
print(n.random.randint(10,size=(3,1)))

#Random decimal numbers
print('Random decimal numbers...')
print(n.random.rand(3,1))

#to copy an array
print('to copy an array...')
b = a.copy()
print('After copying :',b)

#to do arithmatic operation with element in array
print('to do arithmatic operation with element in array...')
print('A+2 :',a+2)
print('A-2 :',a-2)
print('A*2 :',a*2)
print('A/2 :',a/2)

#to find min/max of a matrix
print('to find min/max of a matrix...')
print(f'Minimum of the matrix {a}',n.min(a))
print(f'Maximum of the matrix {b}',n.max(b))

#by row basis
print(n.min(a,axis=1))
print(n.max(b,axis=1))

#to add a matrix
print('to add a matrix...')
print(n.sum(a))
print(n.sum(b))

#to reorganise the matrix
print('to reorganise the matrix...')
rearrange = a.reshape((8,1))
print(rearrange)

#to access files
filedata = n.genfromtxt('matrix.txt',delimiter=',')
print(filedata)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Matrix Multiplication

import numpy as n

a = n.ones((3,2))
b = n.ones((2,3))
print(n.matmul(a,b))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Numpy Sample

import numpy as n

a = n.ones((5,5)) 
b = n.zeros((3,3))
b[1,1] = 9
a[1:4,1:4] = b
print(a)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
