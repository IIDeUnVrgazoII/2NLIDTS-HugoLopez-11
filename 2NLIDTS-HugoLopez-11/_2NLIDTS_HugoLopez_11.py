def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + (n % 10) 

def suma_iterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n

def main():
    cantidad = int(input("Cuantos numeros va a ingresar? "))
    
    for i in range(cantidad):
        numero = int(input(f"\nIngrese el numero {i + 1}: "))
        
        print(f"Resultado (Recursiva): {suma_recursiva(numero)}")
        print(f"Resultado (Iterativa): {suma_iterativa(numero)}")

if __name__ == "__main__":
    main()