if __name__ == "__main__":

    n = int(input('Enter n= '))

    for a in range(1, n):
        divisorOfA = []
        for i in range(1, a):
            if a % i == 0:
                divisorOfA.append(i)

        b = sum(divisorOfA)
        divisorOfB = []

        for j in range(1, b):
            if b % j == 0:
                divisorOfB.append(j)
        if sum(divisorOfB) == a and a != b:
            print([a, b])
