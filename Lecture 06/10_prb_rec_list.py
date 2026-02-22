def l(li, i):

    if(i == -1):
        return   
    
    l(li, i - 1)
    print(li[i])
    


li = [1, 2, 3, 4]

l(li, len(li) - 1)
