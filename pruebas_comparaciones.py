def comparar_jugadas(num_ordenador, num_jugador):
    """
    Compara dos jugadas y devuelve el resultado.

    Args:
        num_ordenador (int): Jugada del ordenador.
        num_jugador (int): Jugada del jugador.

    Returns:
        str: 'empate' si ambos números son iguales, 'True' si gana el jugador, 'False' si gana el ordenador.


    >>> comparar_jugadas(0, 1)
    True
    >>> comparar_jugadas(0, 2)
    True
    >>> comparar_jugadas(0, 3)
    False
    >>> comparar_jugadas(0, 4)
    False

    >>> comparar_jugadas(1, 0)
    False
    >>> comparar_jugadas(1, 2)
    True
    >>> comparar_jugadas(1, 3)
    True
    >>> comparar_jugadas(1, 4)
    False
    
    >>> comparar_jugadas(2, 0)
    False
    >>> comparar_jugadas(2, 1)
    False
    >>> comparar_jugadas(2, 3)
    True
    >>> comparar_jugadas(2, 4)
    True

    >>> comparar_jugadas(3, 0)
    True
    >>> comparar_jugadas(3, 1)
    False
    >>> comparar_jugadas(3, 2)
    False
    >>> comparar_jugadas(3, 4)
    True

    >>> comparar_jugadas(4, 0)
    True
    >>> comparar_jugadas(4, 1)
    True
    >>> comparar_jugadas(4, 2)
    False
    >>> comparar_jugadas(4, 3)
    False

    """
    if num_ordenador == num_jugador:
        return "empate"
    elif num_ordenador == (num_jugador + 1) % 5 or num_ordenador == (num_jugador + 2) % 5:
        return False
    return True
