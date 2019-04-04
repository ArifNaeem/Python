import numpy 

N= input()
array1=[]
array2=[]

for y in range(int(N)):
 array1.append(input().split())
 A = [list(map(int, x)) for x in array1]
  
for y in range(int(N)):
 array2.append(input().split())
 B = [list(map(int, x)) for x in array2]
c=numpy.matmul(A,B)  
print(c)