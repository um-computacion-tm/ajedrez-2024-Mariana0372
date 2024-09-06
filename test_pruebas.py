import unittest
import redis
import json

# Configuración de la conexión a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Función para guardar una partida
def guardar_partida(id_partida, estado_tablero):
    estado_json = json.dumps(estado_tablero)
    r.set(id_partida, estado_json)

# Función para cargar una partida
def cargar_partida(id_partida):
    estado_json = r.get(id_partida)
    if estado_json:
        return json.loads(estado_json)
    return None

# Clase de prueba
class TestRedisFunctions(unittest.TestCase):
    
    def setUp(self):
        # Se ejecuta antes de cada test
        self.id_partida = 'partida_123'
        self.estado_tablero = {
            'jugador1': {'pos': (1, 2), 'puntos': 10},
            'jugador2': {'pos': (2, 3), 'puntos': 20}
        }
        # Limpiar la base de datos de Redis antes de cada prueba
        r.flushdb()

    def test_guardar_partida(self):
        # Guardar la partida
        guardar_partida(self.id_partida, self.estado_tablero)
        # Verificar que se ha guardado
        estado_guardado = r.get(self.id_partida)
        self.assertIsNotNone(estado_guardado)
        estado_guardado = json.loads(estado_guardado)
        self.assertEqual(estado_guardado, self.estado_tablero)

    def test_cargar_partida(self):
        # Guardar la partida primero
        guardar_partida(self.id_partida, self.estado_tablero)
        # Cargar la partida
        estado_cargado = cargar_partida(self.id_partida)
        # Verificar que el estado cargado es correcto
        self.assertEqual(estado_cargado, self.estado_tablero)

    def tearDown(self):
        # Se ejecuta después de cada test
        r.flushdb()

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
