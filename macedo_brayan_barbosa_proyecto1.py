# Número aleatorio que elige el ordenador, las funciones cerradas están terminadas.
def ordenador():
    import random
    return random.randint(0, 2)


def menu():
    print("Bienvenido al piedra, papel, tijera, lagarto o spock")
    print("El primero que llegue a 3 puntos, gana la partida.")
    print('''Escoge tu opción:
          0. Piedra
          1. Papel
          2. Tijera''')
        # 4. Lagarto 5. Spock

puntos_jugador = 0
puntos_ordenador = 0

# falta añadir el empate, lagarto y spock
def comparar_jugadas(num_ordenador, num_jugador, puntos_jugador, puntos_ordenador):
    if num_ordenador == 0 and num_jugador == 2:
        print("Victoria para ordenador")
        puntos_ordenador += 1 
    elif num_ordenador == 1 and num_jugador == 0:
        print("Victoria para ordenador")
        puntos_ordenador += 1
    elif num_ordenador == 2 and num_jugador == 1:
        print("Victoria para ordenador")
        puntos_ordenador += 1
    elif num_jugador == 0 and num_ordenador == 2:
        print("Victoria para jugador")
        puntos_ordenador += 1 
    elif num_jugador == 1 and num_ordenador == 0:
        print("Victoria para jugador")
        puntos_ordenador += 1
    elif num_jugador == 2 and num_ordenador == 1:
        print("Victoria para jugador")
        puntos_ordenador += 1


# falta añadir lagarto y spock a las funciones
def opcion_ordenador(num_ordenador):
    match num_ordenador:
        case 0:
            print("Ordenador eligió Piedra")
        case 1:
            print("Ordenador eligió Papel")
        case 2:
            print("Ordenador eligió Tijera")

def opcion_jugador(num_jugador):
    match num_jugador:
        case 0:
            print("Jugador eligió Piedra")
        case 1:
            print("Jugador eligió Papel")
        case 2:
            print("Jugador eligió Tijera")

menu()


while puntos_jugador < 3 or puntos_ordenador < 3:
        num_jugador = int(input("Elige tu opción: "))
        num_ordenador = ordenador()

        opcion_ordenador(num_ordenador)
        opcion_jugador(num_jugador)    
        comparar_jugadas(num_ordenador, num_jugador, puntos_jugador, puntos_ordenador)
        print("Recuento de puntos, Jugador:", puntos_jugador, "|", "Ordenador:", puntos_ordenador)

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