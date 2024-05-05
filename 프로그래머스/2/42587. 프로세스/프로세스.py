def solution(priorities, location):
    deque = [(val, idx) for idx, val in enumerate(priorities)]  # (인덱스, 우선순위)를 담은 덱 생성
    
    process_order = 0
    while deque:
        if deque[0][0] < max(deque, key = lambda x : x[0])[0]:  # 덱의 가장 앞의 원소의 우선순위가 최댓값보다 작다면 pop하고 덱 맨 뒤로 추가
            deque.append(deque.pop(0))
        
        else:                                  
            process_order += 1                # 가장 앞의 원소가 최댓값이라면 count를 +1 해주고 pop  
            if deque.pop(0)[1] == location:   # 이때, pop한 원소의 인덱스 값이 location과 같으면 이 시점의 count를 반환  
                return process_order
