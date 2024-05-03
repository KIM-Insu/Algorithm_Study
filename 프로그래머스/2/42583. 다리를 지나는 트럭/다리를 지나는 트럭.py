from collections import deque
def solution(bridge_length, weight, truck_weights):
    deque_truck = deque()                                         # 다리를 건너는 중인 트럭을 저장할 덱 생성
    deque_time = deque()                                          # 다리에 처음 진입하는 시점을 저장할 덱 생성
    time = 0
    while truck_weights:
        time += 1                                                 # 현재 시점을 저장하는 time 변수를 1초씩 증가시키면서
        if deque_time and time - deque_time[0] == bridge_length:  # 현재 시점 - 다리에 처음 진입한 시점 = bridge_length면, 즉 맨 앞의 트럭이 완전히 다리를 건넜으면
            deque_time.popleft()                                   
            deque_truck.popleft()                                 # 두 덱에서 모두 pop
        
        if sum(deque_truck) + truck_weights[0] <= weight:         # 현재 다리를 건너는 중인 트럭들의 무게 + 대기중인 트럭 중 맨 앞의 트럭의 무게 <= weight 이면,
            deque_truck.append(truck_weights.pop(0))              # 대기열에서 맨 앞의 트럭을 pop하고 다리를 건너는 중인 덱에 append
            deque_time.append(time)                               # 다리에 진입하는 시점의 time을 덱에 append 
    
    return time + bridge_length              # while문이 대기열의 마지막 트럭이 다리에 진입하면 종료되므로 그 시점의 time에 다리를 건너는 시간을 더해서 반환
