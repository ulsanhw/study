def bubble_sort(toto):
    for i in range(len(toto)):
        if(i < len(toto)-1 and toto[i] > toto[i+1]):
            toto[i+1] , toto[i] = toto[i] , toto[i+1]
            if(i != 0 and toto[i-1] > toto[i]):
                toto[i-1] , toto[i] = toto[i] , toto[i-1]
        
    return(toto)
#print(bubble_sort([1,7,3,2]))
#print(bubble_sort([1,7,3,2,4,6,5]))

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

#print(bubble_sort([1,7,3,2]))
#print(bubble_sort([1,7,3,2,4,6,5]))

def insertion_sort(toto_1):
    for i in range(1,len(toto_1)):
        for a in range(i , 0 , -1):
            if toto_1[a] < toto_1[a-1]:
                toto_1[a],toto_1[a-1] = toto_1[a-1],toto_1[a]
        print(toto_1)

            
    return(toto_1)

#print(insertion_sort([31,25,12,22,11]))

def selection_sort(toto_2):
    for i in range(len(toto_2)):
        n = toto_2.index(min(toto_2[i:]))
        toto_2[i] , toto_2[n] = toto_2[n] , toto_2[i]
        
    return(toto_2)
print(selection_sort([3,4,2,5,6,7,1]))


        
            

