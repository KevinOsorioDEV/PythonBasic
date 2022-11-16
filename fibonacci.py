def fibonacci():
    a = 0
    b = 1

    for i in range(10):
        print(a)
        fibo = a + b
        a = b
        b = fibo


if __name__ == '__main__':
    fibonacci()
