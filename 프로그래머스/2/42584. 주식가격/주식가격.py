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

# def solution(prices):
#     stack = []
#     result = [0] * len(prices)
#     days = 1
#     repeat = 1
#     for i in range(len(prices)):
#         if stack and stack[-1] > prices[i]:
#             while len(stack) > 0:
#                 stack.pop()
#                 result[i-repeat] = days
#                 repeat += 1
#                 days += 1
#             repeat = 1
#             days = 1
#             stack.append(prices[i])
#         else:
#             stack.append(prices[i])
            
#     for j in range(len(result)-1):
#         if result[j] == 0:
#             result[j] = len(result) - j - 1
#     return result