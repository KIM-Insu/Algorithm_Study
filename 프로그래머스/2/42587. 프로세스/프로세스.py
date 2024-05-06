def solution(priorities, location):
    deque = [(val, idx) for idx, val in enumerate(priorities)]  # (우선순위, 인덱스) 값을 담은 덱 생성
    
    process_order = 0
    while deque:
        if deque[0][0] < max(deque, key = lambda x : x[0])[0]:  # 덱의 맨 앞의 원소의 우선순위 값이 최댓값보다 작다면
            deque.append(deque.pop(0))                          # 맨 앞의 원소를 pop하고 맨 뒤로 append  
        
        else:
            process_order += 1                                  # 덱의 맨 앞의 원소가 가장 큰 우선순위의 값이라면
            if deque.pop(0)[1] == location:                     # 인덱스를 pop하고 location과 같다면 
                return process_order                            # 이때의 process_order를 반환
