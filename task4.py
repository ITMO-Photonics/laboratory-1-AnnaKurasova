import scipy.linalg as lng 
import numpy as np
import time
N = 5
A = np.random.random((N,N))
k = np.arange(N)
b = np.zeros(N)

for l in range(0,3): print ('.')

# scipy.linalg.solve
for t in np.linspace(0.,0.1,5):
    b = k/(1.+ k * t) 
    res1 = lng.solve(A,b)
start_time =time.time()
for i in  range (100):
    lng.solve(A,b)
print("scipy.linalg.solve - %s sec" % (time.time()-start_time))

# scipy.linalg.lu_solve
lu,piv = lng.lu_factor(A)
for t in np.linspace(0.,0.1,5):
    b = k/(1.+ k * t) 
    res2 = lng.lu_solve((lu,piv), b)
start_time =time.time()
for i in  range (100):
    lng.lu_solve((lu,piv), b)  
print("scipy.linalg.lu_solve - %s sec" % (time.time()-start_time))

# scipy.linalg.inv (нахождение обратной матрицы)
A2 = lng.inv(A) #обратная матрица
for t in np.linspace(0.,0.1,5):
    b = k/(1.+ k * t) 
    res3 = np.dot(A2,b) 
start_time =time.time()
for i in  range (100):
    np.dot(A2,b)
print("scipy.linalg.inv - %s sec" % (time.time()-start_time))

for l in range(0,3): print ('.')
