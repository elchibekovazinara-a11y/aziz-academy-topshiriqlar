n = int(input())
tub = [x for x in range(2, n + 1) if all(x % d != 0 for d in range(2, x))]
print(*tub)