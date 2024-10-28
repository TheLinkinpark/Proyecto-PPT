puntos_jugador = 0
puntos_ordenador = 0

def ordenador():
    import random
    print(random.randint(0, 4))


def menu():
    print("Bienvenido al piedra, papel, tijera, lagarto o spock")
    print('''Escoge tu opción:
          1. Piedra
          2. Papel
          3. Tijera
          4. Lagarto
          5. Spock''')
    
def comparar_jugadas(opcion_ordenador, jugada_jugador):
    if opcion_ordenador == 0 and jugada_jugador == 3:
        print("Victoria para ordenador") 

    
menu()

jugada_jugador = int(input("Elige tu opción: "))



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