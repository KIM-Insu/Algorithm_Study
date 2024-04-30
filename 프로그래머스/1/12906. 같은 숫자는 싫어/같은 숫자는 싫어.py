def solution(arr):
    stack = []
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            continue
        else:
            stack.append(i)

    return stack
    