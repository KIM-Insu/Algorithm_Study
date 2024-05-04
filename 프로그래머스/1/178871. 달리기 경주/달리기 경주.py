def solution(players, callings):
    rank = {players[i] : i for i in range(len(players))}
    
    for i in callings:
        curr = rank[i]
    
        rank[players[curr - 1]] += 1
        rank[i] -= 1
        
        players[curr - 1], players[curr] = players[curr], players[curr - 1]
        
    return players