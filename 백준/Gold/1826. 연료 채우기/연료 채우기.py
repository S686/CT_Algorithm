#1826
import sys, heapq
n = int(sys.stdin.readline())
con = []
h = [] # maxheap
cnt = 0
for i in range(n):
    heapq.heappush(con, list(map(int, sys.stdin.readline().split())))
d, s = map(int, sys.stdin.readline().split())
while s < d:
    while con and con[0][0] <= s:
        dis, sat = heapq.heappop(con)
        heapq.heappush(h, (-1 * sat, dis))
    if not h:
        cnt = -1
        break
    sat, a = heapq.heappop(h)
    s -= sat
    cnt += 1
print(cnt)