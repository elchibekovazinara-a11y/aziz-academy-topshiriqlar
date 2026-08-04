text = input()
char = input()
x = text[::-1]
if char in x:
    print(x.index(char))
else:
    print("-1")