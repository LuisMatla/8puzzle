#se importa la librería random para generar estados aleatorios.
import random
#se importa plotly para crear visualizaciones gráficas.
import plotly.graph_objects as go

#se inicializa la lista global de nodos visitados.
visitados = []

#se define la clase Nodo para representar estados del puzzle.
class Nodo:
    #se inicializa el nodo con un estado y su nodo padre.
    def __init__(self, dato=None, papa=None):
        #si no se proporciona un estado, se genera uno aleatorio.
        if dato is None:
            #se genera un estado inicial aleatorio.
            self.dato = self.generar_estado_inicial()
        else:
            #se asigna el estado proporcionado.
            self.dato = dato
        #se inicializa la lista de hijos del nodo.
        self.hijos = []
        #se guarda la referencia al nodo padre.
        self.papa = papa
        #se marca si este nodo forma parte de la solución.
        self.is_solution = False
        #se guarda el nivel del nodo en el árbol de búsqueda.
        self.level = 0
        #se guarda el identificador único del nodo.
        self._id = id(self)

    #se define el método hash para poder usar el nodo en conjuntos.
    def __hash__(self):
        #se retorna el hash de la tupla del estado.
        return hash(tuple(self.dato))

    #se define la igualdad entre nodos.
    def __eq__(self, inst):
        #se comparan los estados de los nodos.
        return self.dato == inst.dato

    #se define la representación en string del nodo.
    def __repr__(self):
        #se formatea el estado como una matriz 3x3.
        return f"{self.dato[0:3]}\n{self.dato[3:6]}\n{self.dato[6:9]}\n"

    #se genera un estado inicial aleatorio del puzzle.
    def generar_estado_inicial(self):
        #se crea el estado objetivo con los números ordenados.
        estado = [1, 2, 3, 4, 5, 6, 7, 8, ' ']
        #se mezclan aleatoriamente los elementos del estado.
        random.shuffle(estado)
        #se retorna el estado mezclado.
        return estado

    #se genera un hijo moviendo el espacio hacia arriba.
    def generar_hijo_arriba(self):
        #se encuentra la posición actual del espacio vacío.
        p_actual = self.dato.index(' ')
        #se verifica que el espacio no esté en la primera fila.
        if p_actual > 2:
            #se crea una copia del estado actual.
            hijo = self.dato[:]
            #se calcula la nueva posición del espacio (3 posiciones arriba).
            p_siguiente = p_actual - 3
            #se intercambian el espacio y el número de arriba.
            hijo[p_actual], hijo[p_siguiente] = hijo[p_siguiente], hijo[p_actual]
            #se crea un nuevo nodo con el estado modificado.
            nuevo_hijo = Nodo(hijo, self)
            #se incrementa el nivel del nuevo nodo.
            nuevo_hijo.level = self.level + 1
            #se agrega el nuevo hijo a la lista de hijos.
            self.hijos.append(nuevo_hijo)

    #se genera un hijo moviendo el espacio hacia abajo.
    def generar_hijo_abajo(self):
        #se encuentra la posición actual del espacio vacío.
        p_actual = self.dato.index(' ')
        #se verifica que el espacio no esté en la última fila.
        if p_actual <= 5:
            #se crea una copia del estado actual.
            hijo = self.dato[:]
            #se calcula la nueva posición del espacio (3 posiciones abajo).
            p_siguiente = p_actual + 3
            #se intercambian el espacio y el número de abajo.
            hijo[p_actual], hijo[p_siguiente] = hijo[p_siguiente], hijo[p_actual]
            #se crea un nuevo nodo con el estado modificado.
            nuevo_hijo = Nodo(hijo, self)
            #se incrementa el nivel del nuevo nodo.
            nuevo_hijo.level = self.level + 1
            #se agrega el nuevo hijo a la lista de hijos.
            self.hijos.append(nuevo_hijo)

    #se genera un hijo moviendo el espacio hacia la derecha.
    def generar_hijo_der(self):
        #se encuentra la posición actual del espacio vacío.
        p_actual = self.dato.index(' ')
        #se verifica que el espacio no esté en la última columna.
        if (p_actual % 3) != 2:
            #se crea una copia del estado actual.
            hijo = self.dato[:]
            #se calcula la nueva posición del espacio (1 posición a la derecha).
            p_siguiente = p_actual + 1
            #se intercambian el espacio y el número de la derecha.
            hijo[p_actual], hijo[p_siguiente] = hijo[p_siguiente], hijo[p_actual]
            #se crea un nuevo nodo con el estado modificado.
            nuevo_hijo = Nodo(hijo, self)
            #se incrementa el nivel del nuevo nodo.
            nuevo_hijo.level = self.level + 1
            #se agrega el nuevo hijo a la lista de hijos.
            self.hijos.append(nuevo_hijo)

    #se genera un hijo moviendo el espacio hacia la izquierda.
    def generar_hijo_izq(self):
        #se encuentra la posición actual del espacio vacío.
        p_actual = self.dato.index(' ')
        #se verifica que el espacio no esté en la primera columna.
        if (p_actual % 3) != 0:
            #se crea una copia del estado actual.
            hijo = self.dato[:]
            #se calcula la nueva posición del espacio (1 posición a la izquierda).
            p_siguiente = p_actual - 1
            #se intercambian el espacio y el número de la izquierda.
            hijo[p_actual], hijo[p_siguiente] = hijo[p_siguiente], hijo[p_actual]
            #se crea un nuevo nodo con el estado modificado.
            nuevo_hijo = Nodo(hijo, self)
            #se incrementa el nivel del nuevo nodo.
            nuevo_hijo.level = self.level + 1
            #se agrega el nuevo hijo a la lista de hijos.
            self.hijos.append(nuevo_hijo)

    #se generan todos los hijos posibles del nodo.
    def generar_hijos(self):
        #se intenta generar un hijo moviendo hacia arriba.
        self.generar_hijo_arriba()
        #se intenta generar un hijo moviendo hacia abajo.
        self.generar_hijo_abajo()
        #se intenta generar un hijo moviendo hacia la derecha.
        self.generar_hijo_der()
        #se intenta generar un hijo moviendo hacia la izquierda.
        self.generar_hijo_izq()

    #se verifica si el nodo es el estado meta.
    def es_meta(self, meta):
        #se compara el estado actual con el estado meta.
        return self.dato == meta

    #se convierte el estado a una representación en string.
    def state_to_string(self):
        #se formatea el estado como una matriz 3x3 con guiones bajos para espacios.
        return '\n'.join(
            #se une cada fila de 3 elementos en un string.
            ''.join(str(x) if x != ' ' else '_' for x in self.dato[i:i+3]) for i in range(0, 9, 3)
        )

    #se realiza la búsqueda en amplitud (breadth-first search).
    def busqueda_pa(self, meta):
        #se declara la variable global visitados.
        global visitados
        #se inicializa la lista de nodos visitados.
        visitados = []
        #se verifica si el nodo inicial es la meta.
        if self.es_meta(meta):
            #se marca el nodo como parte de la solución.
            self.is_solution = True
            #se agrega el nodo a la lista de visitados.
            visitados.append(self)
            #se retorna el nodo como solución.
            return [self]
        #se inicializa la cola de nodos por visitar con el nodo inicial.
        por_visitar = [self]
        #se agrega el nodo inicial a la lista de visitados.
        visitados.append(self)
        #se itera mientras haya nodos por visitar.
        while por_visitar:
            #se extrae el primer nodo de la cola (FIFO).
            nodo_actual = por_visitar.pop(0)
            #se generan todos los hijos posibles del nodo actual.
            nodo_actual.generar_hijos()
            #se itera sobre cada hijo generado.
            for hijo in nodo_actual.hijos:
                #se verifica si el hijo es el estado meta.
                if hijo.es_meta(meta):
                    #se marca el hijo como parte de la solución.
                    hijo.is_solution = True
                    #se obtiene el nodo padre del hijo.
                    nodo = hijo.papa
                    #se marca todos los ancestros como parte de la solución.
                    while nodo is not None:
                        #se marca el nodo como parte de la solución.
                        nodo.is_solution = True
                        #se avanza al nodo padre.
                        nodo = nodo.papa
                    #se verifica si el hijo no está en visitados.
                    if hijo not in visitados:
                        #se agrega el hijo a la lista de visitados.
                        visitados.append(hijo)
                    #se inicia la construcción del camino desde el hijo.
                    camino = [hijo]
                    #se obtiene el nodo padre del hijo.
                    nodo = hijo.papa
                    #se construye el camino completo hasta la raíz.
                    while nodo is not None:
                        #se agrega el nodo al camino.
                        camino.append(nodo)
                        #se avanza al nodo padre.
                        nodo = nodo.papa
                    #se invierte el camino para que vaya de raíz a meta.
                    camino.reverse()
                    #se retorna el camino completo de la solución.
                    return camino
                #se verifica si el hijo no ha sido visitado.
                if hijo not in visitados:
                    #se agrega el hijo a la lista de visitados.
                    visitados.append(hijo)
                    #se agrega el hijo a la cola de nodos por visitar.
                    por_visitar.append(hijo)
        #se retorna None si no se encontró solución.
        return None

