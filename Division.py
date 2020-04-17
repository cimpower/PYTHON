def main():
    print("DIVISOR DE NÚMEROS")
    dividendo = int(input("Escriba el dividendo: "))
    divisor = int(input("Escriba el divisor: "))

    if dividendo % divisor:
        print(
            f"La división no es exacta. Cociente: {dividendo // divisor} "
            f"Resto: {dividendo % divisor}"
        )
    else:
        print(f"La división es exacta. Cociente: {dividendo // divisor}")


if __name__ == "__main__":
    main()
    