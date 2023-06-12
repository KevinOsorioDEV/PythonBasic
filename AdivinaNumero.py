from random import randint


def AdivinaNumero():
    print("ADIVINA EL NUMERO!")

    numeroAleatorio = randint(1, 100)
    numero = int(input("Escribe un numero --> "))

    while numero != numeroAleatorio:
        if numero < numeroAleatorio:
            print("El numero debe ser mayor.")
            numero = int(input("--> "))

        if numero > numeroAleatorio:
            print("El numero debe ser menor.")
            numero = int(input("--> "))

    print(f"Numero encontrado! - {numeroAleatorio} -")


if __name__ == "__main__":
    AdivinaNumero()
