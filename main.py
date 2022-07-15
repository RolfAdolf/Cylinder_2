import numpy as np
import scipy as sp
import JADE
import Parlgram
import Cylinder

##root finding function
from scipy import optimize

[a_1, a_2, b_1, b_2, c_1, c_2] = [-2, 2, -2, 2, -1, 4]
Parm = Parlgram([a_1, a_2, b_1, b_2, c_1, c_2])
R = 1
h = 3
I = [0, 0, 0]


Parm = Parlgram([])


#Does Cylinder with current parameters intersect at least one of parallelogram boundaries?
#cyl - Cylinder
#parm - Parlgram
#nm - boundary number
#f - function of equation: f(x, y, z) = 0
#For example:
#f[0]: x^2 + y^2 - R   --  Cylinder implicit equation 
#f[1]: z - 6           --  Upper boundary for Oz.
def IsIntersect(cyl, parm):

    ###Body
    ##Trying to check at least one of boundaries (upper for Oz).
    #f = np.zeros([3])

    #if ((x[2]-cyl.x_0) <= cyl.h):
    #    f[0] = (x[0]-I[0])**2+(x[1]-I[1])**2-R
    #    f[1] = (x[2]-I[2]) - c_2
    #    f[2] = 0
    #else:
    #    f[0] = 5
    #    f[1] = 5
    #    f[2] = 5
    #return f
    return 0

def F(R_tol, h_tol, x_0, y_0, z_0):
    
    I = [x_0, y_0, z_0]
    Cyl = Cylinder(R+R_tol, h+h_tol, I)

    if ( IsIntersect( cyl=Cyl, parm = Parm) ):
        return 0
    return np.min(R_tol, h_tol, np.sqrt(x_0**2 + y_0**2 + z_0**2))

print(JADE(F))


#x0 = np.zeros([3])
#sol = optimize.root(F, x0, method='df-sane')
#sol = optimize.fsolve(F, x0)
print('Solution:\n', x)