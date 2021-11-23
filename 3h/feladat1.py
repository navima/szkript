def mult(l):
    res = 1
    for elem in l:
        res *= elem
    return res


def main():
    print(mult([5, 10, 2]))
    print(mult([]))
    print(mult([0]))


if __name__ == '__main__':
    main()