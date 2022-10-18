"""
Word Occurrences
Estimate: 20 minutes
Actual:   18 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
max_length = max(len(word) for word in words)
for word in sorted(set(words)):
    print(f"{word:{max_length}} : {word_to_count[word]}")

