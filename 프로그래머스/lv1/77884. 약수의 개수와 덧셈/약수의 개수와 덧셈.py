def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for x in range(1, i):
            if i % x == 0:
                count += 1
        if count % 2 == 1:
            answer += i
        else:
            answer -= i
    return answer