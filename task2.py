import timeit
import numpy as np
import scipy.optimize as optimize

import time

def f(x): 
    return np.cos(x)/(1.+x**2)

def fprime(x):
    return (-(x**2+1.)*np.sin(x)-2.*x*np.cos(x))/(x**2+1)**2


start_time = time.time()
brentq_x = optimize.brentq(f, 0.1, 2.4)
print("--- %s seconds ---" % (time.time() - start_time))

bisect_x = optimize.bisect(f, 0.1, 2.4)
newton_x = optimize.newton(f, 0.1)
newtonx2_x = optimize.newton(f, 0.1, fprime)

bisect_time = optimize.bisect (f, 0.1, 2.4)
print("bisect", bisect_time)
brentq_time = optimize.brentq (f, 0.1, 2.4)
print("brentq", brentq_time)
newton_time = optimize.newton (f, 0.1)
print("newton", newton_time)
newtonx2_time = optimize.newton (f, 0.1, fprime)
print("newtonx2", newtonx2_time)
