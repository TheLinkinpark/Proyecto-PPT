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

def reglas():
    print(''' 
1. Piedra le gana a lagarto y a tijera
2. Tijera le gana a papel y a lagarto
3. Papel le gana a piedra y a spock
4. Lagarto le gana a spock y a papel
5. Spock le gana a piedra y a tijera''')
    
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
respuesta_reglas = input("¿Quieres ver las reglas del juego? (s/n)")
if respuesta_reglas == "s":
    reglas()
else:
    pass

respuesta ="s"
while respuesta != "n":

    puntos_jugador = 0
    puntos_ordenador = 0

    while puntos_jugador < 3 and puntos_ordenador < 3:
            print()
            num_jugador = int(input("Elige tu opción: "))

            while num_jugador != 0 and num_jugador != 1 and num_jugador != 2:
                num_jugador = int(input("Has elegido una opción incorrecta, vuelve a introducirla: "))
                print()
            
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
    
    respuesta = input("¿Quieres volver a jugar (s/n)? ")

# Añadir al juego:
# 1. Ordenador tramposo: hace trampas si va perdiendo
# 2. Lagarto, spock
# 3. Añadir un menú de reglas para el usuario. Al empezar la partida preguntar si quiere que se muestre dicho menú.
#    Si dice que no, directamente empieza el juego.

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