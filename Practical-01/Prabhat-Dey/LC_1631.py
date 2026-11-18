import heapq
class Solution:
    def minimumEffortPath(self, heights):
        m = len(heights)
        n = len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while pq:
            effort, x, y = heapq.heappop(pq)
            if x == m-1 and y == n-1:
                return effort
            if effort > dist[x][y]:
                continue
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_effort = max(
                        effort,
                        abs(heights[x][y] - heights[nx][ny])
                    )
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heapq.heappush(
                            pq, (new_effort, nx, ny)
                        )
        return 0
