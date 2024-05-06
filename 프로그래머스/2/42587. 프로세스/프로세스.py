def solution(priorities, location):
    deque = [(val, idx) for idx, val in enumerate(priorities)]
    
    process_order = 0
    while deque:
        if deque[0][0] < max(deque, key = lambda x : x[0])[0]:
            deque.append(deque.pop(0))
        
        else:
            process_order += 1
            if deque.pop(0)[1] == location:
                return process_order