#se crea la función para generar el gráfico del árbol de búsqueda.
def grafico(solution_path):
    #se crea un diccionario de nodos por nivel.
    nodos = {}
    #se itera sobre todos los nodos visitados.
    for node in visitados:
        #se verifica si el nivel no existe en el diccionario.
        if node.level not in nodos:
            #se crea una lista vacía para ese nivel.
            nodos[node.level] = []
        #se agrega el nodo a su nivel correspondiente.
        nodos[node.level].append(node)

    #crea listas para la visualización.
    #se crea la lista de coordenadas x de los nodos.
    nodox = []
    #se crea la lista de coordenadas y de los nodos.
    nodoy = []
    #se crea la lista de textos para cada nodo.
    texto = []
    #se crea la lista de coordenadas x de los bordes.
    bordex = []
    #se crea la lista de coordenadas y de los bordes.
    bordey = []
    #se crea la lista de colores para cada nodo.
    colores = []

    #se posicionan nodos por nivel.
    #guarda las posiciones de los nodos.
    pos_dict = {}
    #se encuentra el número máximo de nodos en un nivel.
    nodosmax = max(len(nodo) for nodo in nodos.values())
    #se itera sobre los niveles ordenados.
    for level in sorted(nodos.keys()):
        #se obtienen los nodos del nivel actual.
        nodo = nodos[level]
        #se calcula el ancho total del nivel.
        width = nodosmax * 2
        #se calcula el espaciado entre nodos.
        spacing = width / (len(nodo) + 1)
        #se itera sobre cada nodo del nivel.
        for i, node in enumerate(nodo):
            #se calcula la coordenada x del nodo.
            x = (i + 1) * spacing - width/2
            #se calcula la coordenada y del nodo (negativa para mostrar arriba).
            y = -level
            #guarda la posición del nodo.
            pos_dict[hash(node)] = (x, y)
            #agrega nodo a las listas de visualización.
            #se agrega la coordenada x del nodo.
            nodox.append(x)
            #se agrega la coordenada y del nodo.
            nodoy.append(y)
            #se agrega el texto del estado del nodo.
            texto.append(node.state_to_string())
            #se agrega el color según si es parte de la solución o no.
            colores.append('lightgreen' if node.is_solution else 'lightblue')
            #agrega bordes si tiene padre.
            #se verifica si el nodo tiene un padre.
            if node.papa is not None:
                #se obtienen las coordenadas del nodo padre.
                parent_x, parent_y = pos_dict[hash(node.papa)]
                #se agregan las coordenadas del borde (con None para separar líneas).
                bordex.extend([x, parent_x, None])
                #se agregan las coordenadas del borde (con None para separar líneas).
                bordey.extend([y, parent_y, None])
    #crea los trazos.
    #se crea el trazo para las líneas que conectan los nodos.
    trazo = go.Scatter(
        #se asignan las coordenadas x de los bordes.
        x=bordex, 
        #se asignan las coordenadas y de los bordes.
        y=bordey,
        #se configura el estilo de la línea.
        line=dict(width=1, color='#888'),
        #se desactiva la información al pasar el mouse.
        hoverinfo='none',
        #se establece el modo de visualización como líneas.
        mode='lines'
    )
    #se crea el trazo para los nodos.
    nodotrazo = go.Scatter(
        #se asignan las coordenadas x de los nodos.
        x=nodox, 
        #se asignan las coordenadas y de los nodos.
        y=nodoy,
        #se establece el modo de visualización como marcadores y texto.
        mode='markers+text',
        #se muestra información al pasar el mouse.
        hoverinfo='text',
        #se asigna el texto a mostrar en cada nodo.
        text=texto,
        #se establece la posición del texto.
        textposition="middle right",
        #se configura el estilo de los marcadores.
        marker=dict(
            #se establece el tamaño de los marcadores.
            size=30,
            #se asignan los colores de los marcadores.
            color=colores,
            #se configura el borde de los marcadores.
            line=dict(width=2, color='DarkSlateGrey')
        )
    )
    #crea la figura.
    #se crea la figura con los trazos y el layout.
    fig = go.Figure(data=[trazo, nodotrazo],
                    #se configura el layout de la figura.
                    layout=go.Layout(
                        #se establece el título de la figura.
                        title="8-Puzzle.",
                        #se oculta la leyenda.
                        showlegend=False,
                        #se establece el modo de hover.
                        hovermode='closest',
                        #se configuran los márgenes de la figura.
                        margin=dict(b=20, l=5, r=5, t=40),
                        #se configura el eje x.
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        #se configura el eje y.
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                    ))
    #se retorna la figura creada.
    return fig

