N = int(input())
sonlar = [int(input()) for _ in range(N)]

print(sonlar.index(max(sonlar)) + 1)