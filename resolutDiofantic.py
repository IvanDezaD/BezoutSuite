#!/usr/bin/python3

# Funcion que resuelve la identidad de bezout para 2 numeros
def resolute(a, b, dictionary, n):
    if a % b == 0:
        return b, 0, 1
    else:
        n += 1  # Aumentamos el iterador
        nextb = (
            a % b
        )  # La proxima vez que llamemos a la funcion esta sera nuestra b, mientras que la b anterior sera nuestra a esta vez
        mult = int(
            a / b
        )  # Necesitamos saber por cuanto multiplicar la b en cada iteracion
        dictionary[f"{n}"] = {
            "resto": a,
            "mult": mult,
            "b": b,
        }  # Guardamos la informacion que necesitaremos a lo largo de las llamadas recursivas
        mcd, x, y = resolute(
            b, nextb, dictionary, n
        )  # Llamamos, lo que irá llenando nuestra etructura de datos.
        return mcd, y, x - mult * y  # Actualiza la operacion


# Funcion main del codigo
def main():
    a = int(input("Introduce el numero a: "))
    b = int(input("Introduce el numero b: "))
    if a < b:
        a, b = b, a
    dictionary = {}
    mcd, x, y = resolute(
        a, b, dictionary, 0
    )  # Deberiamos hacer una inmersion pero soy demasiado lazy para hacer eso para este programa de mierda
    print("The result of mcd({},{})={}".format(a, b, mcd))
    print(f"La identidad de bezout que satisface es: {a}*({x})+{b}*({y}) = {mcd}")


if __name__ == "__main__":
    main()
