from collections import deque
from functools import reduce

def bfs_shortest_path(graph, start, goal):
    def bfs(queue, visited):
        if not queue:
            return []

        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        new_paths = map(
            lambda neighbor: path + [neighbor],
            filter(lambda n: n not in visited, graph.get(node, []))
        )

        queue.extend(new_paths)
        visited.add(node)
        return bfs(queue, visited)

    return bfs(deque([[start]]), set())

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

droga = bfs_shortest_path(graph, 'A', 'F')
print("Najkrótsza ścieżka:", droga)
