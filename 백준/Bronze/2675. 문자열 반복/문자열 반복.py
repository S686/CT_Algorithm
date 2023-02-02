import sys

T = int(sys.stdin.readline())
for _ in range(T):
    R, S = input().split()
    for i in S:
        print(i * int(R), end='')
    print()