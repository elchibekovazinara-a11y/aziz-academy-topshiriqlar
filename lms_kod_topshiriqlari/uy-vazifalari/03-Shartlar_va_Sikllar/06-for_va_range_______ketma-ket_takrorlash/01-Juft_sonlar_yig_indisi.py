N = int(input())
yigindi = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        yigindi += i
        
print(yigindi)