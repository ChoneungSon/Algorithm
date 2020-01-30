# count 배열을 만드는 방법

# num = [4, 5, 6, 7, 7, 9]
# num = list(input()) # 숫자들이 각각 떨어진 문자열로 저장
n = int(input())
num = int(input())
count = [0] * 10

# for i in num:
#     count[int(i)] += 1

for _ in range(n):
    count[num%10] += 1
    num //= 10

print(count)