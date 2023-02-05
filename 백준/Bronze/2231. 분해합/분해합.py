import sys

def sum_digit(n):
    return sum(map(int, str(n)))
N = int(sys.stdin.readline())
answer = N
for i in range(1, N):
    if (i + sum_digit(i)) == N:
        if answer > i:
            answer = i
if answer == N:
    answer = 0
print(answer)