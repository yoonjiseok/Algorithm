def solution(phone_book):

    phone_set = set(phone_book)
    
    for phone in phone_book:

        for j in range(1, len(phone)):
            prefix = phone[:j]
            
   
            if prefix in phone_set:
                return False 
                
    return True