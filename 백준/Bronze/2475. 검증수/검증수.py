import sys
input = sys.stdin.readline
num = list(map(int, input().split()))
v = 0
for x in num:
    v += (x ** 2)
print(v%10)