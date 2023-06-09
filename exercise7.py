def unusual_func(x: list):
    if all(x):
        return "Hello"
    elif not x:
        return "Hi"
    else:
        return "Goodbye"


if __name__ == '__main__':
    lst = [1, 2, -3, 4, 0]
    print(unusual_func(lst))
