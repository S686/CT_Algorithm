import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
blackjack = 0
for i in range(n-2):
    for j in range(i + 1, n-1):
        for k in range(j + 1, n):
            card_sum = cards[i] + cards[j] + cards[k]
            if card_sum > m:
                continue
            elif blackjack < card_sum:
                blackjack = card_sum
print(blackjack)
