def solution(message, spoiler_ranges):
    
    cop_message = set()
    spo_message = set()
    cop_temp = ''
    spo_temp = ''
    
    for i in range(len(message)):
        if message[i] == ' ' or i == len(message)-1:
            if i == len(message) -1:
                cop_temp += message[i]
            
            if spo_temp != '':
                spo_temp += cop_temp
                spo_message.add(spo_temp)
                cop_temp = ''
                spo_temp = ''
            else:
                cop_message.add(cop_temp)
                cop_temp = ''
                    
        else:
            for j in range(len(spoiler_ranges)):
                if spoiler_ranges[j][0]<=i<=spoiler_ranges[j][1]:
                    spo_temp += cop_temp + message[i]
                    cop_temp =''
                    break
            else:
                cop_temp += message[i]
            
        
    answer = 0
    for i in spo_message:
        if i in cop_message:
            continue
        answer+=1
    
    return answer