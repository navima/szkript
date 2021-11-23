TEXT = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""


def main():
    decoded = ""
    for char in TEXT:
        if ord('a') <= ord(char.lower()) <= ord('z'):
            temp = chr(
                (ord(char.lower()) + 2 - ord('a')) % (ord('z') - ord('a') + 1)
                + ord('a'))
            if char.isupper():
                decoded += temp.upper()
            else:
                decoded += temp
        else:
            decoded += char
    print(decoded)


if __name__ == '__main__':
    main()