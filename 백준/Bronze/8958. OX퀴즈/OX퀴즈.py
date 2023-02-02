import sys

T = int(sys.stdin.readline())
for _ in range(T):
    ox = sys.stdin.readline().strip()
    score = 0
    count = 0
    for i in ox:
        if i == 'X':
            count = 0
        else:
            count += 1
            score += count
    print(score)