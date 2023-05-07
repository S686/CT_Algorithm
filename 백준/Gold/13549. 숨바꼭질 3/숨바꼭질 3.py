import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        if 0 <= (v - 1) < 100001 and visited[v - 1] == -1:
            visited[v - 1] = visited[v] + 1
            q.append(v - 1)
        if 0 <= (v * 2) < 100001 and visited[v * 2] == -1:
            visited[v * 2] = visited[v]
            q.append(v * 2)
        if 0 <= (v + 1) < 100001 and visited[v + 1] == -1:
            visited[v + 1] = visited[v] + 1
            q.append(v + 1)

visited = [-1] * (100001)
input = sys.stdin.readline
n, k = map(int, input().split())
visited[n] = 0
print(bfs(n))