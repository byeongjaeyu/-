n = int(input())
nums = list(map(int, input().split()))
nums.sort()
savep1 = 0
savep2 = 0
savep3 = 0
neer_val = 3000000001
for i in range(n-2):
    pointer1 = i
    pointer2 = i+1
    pointer3 = n-1
    default = nums[pointer1]
    flag = True
    while True:
        if pointer2 == pointer3:
            break
        else:
            val = default + nums[pointer2] + nums[pointer3]
            if abs(val) < neer_val:
                savep1 = pointer1
                savep2 = pointer2
                savep3 = pointer3
                neer_val = abs(val)
                if val == 0:
                    flag = False
                    break
                elif val>0:
                    pointer3 -= 1
                else:
                    pointer2 += 1
            elif val == 0:
                flag = False
                break
            elif val>0:
                pointer3 -= 1
            else:
                pointer2 += 1
    if not flag:
        break

print(nums[savep1],nums[savep2],nums[savep3])