def solution(numbers, hand):
    pad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2), 
                0:(3,1)
    }
    left, right = {1,4,7}, {3,6,9}
    left_pos, right_pos = (3,0), (3,2)
    answer = []
    for num in numbers:
        if num in left:
            left_pos = pad[num]
            answer.append("L")
        elif num in right:
            right_pos = pad[num]
            answer.append("R")
        else:
            ldist = abs(left_pos[0] - pad[num][0]) + abs(left_pos[1] - pad[num][1])
            rdist = abs(right_pos[0] - pad[num][0]) + abs(right_pos[1] - pad[num][1])
            if ldist == rdist:
                if hand == 'left':
                    answer.append("L")
                    left_pos = pad[num]
                else:
                    answer.append("R")
                    right_pos = pad[num]
            else:
                if ldist > rdist:
                    answer.append("R")
                    right_pos = pad[num]
                else:
                    answer.append("L")
                    left_pos = pad[num]
    return "".join(answer)
            