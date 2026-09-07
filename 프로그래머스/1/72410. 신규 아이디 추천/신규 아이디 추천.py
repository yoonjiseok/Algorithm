def solution(new_id):
    #1
    new_id = new_id.lower()
    
    a = set()
    for i in range(10):
        a.add(str(i))
    for i in range(97,123):
        a.add(chr(i))
        
    a.add('-')
    a.add('_')
    a.add('.')
    
    #2
    LX = ''
    for char in new_id:
        if char in a:        
            LX += char       
    new_id = LX
    
    #3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
            
            
        
      
    #4
    if len(new_id) >=1:
        if new_id[0] =='.':
            if len(new_id) >=2:
                new_id = new_id[1:]
            else:
                new_id = ''
    
    if len(new_id) >=1:
        if new_id[-1] == '.':
            if len(new_id) >=2:
                new_id = new_id[:-1]
            else:
                new_id = ''
            
    
    #5
    if len(new_id) == 0:
        new_id = 'a'
    
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
        if new_id[-1] == '.':
                new_id = new_id[:-1]
    
    #7
    if 1<= len(new_id) <= 2:
        tempw = new_id[-1]
        while True:
            if len(new_id) == 3:
                break
            new_id += tempw
      
    
    return new_id