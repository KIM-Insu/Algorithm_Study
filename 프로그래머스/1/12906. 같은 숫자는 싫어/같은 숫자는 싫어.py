def solution(arr):
    stack = []
    for i in arr:
        if stack and stack[-1] == i:  # stack이 비어있지 않고 stack의 마지막 원소와 현재 글자가 같으면 (= 중복되는 숫자면) continue
            continue
        else:                         # stack이 비어있거나 stack의 마지막 원소와 현재 글자가 다르면 (=처음 나오는 숫자면) stack에 append   
            stack.append(i)

    return stack
    
