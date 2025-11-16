# 8-Puzzle Solver

Solver del puzzle 8-Puzzle implementado en Python usando búsqueda en amplitud (BFS - Breadth-First Search).

## Descripción

Este proyecto resuelve el clásico problema del 8-Puzzle, un rompecabezas deslizante de 3x3 con 8 piezas numeradas y un espacio vacío. El objetivo es reorganizar las piezas desde un estado inicial hasta el estado meta mediante movimientos válidos.

## Características

- ✅ Resolución automática del 8-Puzzle usando búsqueda en amplitud
- ✅ Visualización interactiva del árbol de búsqueda con Plotly
- ✅ Código completamente comentado en español
- ✅ Muestra la secuencia completa de movimientos para llegar a la solución

## Requisitos

- Python 3.x
- plotly

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/LuisMatla/8puzzle.git
cd 8puzzle
```

2. Instala las dependencias:
```bash
pip install plotly
```

## Uso

Ejecuta el script:
```bash
python 8puzzle.py
```

El programa:
1. Muestra el estado inicial del puzzle
2. Busca la solución usando búsqueda en amplitud
3. Muestra la secuencia de movimientos necesarios
4. Abre una visualización interactiva del árbol de búsqueda en el navegador

## Ejemplo de Salida

```
estado inicial:
[1, ' ', 2]
[4, 5, 3]
[7, 8, 6]

buscando solucion.

solucion encontrada en 3 pasos.

secuencia de movimientos:

paso 0:
[1, ' ', 2]
[4, 5, 3]
[7, 8, 6]

paso 1:
[1, 2, ' ']
[4, 5, 3]
[7, 8, 6]

paso 2:
[1, 2, 3]
[4, 5, ' ']
[7, 8, 6]

paso 3:
[1, 2, 3]
[4, 5, 6]
[7, 8, ' ']
```

## Estructura del Código

- `Nodo`: Clase que representa un estado del puzzle
  - Generación de estados hijos (arriba, abajo, izquierda, derecha)
  - Verificación de estado meta
  - Búsqueda en amplitud

- `grafico()`: Función que genera la visualización interactiva del árbol de búsqueda

- `main()`: Función principal que ejecuta el solver

## Algoritmo

El programa utiliza **búsqueda en amplitud (BFS)** para encontrar la solución:
- Explora todos los nodos nivel por nivel
- Garantiza encontrar la solución óptima (menor número de movimientos)
- Evita estados repetidos usando una lista de visitados

## Visualización

La visualización muestra:
- Todos los nodos explorados durante la búsqueda
- El camino de la solución resaltado en verde
- Nodos no solución en azul claro
- Conexiones entre nodos padre e hijo

## Autor

Luis Matla

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

