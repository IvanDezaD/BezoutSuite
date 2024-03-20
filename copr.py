#!/usr/bin/python3

def mcd(a, b):
    if a % b == 0:
        return b
    else:
        return mcd(b, a % b)


def esCoprimo(num1, num2):
    return mcd(num1, num2) == 1 #Devolvemos true si y solo si mcd = 1, si no devolveremos 0

def calcularCoprimos(num):
    for i in range(2, num):
        if esCoprimo(i, num):
            print(f"Found coprimo con {num}: {i}")

def main():
    num = int(input("Ingrese el número para calular sus coprimos: "))
    calcularCoprimos(num)

if __name__ == '__main__':
    main()
