import time
import threading


def incrementarVariable(lock
                        ):
    global variableCompartida
    time.sleep(1)
    with lock:
        variableCompartida += 1
        print(
            f"El valor actual de la variable compartida es {variableCompartida}")


variableCompartida = 0
lock = threading.Lock()

hilo1 = threading.Thread(target=incrementarVariable, args=(lock,))
hilo2 = threading.Thread(target=incrementarVariable, args=(lock,))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()


print(f"El valor final de la variable compartida es {variableCompartida}")
