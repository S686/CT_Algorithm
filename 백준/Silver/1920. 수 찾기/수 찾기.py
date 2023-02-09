import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in b:
    left, right = 0, n - 1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if i == a[mid]:
            print('1')
            flag = True
            break
        elif i < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if not flag:
        print('0')