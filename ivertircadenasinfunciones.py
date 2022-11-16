def invertirCadena(chain):
    a = []
    for i in range(len(chain), 0, -1):
        a.append(chain[i-1])

    a = ''.join(a)
    return a


print(invertirCadena("hola mundo"))
