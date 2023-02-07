import sys

a, b, v = map(int, sys.stdin.readline().split())
answer = (v-b)//(a-b)
if (v-b) % (a-b) : print(answer + 1)
else : print(answer)