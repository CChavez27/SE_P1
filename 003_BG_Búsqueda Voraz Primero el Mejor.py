import heapq

# Función de Búsqueda Voraz Primero el Mejor
def greedy_best_first_search(graph, start, goal, heuristic):
    queue = [(heuristic[start], [start])]  # (Heurística, camino)
    visited = set()

    while queue:
        _, path = heapq.heappop(queue)
        node = path[-1]

        if node in visited:
            continue

        if node == goal:
            return path

        visited.add(node)

        for neighbor in graph.get(node, []):
            heapq.heappush(queue, (heuristic[neighbor], path + [neighbor]))

# Grafo y heurística para aproximar distancias (ejemplo de restaurantes)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Heurística que representa la distancia en línea recta a la meta (G)
heuristic = {
    'A': 5,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0  # El objetivo
}

# Aplicación: Buscar la ruta más prometedora hacia el restaurante 'F'
ruta = greedy_best_first_search(graph, 'A', 'F', heuristic)
print(f"Ruta hacia el restaurante F: {ruta}")
