def solution(players, callings):
    rank = {val : idx for idx, val in enumerate(players)}
    
    for i in callings:
        called = rank[i]
    
        rank[players[called - 1]] += 1
        rank[i] -= 1
        
        players[called - 1], players[called] = players[called], players[called - 1]
        
    return players