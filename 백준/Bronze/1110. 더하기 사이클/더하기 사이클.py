N = int(input())
num = N
tmp = 0
count = 0
while True:
    if num < 10:
        tmp = num
    else:
        tmp = num // 10 + num % 10
    num = num % 10 * 10 + tmp % 10
    count += 1
    if N == num:
        break

print(count)