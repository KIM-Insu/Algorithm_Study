def solution(ingredient):
    answer = 0
    burger = []                          # stack 생성

    for i in ingredient:    
        burger.append(i)     
        if burger[-4:] == [1, 2, 3, 1]:  # stack에 원소를 push하다가 스택의 마지막 4개의 값이 (빵(1), 야채(2), 고기(3), 빵(1)) 순으로 쌓이면 
            answer += 1                    
            for _ in range(4):           # 결과값에 버거 1개를 더하고 4개의 원소를 pop 
                burger.pop()
    return answer
