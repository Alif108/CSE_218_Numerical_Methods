import numpy as np
import matplotlib.pyplot as plt

def f(x):
    
    return (x/(1-x)) * (6/(2+x))**0.5 - 0.05


#...........false_position_method..........

def fp(xl,xu,Es,maxi):
    
    i = 0
    Ea = 1.1 * Es
    xr0 = 0
    while Ea>Es and i < maxi:
        
        xr = xu - (f(xu)*(xl-xu))/(f(xl)-f(xu))
        i = i+1
        
        if i!=1 and xr!=0:
            Ea = abs((xr-xr0)/xr)*100
        test = f(xl) * f(xr)
        if test==0:
            Ea = 0
        elif test<0:
            xu = xr
            xr0 = xr
        else:
            xl = xr
            xr0 = xr

    print("FALSE POSITION METHOD")
    print("X =",xr)
    print("f(x)= ",f(xr))
    print("Error= ",Ea)
    print("Iterations= ",i)
    
#.......secant_method..........

def sec(x0,x1,Es,maxi):
    
    i = 0
    Ea = 1.1*Es
    
    while Ea>Es and i < maxi:
         
        x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        i+=1
         
        if i!=1 and x2!=0:
            Ea = abs((x2-x1)/x2)*100
             
        x0 = x1
        x1 = x2
    
    print("SECANT METHOD")
    print("X =",x2)
    print("f(x)= ",f(x2))
    print("Error= ",Ea)
    print("Iterations= ",i)



while True:
    xL = input("Xl = ")
    xL = float(xL)
    xU = input("Xu = ")
    xU = float(xU)
    if f(xL)*f(xU)<0:
        break


I = input("Max iterations = ")
I = int(I,10)
print()

x1 = np.arange(xL,xU,0.01)

y = f(x1)

plt.plot(x1,y)
plt.xlabel("X")
plt.ylabel("f(x)")
plt.grid(True)
    
fp(xL,xU,0.5,I)
print()
sec(xL,xU,0.5,I)