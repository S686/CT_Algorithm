import sys
from collections import deque

input = sys.stdin.readline

cards = [i for i in range(1, int(input())+1)]
deck = deque(cards)

while len(deck) > 1:
    deck.popleft()
    if len(deck) <= 1:
        break
    deck.append(deck.popleft())
    
print(deck[0])