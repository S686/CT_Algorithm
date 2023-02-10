import sys

n, k = map(int, sys.stdin.readline().split())
cir = [i for i in range(0, n+1)]
answer = []
index = 0
for _ in range(n):
    for i in range(k): # k번째 찾기
        while True: # 이미 제거된 사람이면 건너뛰기
            index += 1
            index %= (n + 1)
            if cir[index] != 0:
                break
    answer.append(cir[index])
    cir[index] = 0

print("<", end='')
for i in range(len(answer) - 1):
    print(f'{answer[i]},', end=' ')
print(f'{answer[-1]}>')