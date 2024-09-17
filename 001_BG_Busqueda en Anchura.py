from collections import deque

# Función de Búsqueda en Anchura (BFS)
def bfs(graph, start, goal):
    # Cola para almacenar los nodos por explorar (FIFO)
    queue = deque([[start]])
    visited = set()  # Conjunto para almacenar nodos visitados

    while queue:
        path = queue.popleft()  # Obtener la ruta desde la cola
        node = path[-1]  # Último nodo de la ruta

        # Si el nodo ya ha sido visitado, se ignora
        if node in visited:
            continue

        # Si hemos llegado al nodo objetivo, retornamos la ruta
        if node == goal:
            return path

        visited.add(node)  # Marcar el nodo como visitado

        # Expandir nodos vecinos
        for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

# Ejemplo de un grafo para representar estaciones de metro
graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'F'],
    'C': ['A', 'G'],
    'D': ['B'],
    'E': ['A', 'F'],
    'F': ['B', 'E'],
    'G': ['C']
}

# Aplicación: Encontrar la ruta más corta desde 'A' a 'G' (inicio y meta)
ruta = bfs(graph, 'A', 'G')
print(f"Ruta más corta de A a G: {ruta}")
