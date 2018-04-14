import timeit
import numpy as np
import scipy.optimize as optimize

import time

def f(x): 
    return np.cos(x)/(1.+x**2)

def fprime(x):
    return (-(x**2+1.)*np.sin(x)-2.*x*np.cos(x))/(x**2+1)**2

print("time of calculations:")
start_time = time.time()
bisect_x = optimize.bisect(f, 0.1, 2.4)
print("bisect %s seconds" % (time.time() - start_time))

start_time = time.time()
newton_x = optimize.newton(f, 0.1)
print("newton - %s seconds " % (time.time() - start_time))

start_time = time.time()
newtonx2_x = optimize.newton(f, 0.1, fprime)
print("secant - %s seconds " % (time.time() - start_time))


start_time = time.time()
brentq_time = optimize.brentq (f, 0.1, 2.4)
print("brenth - %s seconds " % (time.time() - start_time))


