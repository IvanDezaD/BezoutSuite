#!/usr/bin/python3

def mcd(a, b):
    if a % b == 0:
        return b
    else:
        return mcd(b, a % b)


def esCoprimo(num1, num2):
    return mcd(num1, num2) == 1 #Devolvemos true si y solo si mcd = 1, si no devolveremos 0

def calcularInversos(num, lista1, lista2):
    for num1 in lista1:
        for num2 in lista2:
            if (num1 * num2 % num) == 1:
                print(f"Encontrado una pareja de inversos multiplicativos: {num1}*{num2} (mod{num}) = 1")



def calcularCoprimos(num):
    lista = []
    for i in range(1, num):
        if esCoprimo(i, num):
            print(f"Encontrado coprimo con {num}: {i}")
            lista.append(i)
    return lista

def main():
    num = int(input("Ingrese el número para calular sus coprimos: "))
    list1 = calcularCoprimos(num)
    list2 = list(list1)
    calcularInversos(num, list1, list2)

if __name__ == '__main__':
    main()
