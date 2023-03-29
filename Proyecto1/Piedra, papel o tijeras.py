#Código para importar las opciones randoms de la computadora
import random

#Mensaje al empezar el juego
print("¡Hola! Me llamo Richard y te reto a un juego de Piedra, Papel o Tijeras :)")

#Variable para las opciones que puede elegir el jugador y la computadora
opciones = ["Piedra", "Papel", "Tijeras"]

while True:
    # El jugador escoge su opción
    jugador = input("Elige Piedra, Papel o Tijeras: ")
    #Para que haya consistencia con las opciones a elegir y no haya errores
    jugador = jugador.capitalize()

    #Para que la computadora elija aletoriamente
    Richard = random.choice(opciones)

    print("Tú elegiste " + jugador + ", Richard eligio " + Richard + "." )

    #Para que empiece el juego
    if jugador == Richard:
        print("¡Empate!")
    elif jugador == "Piedra":
        if Richard == "Papel":
            print("¡Perdiste! :(")
        else:
            print("¡Ganaste! :D")
    elif jugador == "Papel":
        if Richard == "Tijeras":
            print("¡Perdiste! :(")
        else:
            print("¡Ganaste! :D")
    elif jugador == "Tijeras":
        if Richard == "Piedra":
            print("¡Perdiste! :(")
        else:
            print("¡Ganaste! :D")

    #Le preguntamos al jugador si quiere terminar o no
    continuar = input("¿Quieres continuar jugando :)? (s/n) ")
    if continuar.lower() != "s":
        break

print("Jejeje. Gracias por jugar")



