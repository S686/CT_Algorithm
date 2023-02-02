import sys
N = sys.stdin.readline().strip()
suml = 0
sumr = 0
for i in range(0, len(N)//2):
    suml += int(N[i])
for i in range(len(N)//2, len(N)):
    sumr += int(N[i])
if suml == sumr:
    print("LUCKY")
else:
    print("READY")