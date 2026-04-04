def solution(skill, skill_trees):
    
    word = [i for i in skill]
    
    cnt = 0
    for i in range(len(skill_trees)):
        st = 0
        is_found = False
        for j in range(len(skill_trees[i])):
            if is_found:
                break
            else:
                for l in range(len(skill)):
                    if skill[l] == skill_trees[i][j]:
                        if l != st:
                            is_found = True
                            break
                        else:
                            st += 1
        if not is_found:
            cnt += 1
    
    
    return cnt