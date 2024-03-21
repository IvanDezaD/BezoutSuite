#!/bin/python3

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def phi_euler(n):
    if n == 1:
        return 1

    factors = set(prime_factors(n))  # Obtén los factores primos únicos de n

    result = n
    for factor in factors:
        result *= (1 - 1 / factor)

    return int(result)

def main():
    n = int(input("Introduzca el numero para calcular la phi de euler: "))
    print(f"La phi de euler de {n} es: {phi_euler(n)}")
    return


if __name__ == "__main__":
    main()
