

import numpy as np
from concurrent.futures import ThreadPoolExecutor

INF = float('inf')


def floyd_warshall_parallel(graph):
    n = len(graph)
    dist = graph.copy()

    def update_row(i, k):
        for j in range(n):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for k in range(n):
        with ThreadPoolExecutor() as executor:
            executor.map(lambda i: update_row(i, k), range(n))

    return dist

# Exemple de graphe (matrice d'adjacence)
graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

# Trouver les plus courts chemins
shortest_paths = floyd_warshall_parallel(graph)

# Afficher le résultat
print("Matrice des plus courts chemins entre tous les nœuds :")
print(shortest_paths)
