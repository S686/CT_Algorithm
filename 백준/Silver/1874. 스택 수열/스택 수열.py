import sys
input = sys.stdin.readline

n = int(input())
num = 1
stack = []
answer = []

for i in range(n):
    input_num = int(input())
    while num <= input_num:
        stack.append(num)
        num += 1
        answer.append('+')
    if stack[-1] == input_num:
        stack.pop(-1)
        answer.append('-')
    else:
        print('NO')
        exit(0)
print(*answer, sep='\n')
