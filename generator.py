
def numeros_enteros(n):
    for i in range(n):
        yield i


if __name__ == '__main__':
    for num in numeros_enteros(20):
        print(num)
