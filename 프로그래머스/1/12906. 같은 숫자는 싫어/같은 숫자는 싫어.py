def solution(arr):
    stack = []
    for i in arr:
        if stack and stack[-1] == i:
            continue
        else:
            stack.append(i)

    return stack
    