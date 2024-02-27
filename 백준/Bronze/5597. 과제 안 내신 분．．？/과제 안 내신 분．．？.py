import sys
input = sys.stdin.readline

student = []

submits = list(int(input().strip()) for i in range(28))

for i in range(1, 31):
    if i not in submits:
        student.append(i)

student.sort()
print(student[0])
print(student[-1])