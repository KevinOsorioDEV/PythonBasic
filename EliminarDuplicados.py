

def EliminarDuplicados():
    print("ELIMINAR DUPLICADOS")
    frase = input("Ingrese su frase -> ")

    fraseResultado = ""
    for i in frase:
        if not (i in fraseResultado):
            fraseResultado += i

    print(fraseResultado)


if __name__ == "__main__":
    EliminarDuplicados()
