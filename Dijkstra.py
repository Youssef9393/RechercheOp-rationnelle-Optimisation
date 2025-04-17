import heapq

# mise a jour des poids a des valeur positifs
def redimension_poids(graph):
    min_weight = min(w for edges in graph.values() for w in edges.values())

    if min_weight < 0:
        offset = abs(min_weight) + 1
        for u in graph:
            for v in graph[u]:
                graph[u][v] += offset

    return graph
    
# creation d'un graphe 
def graph():
    graph = {}
    n = int(input("Entrez le nombre de nœuds : "))

    for i in range(n):
        v = input(f"Saisir le sommet {i+1} : ")
        graph[v] = {}  

        nbr = int(input(f"Combien de voisins pour {v} ? "))
        
        for j in range(nbr):
            key = input(f"Saisir le voisin {j+1} de {v}: ")
            valeur = int(input(f"Saisir la distance de {v} à {key} : "))
            graph[v][key] = valeur  

    return graph

#  Algorithme de Dijkstra 
def dijkstra(graph, origine):
    assert all(graph[u][v] >= 0 for u in graph for v in graph[u])

    distance = {v: float('inf') for v in graph}
    precedent = {v: None for v in graph}
    distance[origine] = 0  
    queue = [(0, origine)] 

    while queue:
        dist_u, u = heapq.heappop(queue)  

        if dist_u > distance[u]:  
            continue

        for voisin, poids in graph[u].items():
            dist_voisin = distance[u] + poids

            if dist_voisin < distance[voisin]:  
                distance[voisin] = dist_voisin
                precedent[voisin] = u
                heapq.heappush(queue, (dist_voisin, voisin))

    return distance, precedent

"""
graph = {
    "Z": {"U": 6, "X": 7},
    "U": {"Y": -4, "V": 5, "X": 8},
    "X": {"V": -3, "Y": 9},
    "V": {"U": -2},
    "Y": {"V": -7, "Z": 2}
}"""

# main
graph = graph()
mon_graph = redimension_poids(graph)
print("Graphe final :", mon_graph)

origine = input("Entrez le sommet de départ pour Dijkstra : ")
distances, precedents = dijkstra(mon_graph, origine)

print("Distances depuis", origine, ":", distances)
print("Prédécesseurs :", precedents)


