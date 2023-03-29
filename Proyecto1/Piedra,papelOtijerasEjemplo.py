import random

print("Bienvenido al juego de Piedra, Papel o Tijeras!")

# Las opciones que tiene el jugador
opciones = ["Piedra", "Papel", "Tijeras"]

while True:
    # El jugador escoge su opción
    jugador = input("Elige Piedra, Papel o Tijeras: ")
    jugador = jugador.capitalize()
    
    # La computadora escoge su opción
    computadora = random.choice(opciones)
    
    # Se muestran las opciones escogidas
    print("Tú elegiste " + jugador + ", la computadora eligió " + computadora + ".")
    
    # Se determina el ganador
    if jugador == computadora:
        print("¡Empate!")
    elif jugador == "Piedra":
        if computadora == "Papel":
            print("¡Perdiste!")
        else:
            print("¡Ganaste!")
    elif jugador == "Papel":
        if computadora == "Tijeras":
            print("¡Perdiste!")
        else:
            print("¡Ganaste!")
    elif jugador == "Tijeras":
        if computadora == "Piedra":
            print("¡Perdiste!")
        else:
            print("¡Ganaste!")
    
    # Preguntamos si el jugador desea continuar
    continuar = input("¿Deseas jugar de nuevo? (s/n): ")
    if continuar.lower() != "s":
        break

print("Gracias por jugar al Piedra, Papel o Tijeras.")