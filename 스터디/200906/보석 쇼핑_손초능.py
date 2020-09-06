def solution(gems):

    n = len(gems)
    gems_dict = {}

    for gem in gems:
        gems_dict[gem] = gems_dict.get(gem, 0) + 1

    left, right = 0, n-1
    answer = [1, n]

    while gems_dict[gems[right]] > 1:
        gems_dict[gems[right]] -= 1
        right -= 1

    while 1:

        while gems_dict[gems[left]] > 1:
            gems_dict[gems[left]] -= 1
            left += 1
        answer = min(answer, [left+1, right+1], key=lambda x: [x[1]-x[0], x[0]])

        right += 1
        if right == n: break
        gems_dict[gems[right]] += 1

    return answer
        

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))