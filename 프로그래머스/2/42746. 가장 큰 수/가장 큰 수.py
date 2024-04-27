def compare(x):
    if len(x) == 1:
        return x * 4
    elif len(x) == 2:
        return x * 2
    elif len(x) == 3:
        return x + x[0]
    else:
        return x

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse= True, key= lambda x : compare(x))
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    return answer