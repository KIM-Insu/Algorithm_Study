def solution(progresses, speeds):
    done = []
    for i,j in zip(progresses, speeds):
        if (100-i) % j == 0:
            done.append((100-i) // j)
        else:
            done.append(((100-i) // j) + 1)
    
    stack = []
    result = []
    cnt = 1
    for i in done:
        if stack and stack[-1] < i:
            stack.pop()
            stack.append(i)
            result.append(cnt)
            cnt = 1
        elif not stack:
            stack.append(i)
        else:
            cnt += 1
    result.append(cnt)
    return result