def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:                                # 크레인의 작동 위치 (i번째 열)    
        for j in range(len(board)):                     
            if board[j][i-1] != 0:                 # i번째 열에서 처음으로 0이 아닌 곳 = i번째 열의 가장 위에 있는 인형 
                pick = board[j][i-1]                
                if stack and stack[-1] == pick:    # 스택이 비어있지 않고 스택의 peek이 새로 뽑은 인형의 종류와 같다면 결과값 +2
                    stack.pop()
                    answer += 2
                else:                              # 스택이 비어있거나 새로 뽑은 인형과 스택의 peek의 종류가 다르다면 스택에 push
                    stack.append(pick)
            
                board[j][i-1] = 0                  # 뽑은 인형의 칸을 비워주고 iteration 종료 -> moves의 다음 원소로 이동
                break
        
    return answer
