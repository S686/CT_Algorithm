import sys
n, k = map(int, sys.stdin.readline().split())
cnt = 0
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
l = l[::-1]
while(k > 0):
    for i in l:
        cnt += k // i
        k %= i
print(cnt)