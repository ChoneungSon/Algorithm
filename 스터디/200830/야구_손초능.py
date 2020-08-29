import sys
from itertools import permutations
input = sys.stdin.readline

def game():
    global hitters, action, inning, max_score
    hitter = score = 0
    for i in range(inning):
        b1 = b2 = b3 = out_cnt = 0
        while out_cnt < 3:
            hit_cnt = action[i][hitters[hitter]]
            if hit_cnt == 0: out_cnt += 1
            elif hit_cnt == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif hit_cnt == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif hit_cnt == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1 = b2 = b3 = 0
            hitter = (hitter + 1) % 9
    max_score = max(max_score, score)

inning = int(input())

action = [list(map(int, input().split())) for _ in range(inning)]

max_score = 0

for i in permutations(range(1, 9)):
    hitters = list(map(int, i))
    hitters = hitters[:3] + [0] + hitters[3:]
    game()

print(max_score)