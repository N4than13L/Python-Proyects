import time 

nombre = str(input('pon tu nombre: '))
print("Hola " + nombre, " que empieze el juego")

print(" ")
time.sleep(1)

print("comienza a adivinar que palabra esta en los hasteriscos")
time.sleep(0.5)

palabra = "dominicana"
tu_palabra = ""

vidas = 5

while vidas > 0:
    fallas = 0

    for letra in palabra:
        if letra in tu_palabra:
            print(letra, end="")
        else:
            print("*", end="")
            fallas+= 1

    if fallas == 0:
        print("")
        print(" felicidades Has Ganado" + " " + nombre)
        break

    tu_letra = str(input(" escribe una letra: "))
    tu_palabra += tu_letra

    if tu_letra not in palabra:
        vidas -=1
        print("equivocacion")
        print(vidas)

    if vidas == 0:
        print("perdiste")
else:
    print("gracias por jugar")
