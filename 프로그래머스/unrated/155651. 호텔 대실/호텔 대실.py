def minute(t):
    [h, m] = t.split(':')
    return int(h) * 60 + int(m)

def solution(book_time):
    answer = 0
    rooms = [0 for _ in range(24*60 + 10)]
    for i in book_time: 
        ci = minute(i[0])
        co = minute(i[1]) + 10
        rooms[ci] += 1
        rooms[co] -= 1
    #누적합  
    for i in range(1, len(rooms)):
        rooms[i] += rooms[i - 1]
    answer = max(rooms)
    return answer