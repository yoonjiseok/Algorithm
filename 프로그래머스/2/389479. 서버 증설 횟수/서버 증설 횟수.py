def solution(players, m, k):
    server = {}
    id = 0
    n = 0
    curr_time = 0
    for i in range(len(players)):
        
        for x in list(server.keys()):
            if server[x]['time'] <= curr_time:
                del server[x]
        
        while (players[i] // m) > len(server):
            server[id] = {'time' : curr_time + k}
            id += 1
            
        curr_time += 1
        
    
    return id