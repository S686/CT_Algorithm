import sys
n = int(sys.stdin.readline())
cnt = 0
a = 1000-n
if a >= 500:
    cnt += a // 500
    a %= 500
if a >= 100:
    cnt += a // 100
    a %= 100
if a >= 50:
    cnt += a // 50
    a %= 50
if a >= 10:
    cnt += a // 10
    a %= 10
if a >= 5:
    cnt += a // 5
    a %= 5
if a >= 1:
    cnt += a // 1
    a %= 1
print(cnt)