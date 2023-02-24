import sys
a = int(sys.stdin.readline())
l = [0 for i in range(a+1)]
l[0] = 1
l[1] = 1
for i in range(2, a+1):
    l[i] = l[i-1] + l[i-2]
print(l[a] % 10007)