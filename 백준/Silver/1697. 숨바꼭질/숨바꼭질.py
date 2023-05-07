import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for i in (v - 1, v + 1, v * 2):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

visited = [0] * (100001)
input = sys.stdin.readline
n, k = map(int, input().split())
print(bfs(n))