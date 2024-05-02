def solution(s):
    stack = []
    for i in s:
        if i == ')':                        # ')'가 나왔다면
            if stack and stack[-1] == '(':      # 1. stack이 비어있지 않고 stack의 마지막 원소가 '('이라면 pop해서 제거
                stack.pop()
            
            else:                               # 2. stack이 비어있을 때 = 왼쪽 괄호보다 오른쪽 괄호가 먼저 나온 경우 stack에 append
                stack.append(i)                 # 3. stack의 마지막 원소가 ')' = 오른쪽 괄호가 연속으로 나온 경우 stack에 append
                                            
        else:                               # '('가 나왔다면
            stack.append(i)                     # stack에 append  
    return not stack
