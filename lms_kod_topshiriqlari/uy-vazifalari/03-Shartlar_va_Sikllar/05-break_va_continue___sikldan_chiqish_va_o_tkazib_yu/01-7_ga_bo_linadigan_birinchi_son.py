n = int(input())

count = 0
found = False

while count < n:
    son = int(input())
    count += 1
    
    if son % 7 == 0:
        print(son)
        found = True
        break
        
if not found:
    print("yo'q")