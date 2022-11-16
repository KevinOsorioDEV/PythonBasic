def esPrimo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


if __name__ == '__main__':
    for i in range(1, 100):
        if esPrimo(i):
            print(i)
