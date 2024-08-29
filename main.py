
from chess import Chess

def main():
    #crea una instancia del juego
    juego = Chess()

    while True:
        #imprimir el estado del tablero
        juego.print_board()
        #solicitar que movimiento desea realizar
        from_pos = input(f"Turno de {juego.turn}. Ingresa movimiento (ej. 'a2 a3'): ")
        #convertir la posicion origen de columa-fila a columna y fila
        from_col, from_row = ord(from_pos[0]) - ord('a'), 8 - int(from_pos[1])
        #solicitar la posicion destino
        to_pos = input("Ingresa destino (ej. 'a3'): ")
        #convertir la posicion destino de formato colum-fila a columna y fila
        to_col, to_row = ord(to_pos[0]) - ord('a'), 8 - int(to_pos[1])
        #intentar relaizar el movimiento en el tablero
        juego.move(from_row, from_col, to_row, to_col)
#entrada del programa
if __name__ == "__main__":
    main()
