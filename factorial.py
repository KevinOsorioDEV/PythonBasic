

def CalcularFactorial():

    print("CALCULAR FACTORIAL!")
    numero = int(input("Ingese su numero -> "))

    factorial = 1
    for i in range(1, numero+1):
        factorial = factorial * i

    print(f"El factorial del {numero} es: {factorial}")


if __name__ == "__main__":
    CalcularFactorial()
