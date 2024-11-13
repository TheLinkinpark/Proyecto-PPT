from random import randint
from time import sleep
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

    print('''
Bienvenido/a al piedra, papel, tijera, lagarto o spock. Te haré una breve explicación de cómo funciona este juego.
Tienes 5 opciones para jugar, las cuales son las siguientes:''')
    sleep(1.3)
    print('''  
    1. Piedra | 2. Tijera | 3. Lagarto | 4. Papel | 5. Spock''')
    sleep(1.3)
    print('''
Estas 5 opciones están asociadas a un número, el cuál debes introducir para hacer la jugada que deseas.
Por ejemplo, si quieres usar "Tijera", tienes que introducir "2" (sin las comillas) cuando se te lo pida.
Jugarás contra el ordenador al mejor de 3, el primero que llegue a los 3 puntos, gana la partida.''')
    sleep(1.3)
    print('También dispones de 2 opciones  llamadas "opciones" y "reglas", las cuales te mostrarán el menú de opciones y las reglas del juego, respectivamente.')
    sleep(1.3)
    print('''
A continuación, te pregunto si quieres ver las reglas del juego antes de comenzar, si quieres escribe "s" y para lo contrario, "n". 
''')


def reglas() -> None:
    '''
    Muestra las reglas del juego
    '''
    print(''' 
Las reglas son muy simples, como ya mencionado en el menú inicial, el primero que consiga 3 puntos ganará la partida.
Cada una de las opciones sirve para ganar a otras 2, pero también serán vencidas por otras 2.
Aquí te muestro cómo funciona:''')
    sleep(1.5)
    print('''   
1. Piedra gana a:  lagarto | tijera.
2. Tijera gana a:  papel   | lagarto.
3. Papel gana a:   piedra  | spock.
4. Lagarto gana a: spock   | papel.
5. Spock gana a:   piedra  | tijera.

Por último, evidentemente existe la posibilidad del empate, si ocurre, no se otorgará ningún punto.''')
    

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

def menu_solo_opciones() -> None:
    '''
    Muestra un diferente menú para cuando el usuario comienza
    de nuevo una partida o pide que se vuelvan a mostrar las opciones.
    '''
    sleep(1)
    print('''
    Opciones:
        1. Piedra
        2. Tijera
        3. Lagarto
        4. Papel
        5. Spock''')



menu()


respuesta_reglas = input("¿Quieres ver las reglas del juego (s/n)? ")
respuesta_reglas = respuesta_reglas.lower()

while respuesta_reglas != "s" and respuesta_reglas != "n":
    respuesta_reglas = input("Has introducido un parámetro incorrecto, vuelve a intentarlo (s/n) ")


if respuesta_reglas == "s":
    reglas()
else:
    pass





respuesta_juego ="s"

while respuesta_juego == "s":

    puntos_jugador = 0
    puntos_ordenador = 0

    while puntos_jugador < 3 and puntos_ordenador < 3:

            print("\u2500" * 50)

            opcion_jugador = input("Elije tu opción: ")

            sleep(1.5)
            while opcion_jugador.isdigit() == False:
                opcion_jugador = opcion_jugador.lower()

                if opcion_jugador == "reglas": 
                    reglas()
                    print("\u2500" * 50)
                    opcion_jugador = input("Elije tu opción: ")

                if opcion_jugador == "opciones":
                    menu_solo_opciones()
                    print("\u2500" * 50)
                    opcion_jugador = input("Elije tu opción: ")

                
            if opcion_jugador.isdigit() == True:
                num_jugador = int(opcion_jugador)


            while num_jugador < 1 or num_jugador > 5:
                num_jugador = int(input("Has introducido un número incorrecto, vuelve a intentarlo: "))
                    

            num_ordenador = ordenador()

            print()
            print("Has elegido:", opcion(num_jugador), "\nEl ordenador ha elegido:", opcion(num_ordenador))
            print()
            sleep(1.5)
            partida = comparar_jugadas(num_ordenador, num_jugador)
            
            if partida == True:
                print("¡Punto para el ordenador!")
                puntos_ordenador += 1
            elif partida == False:
                print("¡Punto para ti!")
                puntos_jugador += 1
            else:
                print("Ha habido un empate, no se sumará ningún punto.")

           
            print("Recuento de puntos:\n", "Tú:", puntos_jugador, "|", "Ordenador:", puntos_ordenador)



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
        print("\u2500" * 50)
        print("¡El juego comenzará de nuevo!")
        print()
        menu_solo_opciones()

    else:
        print("Has escogido una opción incorrecta.")