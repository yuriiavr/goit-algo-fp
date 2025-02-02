import heapq

def dijkstra(graph, start):
    heap = []
    heapq.heappush(heap, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3, 'E': 8},
    'E': {'D': 8}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Найкоротші шляхи від стартової вершини:")
for node, distance in distances.items():
    print(f"Від {start_node} до {node}: {distance}")