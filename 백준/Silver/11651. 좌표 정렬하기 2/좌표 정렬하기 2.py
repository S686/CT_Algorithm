import sys

k = int(sys.stdin.readline())
arr = []
for i in range(k):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr.sort(key = lambda x : (x[1], x[0])) # y 오름차순 정렬 후, x 오름차순 정렬
for x, y in arr:
    print(x, y)