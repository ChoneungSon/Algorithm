def fibo(n):
    global memo

    if n < 2:
        return memo[n]
    elif n >= 2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]
    else:
        return memo[n]

def fact(n):
    global memo_fact

    if n < 2:
        return memo_fact[n]
    elif n >= 2 and memo_fact[n] == 0:
        memo_fact[n] = n * fact(n-1)
        return memo_fact[n]
    else:
        return memo_fact[n]

memo = [0] * 100
memo[1] = 1
memo_fact = [0]*100
memo_fact[0] = 1
memo_fact[1] = 1

print(memo)
print(fibo(99))
print(memo)

print(memo_fact)
print(fact(99))
print(memo_fact)

