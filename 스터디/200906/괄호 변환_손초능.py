def balance(p):
    q = []
    for i in p:
        if not q:
            if i == ')': return False
            q.append(i)
        else:
            if q[-1] == i:
                q.append(i)
            elif q[-1] != i and q[-1] == ')':
                return False
            else: q.pop()
    if q: return False
    else: return True

def solution(p):
    if balance(p): return p
    else:
        bracket = [0] * 2
        for idx, i in enumerate(p):
            if i == '(': bracket[0] += 1
            else: bracket[1] += 1
            if bracket[0] and bracket[0] == bracket[1]:
                if balance(p[:idx+1]):
                    return p[:idx+1] + solution(p[idx+1:])
                else:
                    result = '(' + solution(p[idx+1:]) + ')'
                    for j in range(1, idx):
                        result += '(' if p[j] == ')' else ')'
                    return result

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))