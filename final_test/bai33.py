import numpy



def inversionInFp(a, p): 
    u = a
    v = p
    x1 = [1]
    x2 = [0]
    while u[0] != 1:
        q ,r= numpy.polynomial.polynomial.polydiv(v, u)
        for i in range(len(q)):
            q[i] = a[i]*x1

        x =numpy.polynomial.polynomial.polysub(x2,numpy.polynomial.polynomial.polysub(q,u))
        
        v = u
        u = r
        x2 = x1
        x1 = x
    return x1
def enterArr():

    n = list(map(int, input().strip().split()))
    return n


import numpy
 
print("Gx: ")
# define the polynomials
# p(x) = 5(x**2) + (-2)x +5
gx = enterArr()
print("Ax: ")
ax =enterArr()
print(inversionInFp(ax,gx))



