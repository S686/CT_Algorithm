def solution(numbers):
    answer = 0
    numlist = [i for i in range(0, 10)]
    for i in numlist:
        if i not in numbers:
            answer += i
    return answer