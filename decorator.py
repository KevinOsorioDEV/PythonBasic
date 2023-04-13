
def mensaje(func):
    def wrapper():
        print("Preparando para ejecutar la funcion...")
        func()
        print("Funcion ejecutada correctamente...")
    return wrapper


@mensaje
def saludar():
    print("Hola Kevin")


if __name__ == "__main__":
    saludar()
