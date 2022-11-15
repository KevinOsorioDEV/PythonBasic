def letras():
    letra = "amnorr"
    palabra = "romlar"

    letra = list(letra)
    palabra = list(palabra)

    letra.sort()
    palabra.sort()

    print(letra, palabra)
    if letra == palabra:
        return True
    else:
        return False


if __name__ == "__main__":
    print(letras())
