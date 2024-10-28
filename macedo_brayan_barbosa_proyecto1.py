puntos_jugador = 0
puntos_ordenador = 0

def jugada_ordenador():
    import random
    print("Opción ordenador: ", random.randint(0, 5))

def menu():
    print("Bienvenido al piedra, papel, tijera, lagarto o spock")
    print('''Escoge tu opción:
          1. Piedra
          2. Papel
          3. Tijera
          4. Lagarto
          5. Spock''')
    
menu()

num = int(input("Elige tu opción: "))
print("Opción jugador:", num)

jugada_ordenador()