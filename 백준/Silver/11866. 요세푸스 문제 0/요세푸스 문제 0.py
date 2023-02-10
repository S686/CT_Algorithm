import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
cir = deque([i for i in range(1, n+1)])
answer = []

while cir:
    for i in range(k - 1):
        cir.append(cir.popleft())
    answer.append(cir.popleft())

print("<", end='')
for i in range(len(answer) - 1):
    print(f'{answer[i]},', end=' ')
print(f'{answer[-1]}>')