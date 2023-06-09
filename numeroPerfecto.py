def NumeroPerfecto():
    print("Calcular numero perfecto.")

    try:
        numero = int(input("Ingrese su numero --> "))

        if numero <= 1:
            return ("Para ser un numero perfecto tiene que ser positivo y mayor a 1.")

        contadorDivisores = 0

        for div in range(1, numero):
            if numero % div == 0:
                contadorDivisores += div

        if numero == contadorDivisores:
            return (f"El numero {numero} es perfecto.")

        return (f"El numero {numero} no es perfecto.")
    except Exception as e:
        return (f"Tienes que ingresar un numero.\n{e}")


if __name__ == "__main__":
    print(NumeroPerfecto())