#se define la función principal del programa.
def main():
    # Estado inicial y meta
    #se define el estado inicial del puzzle.
    initial_state = [1, ' ', 2, 4, 5, 3, 7, 8, 6]
    #se define el estado meta (objetivo) del puzzle.
    meta = [1, 2, 3, 4, 5, 6, 7, 8, ' ']
    #se imprime el mensaje de estado inicial.
    print("estado inicial:")
    #se crea el nodo raíz con el estado inicial.
    root = Nodo(initial_state)
    #se imprime el estado inicial.
    print(root)
    #se imprime el mensaje de búsqueda.
    print("\nbuscando solucion.")
    #se realiza la búsqueda en amplitud para encontrar la solución.
    solucion = root.busqueda_pa(meta)
    #se verifica si se encontró una solución.
    if solucion:
        #se imprime el número de pasos de la solución.
        print(f"\nsolucion encontrada en {len(solucion)-1} pasos.")
        #se imprime el mensaje de secuencia de movimientos.
        print("\nsecuencia de movimientos:")
        #se itera sobre cada paso de la solución.
        for i, node in enumerate(solucion):
            #se imprime el número de paso.
            print(f"\npaso {i}:")
            #se imprime el estado del nodo en ese paso.
            print(node)
        
        #visualiza la solucion
        #se genera el gráfico del árbol de búsqueda.
        fig = grafico(solucion)
        #se muestra el gráfico en el navegador.
        fig.show()
    else:
        #se imprime el mensaje si no se encontró solución.
        print("\nno se encontro solucion.")

#se verifica si el script se está ejecutando directamente.
if __name__ == '__main__':
    #se llama a la función principal.
    main()