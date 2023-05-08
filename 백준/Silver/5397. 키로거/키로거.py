import sys
input = sys.stdin.readline

testcase = int(input())
for i in range(testcase):
    string = input().strip()
    left_stack = []
    right_stack = []
    for c in string:
        if c == '-':
            if left_stack:
                left_stack.pop()
        elif c == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif c == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(c)
    left_stack.extend(reversed(right_stack))
    print(*left_stack, sep='')