import string
def solution(new_id):
    answer = ''
    
    a = set()
    lower_list = string.ascii_lowercase
    
    for i in lower_list:
        a.add(i)
    for i in range(0,10):
        a.add(str(i))
    
    a.add('.')
    a.add('_')
    a.add('-')
    
    
    #1
    new_id = new_id.lower()
    
    #2
    temp = new_id
    
    for i in range(len(temp)):
        if temp[i] not in a:
            new_id = new_id.replace(temp[i],'')
    
    #new_id = temp
    
    #3
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    #4
    if len(new_id) >= 1 and new_id[0] == '.':
        new_id = new_id[1:]
    
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    #5
    if len(new_id) == 0:
        new_id = 'a'
    
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
        if len(new_id) >= 1 and new_id[0] == '.':
            new_id = new_id[1:]
    
        if len(new_id) >= 1 and new_id[-1] == '.':
            new_id = new_id[:-1]
    
    #7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += (new_id[-1])
    
    return new_id