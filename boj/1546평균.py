n = int(input())
score_lst = list(map(int, input().split()))
m = max(score_lst)
s = 0
for i in range(len(score_lst)):
    score_lst[i] = (score_lst[i]/m)*100
    s += score_lst[i]

print(s/len(score_lst))