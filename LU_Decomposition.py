import numpy as np

def LU(A,n):
    
    L = np.array([[0.0] * n for i in range(n)])
    U = np.array([[0.0] * n for i in range(n)])
    
    for i in range(n):
        
        L[i][i] = 1
        
        for k in range(i,n):
            s1 = 0
            for j in range(i):
                s1 = s1+U[j][k]*L[i][j]
            U[i][k] = A[i][k] - s1
            
        for k in range(i,n):
                s2 = 0
                for j in range(i):
                    s2 = s2+U[j][i]*L[k][j]
                L[k][i] = (A[k][i] - s2)/U[i][i]
    
    return L,U

def Unique(A):

    for i in range (len(A)):
        c=0
        for j in range(len(A)):
            if(A[i][j]==0):
                c+=1
        if(c==len(A)):
            return 1
        
def Y(B,L):
    
    y = np.array([0 for i in range (n)])

    for i in range(0,n):
        y[i] = B[i]/(L[i][i])
        for j in range (0,i):
            y[i] = y[i] - y[j]*L[i][j]
    
    return y

def X(y,U):
    
    x = np.array([0 for i in range(n)])
    
    #for i in range(n-1,-1,-1):
     #   x[i] = y[i]/U[i][i]
      #  for j in range(i-1,-1,-1):
       #     x[i] = x[i] -x[j]*U[i][j]
    y = np.matrix(y,float)
    y = y.transpose()
    x = np.matrix(x,float)
    U = np.matrix(U,float)
    Ui = np.linalg.inv(U)
       
    x = np.dot(Ui,y)
    x = np.array(x)

    return x

#Driver Code
    
file1 = open("in1.txt","r+")

n = int(file1.readline())

A = np.array([file1.readline().split(" ") for i in range (n)],float)

B = np.array([file1.readline().split(" ") for i in range(n)],float)

file1.close()

L,U = LU(A,n)

file2 = open("out1.txt","w")

for i in range(n):
    for j in range(n):
        file2.write(str(round(L[i][j],4)))
        file2.write(" ")
    file2.write("\n")
    
file2.write("\n")
    
for i in range(n):
    for j in range(n):
        file2.write(str(round(U[i][j],4)))
        file2.write(" ")
    file2.write("\n")

file2.write("\n")       

if(Unique(U)==1):
    file2.write("No Unique Solution")

else:
    y = Y(B,L)

    x = X(y,U)
    
    for i in range(n):
        file2.write(str(round(y[i],4)))
        file2.write("\n")
    
    file2.write('\n')

    for i in range(n):
        file2.write(str(x[i])) 
        file2.write("\n")

file2.close()