import numpy as np
import scipy as sp
from scipy import optimize
import time 
R = 1
h = 10
I = [0, 0, 0]

a_1 = 0
a_2 = 0
b_1 = 0
b_2 = 0
c_1 = 0
c_2 = 5

def Cylinder(x, R, h, I = [0, 0, 0]):

    f = np.zeros([3])

    if ((x[2]-I[2]) <= h):
        f[0] = (x[0]-I[0])**2+(x[1]-I[1])**2-R
        f[1] = (x[2]-I[2]) - c_2
        f[2] = 0
    else:
        f[0] = 5
        f[1] = 5
        f[2] = 5
    return f

def F(x):
    return Cylinder(x, R, h, I = [0, 0, 0])


x0 = np.zeros([3])
#sol = optimize.root(F, x0, method='df-sane')
sol = optimize.fsolve(F, x0)
x = [round(i, 4) for i in sol.x]
print('Solution:\n', x)