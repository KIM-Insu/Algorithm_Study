# [카카오 인턴] 키패드 누르기
def solution(numbers, hand):
    answer = ''

    d = {1 : [3,0], 2 : [3,1], 3 : [3,2],
         4 : [2,0], 5 : [2,1], 6 : [2,2],
         7 : [1,0], 8 : [1,1], 9 : [1,2],
         "*" : [0,0], 0 : [0,1], "#" : [0,2]}

    left = d['*']
    right = d['#']  

    for i in numbers:
        num = d[i]    
        if i in [1,4,7]:
            answer += "L"
            left = num
        elif i in [3,6,9]:
            answer += "R"
            right = num
        elif i in [2,5,8,0]:
            left_d = abs(left[0] - num[0]) + abs(left[1] - num[1])
            right_d = abs(right[0] - num[0]) + abs(right[1] - num[1])

            if left_d < right_d:
                answer += "L"
                left = num
            elif left_d > right_d:
                answer += "R"
                right = num
            else:
                if hand == 'left':
                    answer += "L"
                    left = num
                else:
                    answer += "R"
                    right = num
    return answer