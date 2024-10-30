puntos_jugador = 0
puntos_ordenador = 0

# Número aleatorio que elige el ordenador, las funciones cerradas están terminadas.
def ordenador():
    import random
    return random.randint(0, 2)


def menu():
    print("Bienvenido al piedra, papel, tijera, lagarto o spock")
    print('''Escoge tu opción:
          0. Piedra
          1. Papel
          2. Tijera''')
        # 4. Lagarto 5. Spock
    
def comparar_jugadas(opcion_ordenador, jugada_jugador):
    if opcion_ordenador == 0 and jugada_jugador == 3:
        print("Victoria para ordenador") 

num_ordenador = ordenador()

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
num_jugador = int(input("Elige tu opción: "))


opcion_ordenador(num_ordenador)
opcion_jugador(num_jugador)




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