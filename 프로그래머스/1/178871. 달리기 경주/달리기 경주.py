def solution(players, callings):
    rank = {val : idx for idx, val in enumerate(players)}     # 실시간 달리기 순위 저장하는 딕셔너리 생성
    for i in callings:                                        
        called = rank[i]                                      # 추월한 선수의 기존 순위 저장  
    
        rank[players[called - 1]] += 1                        # 추월당한 선수의 순위 +1
        rank[i] -= 1                                          # 추월한 선수의 순위 -1
        players[called - 1], players[called] = players[called], players[called - 1]  # 추월한 선수와 추월 당한 선수의 원소 순서를 업데이트     
    
    return players
