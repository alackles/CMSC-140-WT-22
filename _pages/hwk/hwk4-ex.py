n = int(input())

seen = set()
duplicates = set()

for _ in range(n):
    word = input().lower()
    if word in seen:
        duplicates.add(word)
    else:
        seen.add(word)

print(len(duplicates))
for i in sorted(duplicates):
    print(i)
