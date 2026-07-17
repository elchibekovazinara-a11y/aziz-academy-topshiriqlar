s = input()
unlilar_soni = 0

for ch in s:
    if ch in "aeiou":
        unlilar_soni += 1
        
print(unlilar_soni)