def isTPrime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            if count == 1:
                return False
            count += 1
    if count == 1:
        return True
    return False

if __name__ == "__main__":
    n = int(input('Enter n = '))

    for i in range(n + 1):
        if isTPrime(i):
            print(i,end=", ")
