import scipy.linalg as linalg
import numpy as np
m=15
A=np.zeros((m,m))
i,j=np.indices(A.shape)
A[i == j] = 1
A[i == j+1] = 1
A[i == j+2] = 1

B = np.arange(m)
C = np.linalg.solve(A, B)
print(C);
