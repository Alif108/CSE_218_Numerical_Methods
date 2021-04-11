0# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

#.........a........

def ln(a,b):

    sum = 0

    for i in range(b):
        sum = sum + (-1)**i * (a**(i+1))/(i+1)

    return sum


while True:
    x = input("x: ")
    x = float(x)
    if x>-1 and x<=1:
        break
    
n = input("n: ")

n = int(n,10) 

print("ln(1+x)= ",end=" ")

print(ln(x,n))    


#........b.......

x1 = np.arange(-0.9,1,0.1)

y = np.log(1+x1)

plt.figure(1)
plt.plot(x1,y,linewidth=3)
plt.xlabel("X")    
plt.ylabel("f(x)")
plt.title("f(x) = ln(1+x)")


#.......c.......

x3 = np.array([])
y3 = np.array([])

for n in [1,3,5,20,50]:
    y3 = list(map(ln,x1,[n]*20))
    plt.plot(x1,y3)


#.......d.........

print()

print("ln(1.5)=",end=" ")
t = math.log(1.5)

print(t)

x2 = np.array([])
y2 = np.array([])

sum = 0

for i in range(n):
     sum = sum + (-1)**i * (0.5**(i+1))/(i+1)
     error = abs(1-sum/t)
     x2 = np.append(x2,i)
     y2 = np.append(y2,error)

plt.figure(2)
plt.plot(x2,y2,linewidth=3,color="orange")
plt.xlabel("Iterations")
plt.ylabel("Error")