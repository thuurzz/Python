import math

a = int(input())
x = math.radians(a)

n = int(input())


cos_approx = 0
for i in range(n):
    coef = (-1)**i
    num = x**(2*i)
    denom = math.factorial(2*i)
    cos_approx += ( coef ) * ( (num)/(denom) )


cos_approx = round(cos_approx, 5)
print(cos_approx)
