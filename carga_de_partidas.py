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
