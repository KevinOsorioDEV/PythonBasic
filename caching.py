import time
from functools import lru_cache


@lru_cache(maxsize=None)
def calculo_costoso(n):
    time.sleep(5)
    return n * 33


if "__main__" == __name__:
    print(calculo_costoso(6))
    print(calculo_costoso(6))
    print(calculo_costoso(6))
    print(calculo_costoso(6))
    print(calculo_costoso(6))
