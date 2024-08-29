#### **Versión 1.1 - 28/08/2024**

##### **1. Reestructuración del Proyecto**

- **Organización en Módulos:**
  - **`tablero.py`**: Introducido para manejar la representación del tablero y la colocación de piezas.
  - **`piezas.py`**: Creado para definir las clases de piezas y sus movimientos.
  - **`movimientos_validacion.py`**: Añadido para validar los movimientos y convertir los símbolos en objetos de pieza.
  - **`chess.py`**: Modificado para integrar la lógica del juego con los nuevos módulos.
  - **`main.py`**: Implementado para la interacción con el usuario y para ejecutar el juego.

##### **2. **Archivo `tablero.py`**

- **Nueva Clase `Board`:**
  - **Método `crear_tablero`**: Configura el tablero con las piezas blancas y negras en sus posiciones iniciales.
  - **Método `get_piece`**: Obtiene el símbolo de una pieza en una posición específica.
  - **Método `set_piece`**: Coloca una pieza en una posición específica.
  - **Método `imprimir_tablero`**: Imprime el tablero en formato legible para el usuario.

##### **3. **Archivo `piezas.py`**

- **Clases de Piezas:**
  - **`Pieza`**: Clase base para todas las piezas.
  - **`Peon`, `Torre`, `Caballo`, `Alfil`, `Reina`, `Rey`**: Clases derivadas de `Pieza` que implementan la lógica de movimiento específica para cada tipo de pieza.

##### **4. **Archivo `movimiento_validacion.py`**

- **Función `es_movimiento_valido`**:
  - Utiliza las clases de piezas para validar los movimientos de acuerdo con las reglas del ajedrez.
- **Función `convert_symbol_to_piece`**:
  - Convierte el símbolo de una pieza en un objeto de la clase correspondiente.

##### **5. **Archivo `chess.py`**

- **Clase `Chess`:**
  - **Método `move`**: Realiza un movimiento si es válido, utilizando la validación de movimientos.
  - **Método `convert_symbol_to_piece`**: Convierte el símbolo de una pieza en un objeto de la clase correspondiente.
  - **Método `change_turn`**: Cambia el turno entre los jugadores.
  - **Método `print_board`**: Imprime el tablero actual.

##### **6. **Archivo `main.py`**

- **Función `main`**:
  - Permite la interacción del usuario para mover piezas y muestra el tablero en cada turno.
  - Lee las entradas del usuario, convierte las posiciones, y llama al método `move` para realizar el movimiento.
