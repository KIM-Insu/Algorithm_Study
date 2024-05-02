from collections import deque
def solution(length, weight, truck):
    deque_truck = deque()
    deque_time = deque()
    time = 0
    while truck:
        time += 1
        if deque_time and time - deque_time[0] == length:
            deque_time.popleft()
            deque_truck.popleft()
        
        if sum(deque_truck) + truck[0] <= weight:
            deque_truck.append(truck.pop(0))
            deque_time.append(time)
    
    return time + length