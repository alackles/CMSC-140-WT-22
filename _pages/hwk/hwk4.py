# You get a number and then that many words
# Find the number of duplicate words
# Output the number of words
# Then output those words in all lowercase, even if they come in differently

# Example:
# 5
# bear
# Bear
# apple
# Apple
# banana

# Taking in the input
words = []
n = int(input())
for i in range(n):
    nextword = input().lower()
    words.append(nextword)
#print("All words", words)

# Sorting through the words
words_seen = []
duplicate_words = []
for word in words:
    if word in words_seen and word not in duplicate_words:
        duplicate_words.append(word)
    else:
        words_seen.append(word)

#print("Seen words", words_seen)
#print("Duplicate words", duplicate_words)

# Printing out the answer 
#alpha order:
duplicate_words.sort()
print(len(duplicate_words))
for word in duplicate_words:
    print(word)