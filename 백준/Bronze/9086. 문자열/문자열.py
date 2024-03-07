import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    sentence = input().strip()
    print(f"{sentence[0]}{sentence[-1]}")