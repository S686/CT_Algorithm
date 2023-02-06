import sys

while True:
    n = int(sys.stdin.readline())
    if n <= 0:
        break
    word = list(str(n)) # 숫자를 한 자리씩 리스트에 저장
    if word == word[::-1]: # 리스트와 리스트(역순)이 같은지 검사
        print('yes')
    else:
        print('no')