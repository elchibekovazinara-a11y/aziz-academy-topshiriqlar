import sys
sonlar = [int(x) for x in sys.stdin.read().split()[1:] if int(x) > 0]
print(sum(sonlar) // len(sonlar) if sonlar else 0)