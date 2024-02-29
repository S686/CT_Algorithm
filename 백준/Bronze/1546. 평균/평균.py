import sys

input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
m = max(score)

avg = sum(score)/len(score)/m * 100
print(avg)