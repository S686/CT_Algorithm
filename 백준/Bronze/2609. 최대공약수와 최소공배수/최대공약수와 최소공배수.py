import sys
input = sys.stdin.readline

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return int(x * y / gcd(x, y))

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))