n,m,k = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
chuls = list(map(int, input().split()))
for chul in chuls:
    s = 0
    e = len(cards)-1
    while True:
        m = (s+e)//2
        if cards[m] > 