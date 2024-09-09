from chess import Chess
from redis_storage import guardar_partida, cargar_partida

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nOpciones:")
    print("1. Hacer movimiento")
    print("2. Deshacer movimiento")
    print("3. Rehacer movimiento")
    print("4. Guardar partida")
    print("5. Cargar partida")
    print("6. Salir")
    print("Ingrese su opción (1-6): ")

def realizar_movimiento(juego):
    """Solicita al usuario que haga un movimiento y lo ejecuta en el juego."""
    from_pos = input(f"Turno de {juego.__turn}. Ingresa movimiento (ej. 'a2 a3'): ").strip().lower()
    if not validar_posicion(from_pos):
        print("Error: Posición de origen inválida.")
        return
    
    to_pos = input("Ingresa destino (ej. 'a3'): ").strip().lower()
    if not validar_posicion(to_pos):
        print("Error: Posición de destino inválida.")
        return

    try:
        from_col, from_row = convertir_a_indices(from_pos)
        to_col, to_row = convertir_a_indices(to_pos)
        juego.move(from_row, from_col, to_row, to_col)
    except Exception as e:
        print(f"Error al realizar el movimiento: {e}")

def validar_posicion(pos):
    """Valida si la posición ingresada es correcta."""
    return len(pos) == 2 and pos[0] in 'abcdefgh' and pos[1] in '12345678'

def convertir_a_indices(pos):
    """Convierte una posición en formato 'a2' a índices de fila y columna."""
    col, row = pos
    return ord(col) - ord('a'), 8 - int(row)

def guardar_partida_en_redis(juego):
    """Solicita un ID y guarda la partida en Redis."""
    id_partida = input("Ingresa un ID para guardar la partida: ").strip()
    guardar_partida(id_partida, juego.obtener_estado())
    print(f"Partida guardada con ID '{id_partida}' en Redis.")

def cargar_partida_de_redis(juego):
    """Solicita un ID y carga la partida desde Redis."""
    id_partida = input("Ingresa el ID de la partida para cargar: ").strip()
    estado_tablero = cargar_partida(id_partida)
    if estado_tablero:
        juego.__board.establecer_estado_tablero(estado_tablero)
        print(f"Partida con ID '{id_partida}' cargada.")
    else:
        print(f"No se encontró ninguna partida con el ID '{id_partida}'.")

def main():
    """Función principal para ejecutar el juego de ajedrez."""
    juego = Chess()

    while True:
        juego.print_board()
        mostrar_menu()

        opcion = input().strip()
        
        if opcion == '1':
            realizar_movimiento(juego)
        
        elif opcion == '2':
            juego.undo()
        
        elif opcion == '3':
            juego.redo()
        
        elif opcion == '4':
            guardar_partida_en_redis(juego)
        
        elif opcion == '5':
            cargar_partida_de_redis(juego)
        
        elif opcion == '6':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 6.")

if __name__ == "__main__":
    main()

