tub_sonlar_soni = 0

while True:
    son = int(input())
    
    if son == 0:
        break
        
    if son < 2:
        continue
        
        
        
    buluvchi = 2
    tub = True
    
    while buluvchi < son:
        if son % buluvchi == 0:
            tub = False
            break
        buluvchi += 1
        
        
    if tub:
        tub_sonlar_soni += 1
        
print(tub_sonlar_soni)