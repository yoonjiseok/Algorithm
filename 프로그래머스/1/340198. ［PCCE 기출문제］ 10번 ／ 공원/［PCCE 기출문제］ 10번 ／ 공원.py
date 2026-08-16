def solution(mats, park):

    mats.sort(reverse=True)
    
    rows = len(park)
    cols = len(park[0])
    
    for mat in mats:
        for i in range(rows):
            for j in range(cols):
                
                if i + mat <= rows and j + mat <= cols:
                
                    can_place = True
                    for r in range(i, i + mat):
                        for c in range(j, j + mat):
                            if park[r][c] != "-1":
                                can_place = False
                                break
                        if not can_place:
                            break
                    if can_place:
                        return mat
                        
    return -1