import math

def inversionInFp(a, p): 
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = int(v/u)
        r = v - q*u
        x = x2 - q*x1
        v = u
        u = r
        x2 = x1
        x1 = x

    return x1
if __name__ == "__main__":
    a = int(input("Enter a = "))
    p = int(input("Enter p = "))
    print("a^-1 mod p = ",end="")
    print(inversionInFp(a,p))


