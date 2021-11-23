def remove_whitespace(s):
    return "".join(s.split())


def main():
    print(remove_whitespace("192.20.246.138:\n 6666"))
    print(remove_whitespace("206.130.99.82:\n8080"))
    print(remove_whitespace("\x201\x20    9 8.2\n\t59.-1.     0:\n8 0 8 0"))


if __name__ == '__main__':
    main()