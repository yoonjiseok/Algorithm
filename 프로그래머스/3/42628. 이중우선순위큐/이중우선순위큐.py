import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for operation in operations:
        cmd, value = operation.split()
        value = int(value)
        
        if cmd == 'I':
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            
        elif cmd == 'D':
            if value == 1 and max_heap:  
                max_val = -heapq.heappop(max_heap)
                min_heap.remove(max_val) 
                heapq.heapify(min_heap)   
                
            elif value == -1 and min_heap:  
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-min_val)  
                heapq.heapify(max_heap)    
    
    if not min_heap:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]
