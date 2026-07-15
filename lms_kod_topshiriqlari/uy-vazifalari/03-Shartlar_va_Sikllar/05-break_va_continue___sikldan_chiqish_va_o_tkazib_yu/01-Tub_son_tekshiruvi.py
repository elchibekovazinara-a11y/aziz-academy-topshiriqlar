n = int(input())
is_tub = n > 1

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_tub = False
        break
        
print("ha" if is_tub else "yo'q")