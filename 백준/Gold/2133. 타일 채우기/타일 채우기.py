import sys

input = sys.stdin.readline

dp = [1,0,3,0]
n = int(input())

for i in range(4, n + 1):
    if (i % 2 != 0):
        dp.append(0)
    else:
        dp.append(dp[i-2] * dp[2] + 2)
        for j in range(i - 4, 0, -2):
            dp[i] += dp[j] * 2
    
print(dp[n])