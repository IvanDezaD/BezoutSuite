#!/bin/python3


def mcd(a, b):
    if a % b == 0:
        return b
    else:
        return mcd(b, a % b)


def main():
    a = int(input("Enter yor a number: "))
    b = int(input("Enter your b number: "))
    c = mcd(a, b)
    print("The result of mcd({},{})={}".format(a, b, c))


if __name__ == "__main__":
    main()
