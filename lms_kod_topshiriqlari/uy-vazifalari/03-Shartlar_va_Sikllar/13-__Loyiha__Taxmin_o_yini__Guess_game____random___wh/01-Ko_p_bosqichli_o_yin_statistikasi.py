import sys

I = iter(map(int,sys.stdin.read().split()))
res = []

for i in range(1, next(I) + 1):
    t, c = next(I) , 0
    while c := c + 1:
        if next(I) == t:
            break
    res.append(c)
    print(f"Round {i}: {c} urinish")
    
print(f"Jami: {sum(res)}\nEng yaxshi: {min(res)}")