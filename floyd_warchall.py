import numpy as np

INF = float('inf')

def floyd_warshall(graph):
# =============================================================================
# Nombre de sommets
# =============================================================================
    n = len(graph)
    
# =============================================================================
# Initialiser la distance avec les valeurs du graphe
# =============================================================================
    dist = np.array(graph, dtype=float)
    
    # Appliquer l'algorithme de Floyd-Warshall
    for k in range(n):
      for i in range(n):
        for j in range(n):
            if i == j:
                continue  # Ignorer les cases diagonales
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

   
# =============================================================================
#    detect cycle negatif 
# =============================================================================
    for i in range(n):
        if dist[i][i]<0:
            print(f"cycle negative dans noeuds ",i)
        else :
           print("no cycle negative",i)
    return dist

# Exemple de graphe (matrice d'adjacence)
graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

# Trouver les plus courts chemins
shortest_paths = floyd_warshall(graph)

# Afficher le résultat
print("Matrice des plus courts chemins entre tous les nœuds :")
print(shortest_paths)
