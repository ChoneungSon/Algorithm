def solution(numbers, hand):

    result = ""
    left, right = [3, 0], [3, 2]

    def dist(p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    for number in numbers:

        if number: number -= 1
        else: number = 10
        point = [number//3, number%3]

        if number in (0, 3, 6):
            add_str = 'L'
        elif number in (2, 5, 8):
            add_str = 'R'
        else:
            l_len = dist(left, point)
            r_len = dist(right, point)
            if l_len < r_len:
                add_str = 'L'
            elif l_len > r_len:
                add_str = 'R'
            else:
                add_str = 'R' if hand == 'right' else 'L'

        if add_str == 'R': right = point[:]
        else: left = point[:]

        result += add_str
    
    return result