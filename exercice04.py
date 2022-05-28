def recherche(tab):
    k=0
    l=[]
    for i in tab:
        if i==(k+1):
            p=[k,i]
            l.append(p)
        k=i
    return l
    
#print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))

def recherche(elt,tab):
    for i in range(len(tab)):
        if tab[i]==elt:
            print(tab[i])
        else:
            return -1
        
print(recherche(15,[8, 9, 10, 15]))