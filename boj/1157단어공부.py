st = str(input())
d = dict()
for s in st:
    if s.isupper():
        if s.lower() not in d:
            d[s.lower()] = 1
        else:
            d[s.lower()] += 1
    else:
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1

m = max(d.values())
ans = []
for k in d:
    if d[k]==m:
        ans.append(k)

print(ans[0].upper()) if len(ans)==1 else print('?')
