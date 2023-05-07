scale = list(map(int,input().split(' ')))

ascending = True
descending = True
a = 1

for i in scale :
    if a == len(scale) : break
    if i < scale[a] :
        descending = False
    elif i > scale[a] :
        ascending = False
    a += 1

if ascending : print("ascending")
elif descending : print("descending")
else : print("mixed")
