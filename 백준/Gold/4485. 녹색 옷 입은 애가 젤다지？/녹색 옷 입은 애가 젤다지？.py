import sys, heapq

def dijkstra():
    queue = []
    heapq.heappush(queue, (route[0][0], 0, 0))
    dist[0][0] = route[0][0]

    while queue:
        cur_dist, x, y = heapq.heappop(queue)
        if cur_dist > dist[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = cur_dist + route[nx][ny]
                if cost < dist[nx][ny]:
                    heapq.heappush(queue, (cost, nx, ny))
                    dist[nx][ny] = cost

n = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
count = 0
while n != 0:
    count += 1
    route = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dist = [[sys.maxsize] * n for _ in range(n)]
    dijkstra()
    print(f'Problem {count}: {dist[n-1][n-1]}')
    n = int(sys.stdin.readline())