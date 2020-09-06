def solution(s):

    min_length = float('inf')

    for i in range(1, len(s)+1):
        total_string = ""
        string = s[:i]
        cnt = 1
        if len(s)//i > 1:
            for j in range(1, len(s)//i):
                a = s[i*j:i*(j+1)]
                if string != a:
                    if cnt == 1: total_string += string
                    else: total_string += string + str(cnt)
                    string = s[i*j:i*(j+1)]
                    cnt = 1
                else:
                    cnt += 1
            if cnt == 1: total_string += string
            else: total_string += string + str(cnt)
            total_string += s[i*(j+1):]
            min_length = min(min_length, len(total_string))

    return min_length

print(solution("abcabcdede"))