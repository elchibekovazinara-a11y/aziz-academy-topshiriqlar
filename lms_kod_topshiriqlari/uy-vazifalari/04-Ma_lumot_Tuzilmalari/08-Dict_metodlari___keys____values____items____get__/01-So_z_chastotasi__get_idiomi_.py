words = input().split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
    
for word in sorted(freq.keys()):
    print(f"{word} {freq[word]}")