import numpy 

N, M = input().split()
array=[]
for x in range (int(N)):
    E1 , E2=input().split()
    array.append([int(E1),int(E2)])
 
m=numpy.mean(array,axis=1) 
var=numpy.var(array,axis=0)
std=numpy.std(array,axis=None)
numpy.set_printoptions(legacy='1.13')
print(m)
