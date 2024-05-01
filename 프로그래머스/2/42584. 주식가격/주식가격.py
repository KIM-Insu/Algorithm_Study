def solution(prices):
    result = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[j] >= prices[i]:
                cnt += 1
            else:
                cnt += 1
                break
        result.append(cnt)
    return result
