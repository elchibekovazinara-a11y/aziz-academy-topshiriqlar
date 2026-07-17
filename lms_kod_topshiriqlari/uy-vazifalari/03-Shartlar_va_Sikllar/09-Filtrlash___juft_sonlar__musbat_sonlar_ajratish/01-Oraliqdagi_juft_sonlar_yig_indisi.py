a = int(input())
b = int(input())

boshlash = a if a % 2 == 0 else a + 1

print(sum(range(boshlash, b + 1, 2)))