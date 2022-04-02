n = int(input())
visited = [0]*n
plus_visited=set()
minus_visited=set()
ans = 0
def chess(row:int):
    global ans
    if row == n:
        ans += 1
        return
    else:
        for i in range(n):
            p = row+i
            m = row-i
            if not visited[i] and p not in plus_visited and m not in minus_visited:
                visited[i] = 1
                plus_visited.add(p)
                minus_visited.add(m)
                chess(row+1)
                plus_visited.remove(p)
                minus_visited.remove(m)
                visited[i] = 0
chess(0)
print(ans)