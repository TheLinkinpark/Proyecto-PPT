def ordenador():
    import random
    return random.randint(0, 2)

# 4. Lagarto 5. Spock
def menu():
    print("Bienvenido al piedra, papel, tijera, lagarto o spock")
    print("El primero que llegue a 3 puntos, gana la partida.")
    print('''Escoge tu opción:
          0. Piedra
          1. Papel
          2. Tijera''')

# falta añadir lagarto y spock.
def comparar_jugadas(num_ordenador, num_jugador):
    victoria_ordenador = False
    if num_ordenador == 0 and num_jugador == 2:
        print("Victoria para ordenador")
        victoria_ordenador = True
        return victoria_ordenador
    elif num_ordenador == 1 and num_jugador == 0:
        print("Victoria para ordenador")
        victoria_ordenador = True
        return victoria_ordenador
    elif num_ordenador == 2 and num_jugador == 1:
        print("Victoria para ordenador")
        victoria_ordenador = True
        return victoria_ordenador
    elif num_jugador == 0 and num_ordenador == 2:
        print("Victoria para jugador")
        victoria_ordenador = False
        return victoria_ordenador
    elif num_jugador == 1 and num_ordenador == 0:
        print("Victoria para jugador")
        victoria_ordenador = False
        return victoria_ordenador
    elif num_jugador == 2 and num_ordenador == 1:
        print("Victoria para jugador")
        victoria_ordenador = False
        return victoria_ordenador
    elif num_jugador == 0 and num_ordenador == 0:
        print("Ha sido empate, no se otorgan puntos")
        victoria_ordenador = False
        return "empate"
    elif num_jugador == 1 and num_ordenador == 1:
        print("Ha sido empate, no se otorgan puntos")
        victoria_ordenador = False
        return "empate"
    elif num_jugador == 2 and num_ordenador == 2:
        print("Ha sido empate, no se otorgan puntos")
        victoria_ordenador = False
        return "empate"

# falta añadir lagarto y spock a la función
def opcion(numero):
    match numero:
        case 0:
            return "Piedra"
        case 1:
            return "Papel"
        case 2:
            return "Tijera"


menu()

puntos_jugador = 0
puntos_ordenador = 0

while puntos_jugador < 3 and puntos_ordenador < 3:
        print()
        num_jugador = int(input("Elige tu opción: "))
        num_ordenador = ordenador()

        print("Has elegido:", opcion(num_jugador), "\nEl ordenador ha elegido:", opcion(num_ordenador))
        print()

        partida = comparar_jugadas(num_ordenador, num_jugador)
        if partida == True:
            puntos_ordenador += 1
        elif partida == False:
            puntos_jugador += 1
        
        print("Recuento de puntos:\n", "Jugador:", puntos_jugador, "|", "Ordenador:", puntos_ordenador)

if puntos_jugador == 3:
    print("Has ganado la partida, ¡Felicidades!")
elif puntos_ordenador == 3:
    print("El ordenador ha ganado la partida, ¡Suerte en la próxima!")

# piedra > lagarto
# piedra > tijeras

# tijera > papel
# tijeras > lagarto

# papel > piedra
# papel > spock

# lagarto > spock
# lagarto > papel

# spock > piedra
# spock > tijeras