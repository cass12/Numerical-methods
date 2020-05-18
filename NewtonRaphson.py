#prima ecuatie x-(x**3+4*x**2-10)/(3*x**2+8*x)
#a doua ecuaie x*cos(x)

import math
import numpy as np

def f(x):
  return x-(x**3+4*x**2-10)/(3*x**2+8*x)

def f_derived(x):
  return 1-(3*x**2+8*x-10)/(6*x+8)

def f1(x):
    return x*math.cos(x)

def f1_derived(x):
    return math.cos(x)-x*math.sin(x)

def Newton(p_init,tol,n):
    i=1
    while i < n:
        p=p_init-f(p_init)/f_derived(p_init)
        #p=p_init-f1(p_init)/f1_derived(p_init)
        if abs(p-p_init) < tol:
            print ("The solution for step" , i , "is", p)
        i=i+1
        p_init=p
    print ("The method failed after", n,  "iterations")
    print("The procedure was unsuccessful")

print(Newton(1.5,10**-8,20))
#print(Newton(2.0,10**3,10))
