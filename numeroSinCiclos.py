
def PrintNumbers(num: int):
    print(num)
    if num < 100:
        PrintNumbers(num + 1)


if __name__ == "__main__":
    PrintNumbers(0)
