from typing import List, Tuple
import heapq

def path_finder(area: str) -> int:
    area = area.splitlines()
    n = len(area)

    def get_neighbors(x: int, y: int) -> List[Tuple[int, int]]:
        return [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= x + dx < n and 0 <= y + dy < n]

    graph = {i * n + j: {} for i in range(n) for j in range(n)}
    
    for i in range(n):
        for j in range(n):
            for ni, nj in get_neighbors(i, j):
                weight = abs(int(area[i][j]) - int(area[ni][nj]))
                graph[i * n + j][ni * n + nj] = weight

    start, target = 0, n * n - 1
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)
        
        if node == target:
            return dist
        
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return -1
