from collections import deque

def BFS():
    global ans, compare_i

    while q:
        p = q.popleft()
        
        v_nums = v_lst[p]   #뽑은값이 1이면 1에 연결된 모든 노드들.
        unv_v_nums = []     #그중 방문하지 않은 점

        for num in v_nums:
            if visited[num] == 0:
                unv_v_nums.append(num)
        
        l = len(unv_v_nums)     #방문하지 않은 점의 길이
        if(set(input_BFS[compare_i:compare_i+l]) != set(unv_v_nums)):   
            ans = 0
            return
        else:
            for i in range(l):
                q.append(input_BFS[compare_i+i])
                visited[input_BFS[compare_i+i]] = 1
        
        compare_i += l

            

n = int(input())
v_lst = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(n-1):
    v, e = map(int, input().split())
    v_lst[v].append(e)
    v_lst[e].append(v)

input_BFS = list(map(int, input().split()))

q = deque()
q.append(1)
visited[1] = 1
compare_i = 1


ans = 1

BFS()

print(ans)
