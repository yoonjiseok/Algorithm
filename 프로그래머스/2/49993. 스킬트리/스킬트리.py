def solution(skill, skill_trees):
    
    cnt = 0
    for skills in skill_trees:
        st = 0
        for j in skills:
            if j in skill:
                if j == skill[st]:
                    st += 1
                else:
                    break
        else:
            cnt+=1
    return cnt