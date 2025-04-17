import math

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

def minDistance(dist, Q):
    min_val = math.inf
    minNbr = None
    for v in Q:
        if dist[v] < min_val:
            min_val = dist[v]
            minNbr = v
    return minNbr

def dijkstra(s, graph):
    dist = {}
    Q = []
    pred = {}

    for noud in graph.keys():
        dist[noud] = math.inf
        pred[noud] = None
        Q.append(noud)

    dist[s] = 0

    while Q:
        u = minDistance(dist, Q)
        if u is None:
            break  
        Q.remove(u)

        for v, poids in graph[u].items():
            temp = dist[u] + poids
            if temp < dist[v]:
                dist[v] = temp
                pred[v] = u

    return dist, pred

# main
graph = graph()
start = input("origin : ")
dist, pred = dijkstra(start, graph)

print(f"{start} -> {dist}")  
print("Pred :", pred)  
