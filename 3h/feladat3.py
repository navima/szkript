def pal1(s):
    return s[::-1] == s


def pal2(s):
    i = len(s)-1
    for elem in s:
        if elem != s[i]:
            return False
        i -= 1
    return True


def pal3(s):
    if s == '':
        return True
    else:
        return s[0] == s[-1] and pal3(s[1:-1])

def test(s):
    m = s.lower().replace(' ', '').replace('.', '').replace(',', '').replace('?', '').replace('!', '')
    print(f"{s}: {pal1(m)}, {pal2(m)}, {pal3(m)}")


def main():
    test("görög")
    test("rögög")
    test("ΝΙΨΟΝ ΑΝΟΜΗΜΑΤΑ ΜΗ ΜΟΝΑΝ ΟΨΙΝ")
    test("Do geese see God?")


if __name__ == '__main__':
    main()