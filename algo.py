def bubble_sort(toto):
    for i in range(len(toto)):
        if(i < len(toto)-1 and toto[i] > toto[i+1]):
            toto[i+1] , toto[i] = toto[i] , toto[i+1]
            if(i != 0 and toto[i-1] > toto[i]):
                toto[i-1] , toto[i] = toto[i] , toto[i-1]
        
    return(toto)
print(bubble_sort([1,7,3,2]))
print(bubble_sort([1,7,3,2,4,6,5]))

def go_back(idx, toto):
    if (idx != 0 and toto[idx -1] >  toto[idx]):
        toto[idx-1], toto[idx] = toto[idx], toto[idx-1]
    return toto

def bubble_sort(toto):
    
    lst_len = len(toto)

    for i in range(lst_len):
        if(i < lst_len-1 and toto[i] > toto[i+1]):
            toto[i+1] , toto[i] = toto[i] , toto[i+1]
            toto = go_back(i, toto)
        
    return(toto)

print(bubble_sort([1,7,3,2]))
print(bubble_sort([1,7,3,2,4,6,5]))