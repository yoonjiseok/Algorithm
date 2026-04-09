import re
from itertools import permutations

def solution(expression):
    answer = 0

    tokens = re.split(r'([-+*])', expression)
    
    operators = ['+', '-', '*']
    for priorities in permutations(operators):
        

        temp_tokens = tokens[:]
        
        
        for op in priorities:
         
            while op in temp_tokens:
               
                idx = temp_tokens.index(op)
                

                num1 = int(temp_tokens[idx - 1])
                num2 = int(temp_tokens[idx + 1])
                
    
                if op == '+':
                    res = num1 + num2
                elif op == '-':
                    res = num1 - num2
                elif op == '*':
                    res = num1 * num2 
                
                temp_tokens[idx-1 : idx+2] = [str(res)]
                

                

        final_result = abs(int(temp_tokens[0]))
        answer = max(answer, final_result)
        
    return answer