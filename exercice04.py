def recherche(tab):
    k=0
    l=[]
    for i in tab:
        if i==(k+1):
            p=[k,i]
            l.append(p)
            print(p)
        k=i
    return l
    
print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))