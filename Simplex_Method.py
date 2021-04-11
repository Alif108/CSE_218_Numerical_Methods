import numpy as np

def simplex(A):
    
    row = len(A)
    col = len(A[0])
    
    solution = np.array([0.0 for i in range(row)])
    solutionIndx = np.array([0 for i in range(row)])
    
    mini = np.argmin(A[row-1])
    
    while(A[row-1][mini]<0):
        
        ic = np.array([0.0 for i in range(row-1)])
        for i in range(row-1):
            ic[i] = A[i][col-1]/A[i][mini]
        #print(ic)
        icMin = np.argmin(ic)
        solutionIndx[mini] = icMin+1
        
        A[icMin] = A[icMin]/A[icMin][mini]
        #print(A)
        
        for i in range(row):
            if(i == icMin):
                continue
            A[i] = A[i] + A[i][mini]*(-1)*A[icMin] 
        
        mini = np.argmin(A[row-1])
        print(A)
        #print(A[row-1][mini])
        
    for i in range(row):
        if(solutionIndx[i] != 0):
            solution[i] = A[solutionIndx[i]-1][col-1]
    
    solution[row-1] = A[row-1][col-1]
    
    return solution

#Driver Code

file = open("in2.txt","r")

z = np.array([file.readline().split()],float)

A = np.array([line.split() for line in file],float)

n = len(z[0])

z= -z

z = np.append(z, 0)

table = np.append(A,[z],axis =0)

I = np.array([[0.0] * len(table) for i in range(len(table))])

for i in range(len(table)):
    I[i][i] = 1

mat = np.matrix(table, float)
I = np.matrix(I, float)

mat = np.insert(mat, n, I, axis=1)

mat = np.array(mat)

result = simplex(mat)

for i in range(n):
    print("x",end="")
    print(i,end=" ")
    print("=",end="")
    print(result[i])

print("z= ",end="")
print(result[-1])