import sys

k, n = map(int, sys.stdin.readline().split())
lan = []
for i in range(k):
    lan.append(int(sys.stdin.readline()))

#이분탐색
min_len = 1
max_len = max(lan)

while min_len <= max_len:
    mid = (min_len + max_len) // 2
    cnt = 0
    for i in lan:
        cnt += i // mid
    if cnt >= n: # 만든 랜선 수가 요구사항보다 더 많으면
        min_len = mid + 1 # 랜선 최소 길이 1 증가
    else: # 랜선 수 부족
        max_len = mid - 1 # 랜선 최대 길이 1 감소

print(max_len)