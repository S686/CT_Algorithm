import sys
input = sys.stdin.readline
for i in input():
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    print(i, end='')