import math

if __name__ == '__main__':
    M = int(input("Enter M = "))
    N = int(input("Enter N = "))
    D = int(input("Enter D = "))
    test_arr = []
    for i in range(int(M/D), int(N/D), 1):
        test_arr.append(i*D)

    for i in test_arr:
        for j in test_arr:
            if i < j:
                if math.gcd(i, j) == D:
                    print([i, j], end=', ')
