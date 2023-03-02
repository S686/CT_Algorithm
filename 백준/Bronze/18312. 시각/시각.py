h, n = map(int, input().split())
cnt = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if str(n) in f'{i:02d}{j:02d}{k:02d}':
                cnt += 1
print(cnt)