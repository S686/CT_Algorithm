import sys

input = sys.stdin.readline
matrix = []

n, m = map(int, input().split())
for i in range(n*2):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(matrix[i][j] + matrix[i+n][j], end=' ')
    print()
