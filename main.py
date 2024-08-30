from chess import Chess

def mostrar_menu():
    print("\nOpciones:")
    print("1. Hacer movimiento")
    print("2. Deshacer movimiento")
    print("3. Rehacer movimiento")
    print("4. Salir")
    print("Ingrese su opción (1-4): ")

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
            # Salir del juego
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 4.")

if __name__ == "__main__":
    main()

