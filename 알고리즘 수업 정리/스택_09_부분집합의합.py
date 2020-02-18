def f(n, k, s):
    global count, ans
    count += 1
    if n == k:
        if s == 55: # 합이 10인 경우의 수
            ans += 1
    # elif s > 10: # 완전탐색코드를 작성하고, 중간 경우를 생략하는 코드를 삽입한다.(백트레킹)
    #     return
    else:
        f(n+1, k, s)
        f(n+1, k, s+A[n])

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
ans = 0
f(0, 10, 0)
print(count, ans)