def merge_list(l1, l2):
    if(not isinstance(l1,list) or not isinstance(l2,list)):
        raise TypeError()
        
    for val in l1:
            if not isinstance(val, int):
                raise TypeError
                
    for val in l2:
            if not isinstance(val, int):
                raise TypeError
    
    l1.extend(l2)
    
    for i in range(len(l1)):
        for j in range(i,0,-1):
            if (l1[j] < l1[j-1]):
                temp = l1[j]
                l1[j] = l1[j-1]
                l1[j-1] = temp
            else:
                break
                
    return l1


