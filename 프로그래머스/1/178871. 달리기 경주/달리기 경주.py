def solution(players, callings):
    answer = []
    score = 1
    
    tier = {}
    

    for i in range(len(players)):
        tier[players[i]] = i
        
    for i in callings:

        X = tier[i]

        front_player = players[X - 1]

        players[X], players[X - 1] = players[X - 1], players[X]

        tier[i] = X - 1
        tier[front_player] = X

        
        
    return players