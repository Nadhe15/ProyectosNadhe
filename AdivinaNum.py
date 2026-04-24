import random

#Variables
intento = 0
dato = random.randint(1,100)

while intento != dato:
    intento = int(input("Adivine un número del 1 al 100: "))
    if dato > intento:
      print("Pista: Intenta un número más alto ")
    elif dato < intento: 
       print("Pista: Intenta un número más bajo ")

print("Muy bien, adivinaste!")

