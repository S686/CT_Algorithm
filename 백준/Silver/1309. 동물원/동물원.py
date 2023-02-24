import sys #1309
a = int(sys.stdin.readline())
l = [0 for _ in range(a+1)]
l[0] = 3
l[1] = 7
for i in range(2, a+1):
    l[i] = ((l[i-1]%9901) * 2 + (l[i-2]%9901))%9901
print(l[a-1])