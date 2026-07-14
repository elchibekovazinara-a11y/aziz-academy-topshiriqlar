n = int(input())

yigindi = 0
count = 0

while count < n:
    son = int(input())
    count += 1
    
    
    if son <= 0:
        continue
        
        
    yigindi += son
    
print(yigindi)