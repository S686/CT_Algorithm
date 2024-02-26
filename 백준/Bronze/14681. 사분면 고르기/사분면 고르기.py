import sys
lines = sys.stdin.read().splitlines()

x = int(lines[0])
y = int(lines[1])

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")