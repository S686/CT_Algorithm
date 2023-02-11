def solution(s, skip, index):
    answer = ''
    for i in s:
        pw = ord(i)
        for j in range(index):
            pw += 1
            if pw > ord('z'):
                pw -= 26
            while chr(pw) in skip:
                pw += 1
                if pw > ord('z'):
                    pw -= 26
        answer += chr(pw)
    return answer