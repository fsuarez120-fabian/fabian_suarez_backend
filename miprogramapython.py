def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero"
    else:
        return num1 / num2

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    print("Suma:", suma(num1, num2))
    print("Resta:", resta(num1, num2))
    print("Multiplicación:", multiplicacion(num1, num2))
    print("División:", division(num1, num2))

if __name__ == "__main__":
    main()
