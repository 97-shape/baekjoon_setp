import sys

n = int(sys.stdin.readline().rstrip())
words = []

for i in range(n):
    word = sys.stdin.readline().rstrip()
    words.append((len(word), word))

words = list(set(words))
words.sort(key=lambda words: (words[0], words[1]))

for i in words:
    print(i[1])