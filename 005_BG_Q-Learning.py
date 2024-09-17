import numpy as np

# Parámetros de Q-learning
learning_rate = 0.8
discount_factor = 0.95
epsilon = 0.1  # Exploración

# Función de Q-learning
def q_learning(env, episodes):
    q_table = np.zeros((env.observation_space.n, env.action_space.n))

    for _ in range(episodes):
        state = env.reset()
        done = False

        while not done:
            if np.random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()  # Explorar
            else:
                action = np.argmax(q_table[state, :])  # Explotar

            new_state, reward, done, _ = env.step(action)

            # Actualización de la tabla Q
            q_table[state, action] = q_table[state, action] + learning_rate * (
                reward + discount_factor * np.max(q_table[new_state, :]) - q_table[state, action]
            )

            state = new_state

    return q_table

# Aplicación: Simular y entrenar un robot en un entorno sencillo
# Esta sección depende de un entorno como OpenAI Gym para funcionar
# No se incluye un entorno aquí, pero el código ilustra la idea básica
