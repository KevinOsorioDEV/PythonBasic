def NumeroMaximo():
    try:
        print("Ingresa tus numeros separados por una coma.")
        numeros = input(">>>")
        numeros.strip()
        numeros = numeros.split(",")

        listaNumeros = [int(x) for x in numeros]

        print(max(listaNumeros))
    except Exception as e:
        print(f"Debes ingresar una lista de numeros.\nEjemplo: 1,2,3,4,5\n{e}")


if __name__ == "__main__":
    NumeroMaximo()
