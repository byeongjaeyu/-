n = int(input())
nums = list(map(int, input().split()))
savep1 = 0
savep2 = n-1
pointer1 = 0
pointer2 = n-1
neer_val = 2000000001
while True:
    if pointer1 == pointer2:
        break
    else:
        val = nums[pointer1]+nums[pointer2]
        if abs(val) < neer_val:
            savep1 = pointer1
            savep2 = pointer2
            neer_val = abs(val)
            if val>0:
                pointer2 -= 1
            elif val == 0:
                break
            else:
                pointer1 += 1
        elif val == 0:
            break
        elif val>0:
            pointer2 -= 1
        else:
            pointer1 += 1

print(nums[savep1],nums[savep2])