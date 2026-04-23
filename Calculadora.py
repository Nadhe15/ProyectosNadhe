#Variables
num1 = float(input("Ingrese el primer número a operar: "))
num2 = float(input("Ingrese el segundo número a operar: "))
operador = input("Elija una operación(-, +, /, * ): ")

print("Primer número ", num1)
print("Segundo número ", num2)
print("Operador ", operador)

if operador == "+": 
    result = num1 + num2
    print("El resultado es: ", result)

elif operador == "-" :
    result = num1 - num2
    print("El resultado es: ", result)

elif operador == "*" :
    result = num1 * num2
    print("EL resultado es: ", result)

elif operador == "/" :
    if num2 == 0:
        print("División no válida")
    else:
       result = num1 / num2
       print("El resultado es: ", result)

else: 
    print("Operador incorrecto ")


