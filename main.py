import time


def bumeran():
    arra1 = [2, 1, 2, 3, 3, 4, 2, 4, 2]

    try:
        for i in range(len(arra1)):
            if arra1[i] == arra1[i + 2]:
                print(arra1[i], arra1[i + 1], arra1[i + 2])
            else:
                print("")
    except IndexError:
        print("EL proceso terminó")


if __name__ == '__main__':
    bumeran()
