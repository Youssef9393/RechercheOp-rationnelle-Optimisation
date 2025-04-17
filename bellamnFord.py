
def bellman_ford(graph, source):
    # Initialize distances
    distances = {v: float('inf') for v in graph}
    distances[source] = 0  
    
    predecessors = {v: None for v in graph}
    
    iteration_count = 0  # Counter for iterations
    
    # Relax edges |V|-1 times
    for _ in range(len(graph) - 1):
        updated = False  
        for u in graph:
            for v, w in graph[u].items():
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    predecessors[v] = u  # Track the predecessor
                    updated = True
                    iteration_count += 1  # Increment counter
        if not updated:  # If no update, we can stop
            break
    
    # Check for negative weight cycles and identify the nodes in the cycle
    negative_cycle_nodes = []
    
    for u in graph:
        for v, w in graph[u].items():
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                # Found a negative cycle, now identify the nodes in it
                negative_cycle_nodes = find_negative_cycle(graph, v, predecessors)
                return distances, iteration_count, negative_cycle_nodes
    
    return distances, iteration_count, negative_cycle_nodes

def find_negative_cycle(graph, start_node, predecessors):
    visited = set()
    current = start_node
    
    # Follow predecessors until we find a cycle
    while current not in visited and current is not None:
        visited.add(current)
        current = predecessors[current]
    
    if current is None:
        return []  # No cycle found
    
    # Reconstruct the cycle
    cycle = []
    cycle_start = current
    current = predecessors[current]
    cycle.append(cycle_start)
    
    while current != cycle_start:
        cycle.append(current)
        current = predecessors[current]
    
    cycle.append(cycle_start)  # Complete the cycle
    return cycle[::-1]  # Return in proper order
    
# Graph definition
graph = {
    "Z": {"U": 6, "X": 7},
    "U": {"Y": -4, "V": 5, "X": 8},
    "X": {"V": -3, "Y": 9},
    "V": {"U": -2},
    "Y": {"V": -7, "Z": 2}
}

source = 'Z'
try:
    shortest_distances, total_iterations, negative_cycle = bellman_ford(graph, source)
    print("Shortest distances:", shortest_distances)
    print("Total iterations:", total_iterations)
    if negative_cycle:
        print("Negative cycle found containing nodes:", " → ".join(negative_cycle))
except ValueError as e:
    print(e)