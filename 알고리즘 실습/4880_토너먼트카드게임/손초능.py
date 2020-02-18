def fight(a, b):
    global nums
    if nums[a-1] == 1:
        if nums[b-1] == 1 or nums[b-1] == 3:
            return a
        elif nums[b-1] == 2:
            return b
    if nums[a-1] == 2:
        if nums[b-1] == 2 or nums[b-1] == 1:
            return a
        elif nums[b-1] == 3:
            return b
    if nums[a-1] == 3:
        if nums[b-1] == 3 or nums[b-1] == 2:
            return a
        elif nums[b-1] == 1:
            return b

def part(s, e):

    if s+1 == e:
        return fight(s, e)
    elif s == e:
        return s
    else:
        a = part(s, (s+e)//2)
        b = part((s+e)//2+1, e)
        return fight(a, b)

T = int(input())

for case in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    print('#{0} {1}'.format(case, part(1, len(nums))))