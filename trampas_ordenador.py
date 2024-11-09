def trampas_ordenador(num_jugador):
    match num_jugador-1:
        case 0:
            return 5
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 4
        case 4:
            return 3
        
puntos_jugador = 0
puntos_ordenador = 0


if puntos_jugador == 2 and puntos_ordenador == 0:
    num_jugador = int(input("Elige tu opción: "))
    num_ordenador = trampas_ordenador(num_jugador)
    print("El ordenador ha hecho trampas.")