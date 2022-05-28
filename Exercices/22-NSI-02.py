#-------------Exercice 2-------------

def moyenne(tab):
    note=0
    coef=0
    for i in tab:
        note=note+i[0]*i[1]
        coef=coef+i[1]
    return note/coef    


def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
           Ck.append(C[k-1][i-1]+C[k-1][i] ) 
        Ck.append(1)
        C.append(Ck)
    return(C)    



print(pascal(5))
print(moyenne([(15,2),(9,1),(12,3)]))
