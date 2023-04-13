

def func(lst):
    for i in range(len(lst)):
        lst[i] *= lst[i]
    return lst


if __name__ == '__main__':
    lst = [2]
    func(lst)
    print(func(lst))
