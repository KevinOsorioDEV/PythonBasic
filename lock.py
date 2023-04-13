import threading

listaCompartida = []

lock = threading.Lock()


def agregarElemento(elemento):
    lock.acquire()

    listaCompartida.append(elemento)

    lock.release()


hilo1 = threading.Thread(target=agregarElemento, args=("elemento1",))
hilo2 = threading.Thread(target=agregarElemento, args=("elemento2",))


hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(listaCompartida)
