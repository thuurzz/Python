import math as m
import numpy as np

V=[3, 0, -1]
W=[-2, 1, 1]
X=[0, -3, 2]

 s=(V[i]+W[i])+X[i]

print("Soma\n",np.equal(s1,s2))

m1=(V*W)*X[0]
m2= V[0]*(W*X)

print("Mul\n",np.equal(m1,m2))
