def fibonacci():
    a = 0
    b = 1

    for i in range(10):
        print(a)
        fibo = a + b
        a = b
        b = fibo


def FiboRecusivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FiboRecusivo(n-1) + FiboRecusivo(n-2)


if __name__ == '__main__':
    # fibonacci()
    n = 100
    for i in range(n):
        print(FiboRecusivo(i))
