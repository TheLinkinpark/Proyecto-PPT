from random import randint
def ordenador() -> int:
    '''
    Función que genera un número aleatorio
    entre 1 y 5 (incluídos).
    '''

    return randint(1, 5)

def menu() -> None:
    '''
    Muestra el menú del juego
    '''
    print("Bienvenido al piedra, papel, tijera, lagarto o spock.")
    print("El primero que llegue a 3 puntos, gana la partida.")
    print('''Opciones:
          1. Piedra
          2. Tijera
          3. Lagarto
          4. Papel
          5. Spock''')

def reglas() -> None:
    '''
    Muestra las reglas del juego
    '''
    print("\u2500" * 50, ''' 
Cada opción le gana a otras dos:
          
1. Piedra le gana a lagarto y a tijera.
2. Tijera le gana a papel y a lagarto.
3. Papel le gana a piedra y a spock.
4. Lagarto le gana a spock y a papel.
5. Spock le gana a piedra y a tijera.''')
    

def comparar_jugadas(num_ordenador: int, num_jugador:int) -> bool | str:
    """
    Compara las jugadas.

    Devuelve True si gana el jugador, False si gana ordenador.\n
    Si es un empate, devuelve "empate".
    """
    if num_ordenador == num_jugador:
        return "empate"
    elif num_ordenador == (num_jugador +1) % 5 or num_ordenador == (num_jugador + 2) % 5: # Devuelve True si gana el jugador, False si gana ordenador.
        return False
    return True

def opcion(numero: int) -> str:
    '''
    Función que recibe el número
    elegido por el usuario y el ordenador.

    Devuelve un string de la opción elegida: piedra, papel...
    '''
    match numero-1:
        case 0:
            return "Piedra"
        case 1:
            return "Tijera"
        case 2:
            return "Lagarto"
        case 3:
            return "Papel"
        case 4:
            return "Spock"
        case _:
            return "Valor incorrecto"


# COSAS A ARREGLAR:
# DENTRO DE LA PARTIDA: 
    # Cuando se pide al usuario introducir su opción, si introduce una cadena de caracteres, sale como "syntax error". Sería
    # modificarlo para que aparezca el mensaje de error personalizado para que vuelva a introducir la opción. 


menu()

# REGLAS: Antes de comenzar la partida, se le pregunta al usuario si quiere ver las reglas del juego.
# Esta pregunta sólo se hará antes de comenzar la primera partida,
# si el usuario comienza una nueva partida sin terminar el bucle, comienza el juego directamente.

respuesta_reglas = input("¿Quiere ver las reglas del juego (s/n)? ")
respuesta_reglas = respuesta_reglas.lower()

while respuesta_reglas != "s" and respuesta_reglas != "n":
    respuesta_reglas = input("Has introducido un parámetro incorrecto, vuelve a intentarlo (s/n) ")


if respuesta_reglas == "s":
    reglas()
else:
    pass


# PARTIDA: Se realiza la partida con el recuento de puntos, cuando uno de los 2 llega a 3 puntos, termina.
# Al terminar, se pregunta al usuario si quier volver a jugar, si dice sí, se reinicia el programa.
# Si dice que no, se cierra el programa.


respuesta_juego ="s"

while respuesta_juego == "s":

    puntos_jugador = 0
    puntos_ordenador = 0

    while puntos_jugador < 3 and puntos_ordenador < 3:

            print("\u2500" * 50)
            num_jugador = int(input("Elige tu opción: "))

            while num_jugador < 1 or num_jugador > 5:
                num_jugador = int(input("Has elegido una opción incorrecta, vuelve a introducirla: "))
            
            num_ordenador = ordenador()
            print()
            print("Has elegido:", opcion(num_jugador), "\nEl ordenador ha elegido:", opcion(num_ordenador))
            print()

            partida = comparar_jugadas(num_ordenador, num_jugador)
            
            if partida == True:
                print("¡Punto para el ordenador!")
                puntos_ordenador += 1
            elif partida == False:
                print("¡Punto para ti!")
                puntos_jugador += 1
            else:
                print("Ha habido un empate, no se sumará ningún punto.")
            
            print("Recuento de puntos:\n", "Jugador:", puntos_jugador, "|", "Ordenador:", puntos_ordenador)

    if puntos_jugador == 3:
        print("\u2500" * 50)
        print('''\nHas ganado la partida, ¡Felicidades!''')
    elif puntos_ordenador == 3:
        print("\u2500" * 50)
        print('''\nEl ordenador ha ganado la partida, ¡Suerte en la próxima!''')
    
    respuesta_juego = input("¿Quieres volver a jugar (s/n)? ")
    respuesta_juego = respuesta_juego.lower()

    if respuesta_juego == "n":
        print("¡Adiós!")
    elif respuesta_juego == "s":
        print("¡El juego comenzará de nuevo!")
    else:
        print("Has escogido una opción incorrecta.")