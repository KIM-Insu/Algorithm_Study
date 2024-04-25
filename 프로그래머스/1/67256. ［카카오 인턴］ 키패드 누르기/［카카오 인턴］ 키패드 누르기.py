def solution(numbers, hand):
    answer = ''
    # 키패드별 좌표값 저장 (왼쪽 아래에서부터 (0,0))
    d = {1 : [3,0], 2 : [3,1], 3 : [3,2],
         4 : [2,0], 5 : [2,1], 6 : [2,2],
         7 : [1,0], 8 : [1,1], 9 : [1,2],
         "*" : [0,0], 0 : [0,1], "#" : [0,2]}
    
    # 초기 왼손, 오른손의 좌표 설정
    left = d['*']
    right = d['#']  

    for i in numbers:
        num = d[i]                  
        if i in [1,4,7]:            # 1,4,7은 왼손 이용
            answer += "L"            
            left = num              # 현재 왼손의 위치를 움직인 좌표로 업데이트
        elif i in [3,6,9]:          # 3,6,9는 오른손 이용  
            answer += "R"
            right = num
        elif i in [2,5,8,0]:        # 가운데 열의 숫자 2,5,8,0은 아래의 조건들에 의해 결정
            
            # 왼손과 오른손의 현재 좌표에서 누르고자 하는 숫자 사이의 거리
            left_d = abs(left[0] - num[0]) + abs(left[1] - num[1])
            right_d = abs(right[0] - num[0]) + abs(right[1] - num[1])

            if left_d < right_d:    
                answer += "L"
                left = num
            elif left_d > right_d:   # 거리를 비교해서 더 가까운 손을 이동하고 좌표 업데이트
                answer += "R"
                right = num
            else:                    # 양손의 거리가 같다면 왼손잡이인지 오른손잡이인지에 따라 좌표 업데이트
                if hand == 'left':
                    answer += "L"
                    left = num
                else:
                    answer += "R"
                    right = num
    return answer
