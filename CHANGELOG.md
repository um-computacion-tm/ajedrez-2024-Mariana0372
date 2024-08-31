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

#### **Versión 1.2 - 29/08/2024**


#### Nuevas Funcionalidades

- **Deshacer y Rehacer Movimientos**:
  - Se agregó un nuevo archivo `undo_redo.py` que implementa la funcionalidad de deshacer y rehacer movimientos utilizando dos pilas (historial y rehacer).
  - Métodos añadidos:
    - `push(board_copy)`: Guarda una copia del estado del tablero en la pila de deshacer.
    - `undo()`: Deshace el último movimiento y recupera el estado anterior del tablero.
    - `redo()`: Rehace el último movimiento deshecho y restaura el estado del tablero.

#### Actualizaciones en `chess.py`

- **Integración del Manejador de Deshacer/Rehacer**:
  - Se incorporó `UndoRedoManager` en la clase `Chess`
  - Métodos modificados:
    - `move(from_row, from_col, to_row, to_col)`: Ahora guarda el estado actual del tablero antes de realizar un movimiento
    - `undo()`: Recupera el estado anterior del tablero y cambia el turno
    - `redo()`: Restaura el estado deshecho del tablero y cambia el turno
  - Método nuevo:
    - `__convert_symbol_to_piece(symbol)`: Encapsulado para convertir un símbolo de pieza a un objeto de pieza

#### Actualizaciones en `tablero.py`

- **Método de Copia de Tablero**:
  - Se agregó el método `crear_copia()` en la clase `Board` para crear una copia profunda del estado del tablero. Esto es necesario para la funcionalidad de deshacer y rehacer.

#### Actualizaciones en `main.py`

- **Mejora de la Interfaz de Usuario**:
  - Se añadió un menú interactivo para elegir entre realizar un movimiento, deshacer un movimiento, rehacer un movimiento o salir del juego.
  - Manejo de errores mejorado para entradas inválidas, incluyendo manejo de excepciones para posiciones inválidas

#### **Versión 1.3 - 30/08/2024**

#### `chess.py`
- **Arreglos en `move`**: Corrección en la conversión de símbolos a piezas y en la lógica de actualización del tablero.
- **Simplificación de `print_board`**: Se eliminó la modificación del turno dentro del método de impresión.
- **Corrección en `__convert_symbol_to_piece`**: Ajuste para convertir correctamente los símbolos a objetos de pieza.

#### `movimientos.py`
- **`es_movimiento_valido`**: Se simplificó la validación de movimientos, eliminando parámetros innecesarios.
- **`convert_symbol_to_piece`**: Ajuste para la conversión de símbolos a piezas sin parámetros adicionales.

#### `undo_redo.py`
- **Correcciones en deshacer/rehacer**: Ajustes en el manejo de las pilas de deshacer y rehacer para una funcionalidad correcta.

#### `piezas.py`
- **Corrección en los métodos `mover`**: Ajustes en la lógica de movimiento para `Peon`, `Torre`, `Alfil`, `Reina`, y `Rey`.

#### `board.py`
- **Nuevo archivo**: Implementación del tablero y manejo inicial de piezas.

#### **Versión 1.4 - 31/08/2024**


### **Añadido**
- **Nuevo módulo para Redis**:
  - Se añadió `redis_storage.py` para gestionar el almacenamiento y recuperación del estado del juego usando Redis.
    - Funciones agregadas:
      - `guardar_partida(id_partida, estado_tablero)`: Guarda el estado del tablero en Redis.
      - `cargar_partida(id_partida)`: Carga el estado del tablero desde Redis.

### **Modificado**
- **Clase `Chess`**:
  - Se añadieron métodos para guardar y cargar partidas usando Redis:
    - `guardar_partida(id_partida)`: Guarda el estado del tablero en Redis.
    - `cargar_partida(id_partida)`: Carga el estado del tablero desde Redis y restaura el turno.
  - Integración con `redis_storage` para manejar el almacenamiento persistente del estado del juego.

- **Clase `Board`**:
  - Se añadieron métodos para serializar y deserializar el estado del tablero:
    - `obtener_estado_tablero()`: Devuelve el estado del tablero en formato dictado por el formato de serialización.
    - `establecer_estado_tablero(estado)`: Configura el tablero con el estado proporcionado.

- **Menú en `main.py`**:
  - Se añadieron opciones para guardar y cargar partidas:
    - Opción 4: Guardar partida en Redis.
    - Opción 5: Cargar partida desde Redis.
  - Se actualizaron las interacciones del menú para manejar el almacenamiento persistente del juego.

