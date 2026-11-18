class Solution:
    def validPath(self, n, edges, source, destination):
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        stack.append(neighbour)
        return False