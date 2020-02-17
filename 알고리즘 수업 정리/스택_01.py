# 스택
s = [0]*10
top = -1

top += 1 # push(10)
s[top] = 10

top += 1 # push(20)
s[top] = 20

if top != -1:
    d = s[top] # pop(20)
    top -= 1
    print(d)

if top != -1:
    d = s[top] # pop(10)
    top -= 1
    print(d)

while len(s) != 0:
    s.pop()
    # 작업을 하고 다시 이전 요소를 꺼내서 작업을 한다. -> 스택 구조를 활용한 알고리즘의 기본
    # 기본적으로 다른 함수에서 선언한 변수들을 사용을 할 수 없다. -> 스택 구조이기 때문에
    # 스택의 동적 구현