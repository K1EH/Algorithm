N = int(input())
word = set(input()  for i in range(N))
word = list(word)
word.sort(key = lambda x : (len(x), x))
for _ in word:
    print(_)