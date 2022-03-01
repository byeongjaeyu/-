n = int(input())
word_lst = [input() for _ in range(n)]
word_lst = list(set(word_lst))
word_lst.sort()
word_lst.sort(key=lambda x : len(x))
for i in range(len(word_lst)):
    print(word_lst[i])