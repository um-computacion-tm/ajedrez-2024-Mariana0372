from chess import Chess
from redis_storage import guardar_partida, cargar_partida

def mostrar_menu():
    print("\nOpciones:")
    print("1. Hacer movimiento")
    print("2. Deshacer movimiento")
    print("3. Rehacer movimiento")
    print("4. Guardar partida")
    print("5. Cargar partida")
    print("6. Salir")
    print("Ingrese su opción (1-6): ")

def main():
    # Crear una instancia del juego
    juego = Chess()

    while True:
        # Imprimir el estado del tablero
        juego.print_board()
        
        # Mostrar menú de opciones
        mostrar_menu()
        
        opcion = input().strip()
        
        if opcion == '1':
            # Solicitar que movimiento desea realizar
            from_pos = input(f"Turno de {juego.__turn}. Ingresa movimiento (ej. 'a2 a3'): ").strip().lower()
            try:
                from_col, from_row = ord(from_pos[0]) - ord('a'), 8 - int(from_pos[1])
                to_pos = input("Ingresa destino (ej. 'a3'): ").strip().lower()
                to_col, to_row = ord(to_pos[0]) - ord('a'), 8 - int(to_pos[1])
                # Intentar realizar el movimiento en el tablero
                juego.move(from_row, from_col, to_row, to_col)
            except (IndexError, ValueError):
                print("Error: Posición inválida. Asegúrate de ingresar la posición correctamente.")
        
        elif opcion == '2':
            # Deshacer movimiento
            juego.undo()
        
        elif opcion == '3':
            # Rehacer movimiento
            juego.redo()
        
        elif opcion == '4':
            # Guardar partida en Redis
            id_partida = input("Ingresa un ID para guardar la partida: ").strip()
            juego.guardar_partida(id_partida)
            print(f"Partida guardada con ID '{id_partida}' en Redis.")
        
        elif opcion == '5':
            # Cargar partida desde Redis
            id_partida = input("Ingresa el ID de la partida para cargar: ").strip()
            estado_tablero = cargar_partida(id_partida)
            if estado_tablero:
                juego.__board.establecer_estado_tablero(estado_tablero)  # Método para actualizar el tablero con el estado cargado
                print(f"Partida con ID '{id_partida}' cargada.")
            else:
                print(f"No se encontró ninguna partida con el ID '{id_partida}'.")
        
        elif opcion == '6':
            # Salir del juego
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 6.")

if __name__ == "__main__":
    main()

