from src.othello import modificar_tablero

def test_modificar_tablero():
  # Abajo
  tablero_0 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  modificar_tablero(tablero_0, (2, 3), 2, (1, 0))
  assert tablero_1 == tablero_0

  # Derecha
  tablero_0 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 0, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  modificar_tablero(tablero_0, (4, 2), 1, (0, 1))
  assert tablero_1 == tablero_0

  # Arriba
  tablero_0 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 1, 2, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
  modificar_tablero(tablero_0, (5, 3), 2, (-1, 0))
  assert tablero_1 == tablero_0

  # Izquierda
  tablero_0 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 1, 2, 1, 0, 0, 0],
               [0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 1, 2, 2, 0, 0, 0],
               [0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  modificar_tablero(tablero_0, (4, 5), 2, (0, -1))
  assert tablero_1 == tablero_0

  # Diagonal arriba derecha
  tablero_0 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 1, 2, 2, 2, 0, 0],
               [0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 1, 1, 2, 2, 0, 0],
               [0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  modificar_tablero(tablero_0, (5, 2), 1, (-1, 1))
  assert tablero_1 == tablero_0

  # Diagonal abajo izquierda
  tablero_0 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 1, 1, 2, 2, 0, 0],
               [0, 0, 1, 2, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 1, 1, 2, 2, 0, 0],
               [0, 0, 1, 2, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  modificar_tablero(tablero_0, (1, 5), 2, (1, -1))
  assert tablero_1 == tablero_0

  # Diagonal arriba izquierda
  tablero_0 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 1, 1, 1, 2, 0, 0],
               [0, 0, 1, 2, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 1, 1, 1, 2, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  modificar_tablero(tablero_0, (6, 4), 1, (-1, -1))
  assert tablero_1 == tablero_0

  # Diagonal abajo derecha
  tablero_0 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 2, 2, 2, 2, 2, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 2, 2, 2, 2, 2, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

  modificar_tablero(tablero_0, (1, 2), 1, (1, 1))
  assert tablero_1 == tablero_0