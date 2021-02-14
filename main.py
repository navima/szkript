#!/usr/bin/env python3

import sys


def main():
    print("Hello world!")
    if True:
        print('Aloha!')
    #
    if len(sys.argv) >= 2:
        pre = ""
        if sys.argv[1] == 'Balázs':
            print("Szia, ", end="")
        else:
            print("おはよう　ございます, ", end="")
        print(sys.argv[1] + '!')
#

# ha modulként futtatod akkor ez hamis
if __name__ == '__main__':
    main()
