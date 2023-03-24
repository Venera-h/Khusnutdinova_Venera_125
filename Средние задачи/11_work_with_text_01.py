# не доделано


import collections
print("Введите текст")
text = str(input())
words = text.split()

replay={}
if len(words) <5:
    print("Write other text")
else:
    for word in words:
        if word in replay:
            replay[word] += 1
        else:
            replay[word]= 1

max_word = max(replay, key=replay.get)
max_len = max(words, key = len)

print(max_word, max_len)


