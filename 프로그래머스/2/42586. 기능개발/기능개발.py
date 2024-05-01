def solution(progresses, speeds):
    done = [(100-i) // j + min((100-i) % j, 1) for i,j in zip(progresses, speeds)]
    stack = []
    result = []
    
    cnt = 1
    for i in done:
        if stack and stack[-1] < i:
            stack.append(i)
            result.append(cnt)
            cnt = 1
        elif not stack:
            stack.append(i)    
        else:
            cnt += 1
    result.append(cnt)
    return result