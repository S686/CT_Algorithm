N = int(input())
P = list(map(int, input().split()))
P.sort()
sum = 0
for i in range(0, len(P)):
    sum += P[i] * (len(P)-i)
print(sum)