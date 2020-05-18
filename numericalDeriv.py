import numpy as np

def f(x): 
    return (x**3-4) 
    
def f_derived(x): 
    return (3*x**2)

def all_3_methods(f,a,method='central',h=0.01):
    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'forward':
        return (f(a + h) - f(a))/h
    elif method == 'backward':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Choose one of the 3 methods.")

        

print(all_3_methods(f,0,method='central',h=0.1))
print(all_3_methods(f,0,method='central',h=0.01))

print(all_3_methods(f,0,method='forward',h=0.1))
print(all_3_methods(f,0,method='forward',h=0.01)) 

print(all_3_methods(f,0,method='backward',h=0.1))
print(all_3_methods(f,0,method='backward',h=0.01))
