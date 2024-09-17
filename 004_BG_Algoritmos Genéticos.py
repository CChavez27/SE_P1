import random

# Función para crear una población inicial
def create_population(size, gene_pool, length):
    return [[random.choice(gene_pool) for _ in range(length)] for _ in range(size)]

# Función de evaluación de aptitud (fitness)
def fitness(individual, goal):
    return sum(1 for i, g in zip(individual, goal) if i == g)

# Función de cruce (crossover)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

# Función de mutación
def mutate(individual, gene_pool):
    index = random.randint(0, len(individual) - 1)
    individual[index] = random.choice(gene_pool)

# Algoritmo genético
def genetic_algorithm(gene_pool, goal, population_size, generations):
    population = create_population(population_size, gene_pool, len(goal))

    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x, goal), reverse=True)

        if fitness(population[0], goal) == len(goal):
            return population[0], generation

        next_generation = population[:2]

        for _ in range(population_size - 2):
            parent1, parent2 = random.sample(population[:10], 2)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:  # Probabilidad de mutación
                mutate(child, gene_pool)
            next_generation.append(child)

        population = next_generation

# Ejemplo: Optimizar una combinación de caracteres
gene_pool = 'abcdefghijklmnopqrstuvwxyz '
goal = 'hello world'
population_size = 100
generations = 1000

# Aplicación: Encontrar la combinación de caracteres que más se acerque a 'hello world'
mejor_solucion, generacion = genetic_algorithm(gene_pool, goal, population_size, generations)
print(f"Solución encontrada: {mejor_solucion} en la generación {generacion}")
