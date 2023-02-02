import sys

def deu_lotto(start, depth): ## dfs
    if depth == 6:
        for i in range(depth):
            print(lotto[i], end=' ')
        print()
        return
    for i in range(start, len(T)):
        lotto[depth] = T[i]
        deu_lotto(i + 1, depth + 1)

lotto = [0 for _ in range(13)]
while True:
    T = list(map(int, sys.stdin.readline().split()))
    if T[0] == 0:
        break
    del T[0]
    deu_lotto(0,0)
    print()