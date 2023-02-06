import sys

def count_paint(m, y, x):
    count = 0 # 페인트 칠할 갯수
    base = board[y][x] # 첫 번째 칸
    for i in range(y, y+8): # 8x8 검사
        for j in range(x, x+8):
            if (i+j) % 2 == 0: # --> 첫 번째 칸과 같아야 하는 칸
                if board[i][j] != base:
                    count += 1
            else: # --> 첫 번째 칸과 달라야 하는 칸
                if board[i][j] == base:
                    count += 1
    if count > 32:
        count = 64 - count # 기준 바꾸기(첫 번째 칸 색 반전)
    return count if m > count else m # 최솟값 갱신

N, M = map(int, sys.stdin.readline().split())
board = []
answer = 32
for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

for i in range(N - 7): # 8x8 시작점 찾기
    for j in range(M - 7):
        answer = count_paint(answer, i, j) # 페인트칠 최솟값 찾기

print(answer)