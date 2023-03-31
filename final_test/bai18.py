import math


def enterArr():

    n = list(map(int, input("Array :").strip().split()))
    return n


def intToArr(a, p, W):  # Bai 1.a
    t = math.ceil(math.log(p, 2)/W)
    A = [0]*t

    for i in range(t, 0, -1):
        A[t-i] = math.floor(a/math.pow(2, W*(i-1)))
        a -= math.pow(2, (i-1)*W)*A[t-i]
    return A


def arrToInt(A, W):  # Bai 1.b
    t = len(A)
    a = 0
    for i in range(len(A)):
        a += math.pow(2, (t-i-1)*W)*A[i]

    return int(a)


def multiprecision_addition(A, B, p, W):  # Bai 2
    t = math.ceil(math.log(p, 2)/W)

    C = [0]*t
    e = 0
    C[t-1] = int((A[t-1]+B[t-1]) % math.pow(2, W))

    for i in range(t-1, 0, -1):
        if 0 <= A[i] + B[i] + e <= math.pow(2, W):

            e = 0
        else:
            e = 1

        C[i-1] = int((A[i-1]+B[i-1] + e) % math.pow(2, W))
    if 0 <= A[0]+B[0]+e <= math.pow(2, W):
        e = 0
    else:
        e = 1

    return C




if __name__ == "__main__":
    a = int(input("Enter a = "))    
    b = int(input("Enter b = "))
    p = int(input("Enter p = "))
    W = int(input("Enter W = "))
    print("Int :", end=" ")
    print(arrToInt(multiprecision_addition(intToArr(a,p,W),intToArr(b,p,W),p,W)))
    print("Arr :",end=" ")
    print(multiprecision_addition(intToArr(a,p,W),intToArr(b,p,W),p,W))



    

