import sys

k = int(sys.stdin.readline())
arr = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n : arr.append(n)
    else : arr.pop()
print(sum(arr))