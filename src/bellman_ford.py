def bellman_ford(graph, src):
    dist = [float('Inf')] * graph.vertices
    dist[src] = 0
    predecessors = [None] * graph.vertices

    # Relax edges V - 1 times
    for _ in range(graph.vertices - 1):
        for u, v, w in graph.edges:
            if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessors[v] = u

    # Check for negative-weight cycles
    for u, v, w in graph.edges:
        if dist[u] + w < dist[v]:
            return True, predecessors
    return False, None