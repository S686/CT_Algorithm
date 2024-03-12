import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in numbers:
    if i < 2:
        pass
    else:
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            count += 1

print(count)
        