import sys
while True:
    leg = list(map(int, sys.stdin.readline().split()))
    if leg.count(0) == 3:
        break
    leg.sort()
    if leg[0] ** 2 + leg[1] ** 2 == leg[-1] ** 2:
        print('right')
    else:
        print('wrong')