import collections
text = str(input())
words = text.split()

replay={}
for word in words:
    if word in replay:
        replay[word] += 1
    else:
        replay[word]= 1

max_word = max(replay, key=replay.get)


