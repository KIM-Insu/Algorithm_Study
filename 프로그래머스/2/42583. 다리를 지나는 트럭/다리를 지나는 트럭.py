from collections import deque
def solution(bridge_length, weight, truck_weights):
    deque_truck = deque()
    deque_time = deque()
    time = 0
    while truck_weights:
        time += 1
        if deque_time and time - deque_time[0] == bridge_length:
            deque_time.popleft()
            deque_truck.popleft()
        
        if sum(deque_truck) + truck_weights[0] <= weight:
            deque_truck.append(truck_weights.pop(0))
            deque_time.append(time)
    
    return time + bridge_length