import heapq

# Función de Búsqueda de Costo Uniforme
def uniform_cost_search(graph, start, goal):
    # Cola de prioridad para almacenar los nodos y sus costos
    queue = [(0, [start])]  # (Costo acumulado, camino)
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node in visited:
            continue

        if node == goal:
            return path, cost  # Retornar camino y costo

        visited.add(node)

        for neighbor, neighbor_cost in graph.get(node, []):
            new_cost = cost + neighbor_cost
            new_path = path + [neighbor]
            heapq.heappush(queue, (new_cost, new_path))

# Grafo con costos asociados (representa ciudades y costos de viaje)
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('D', 4), ('E', 6)],
    'C': [('A', 3), ('F', 8)],
    'D': [('B', 4)],
    'E': [('B', 6), ('F', 1)],
    'F': [('C', 8), ('E', 1)]
}

# Aplicación: Encontrar la ruta más barata de 'A' a 'F'
ruta, costo = uniform_cost_search(graph, 'A', 'F')
print(f"Ruta más barata de A a F: {ruta} con un costo de {costo}")
