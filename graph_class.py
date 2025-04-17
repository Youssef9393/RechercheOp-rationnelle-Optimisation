import math


def minDistance(dist, Q):
    min = math.inf
    minNbr = ""
    for v in Q:
        if min>dist[v]:
            min = dist[v]
            minNbr = v
    return minNbr


def dijkstra(s, graph):
    dist = {}
    Q = []
    dist[s]=0
    pred = {}

    for noud in graph.keys():
        if noud != s:
            dist[noud] = math.inf
            pred[noud] = []

        Q.append(noud)

    while Q:
        u = minDistance(dist, Q)
        Q.remove(u)

        for v in graph[u].keys():
            temp = dist[u] + graph[u][v]
            if temp < dist[v]:
                dist[v] = temp
                pred[v] = u

    return dist, pred


graph = {
    "A": {"B": 2, "C": 1},
    "B": {"A":2, "C":3, "D":5, "E":9},
    "C": {"A":1, "B":3, "D":1, "E":8},
    "D": {"B":5, "C":1, "G":11},
    "E": {"B":9, "C":8, "F":3},
    "F": {"E":3, "G":9},
    "G": {"F":9, "D":11}
}

start = 'A'
dist, pred = dijkstra(start, graph)

print(f"{start} -> ",dist)