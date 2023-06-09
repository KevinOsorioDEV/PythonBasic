def CombinacionesCadenas():
    listaString = ["abc", "123"]

    for i in range(len(listaString)):
        palabra = listaString[i]
        lista = []

        for j in palabra:
            for k in palabra:
                for l in palabra:
                    lista.append(j+k+l)

        print(f'{i+1} - {",".join(lista)}')


if __name__ == "__main__":
    CombinacionesCadenas()
