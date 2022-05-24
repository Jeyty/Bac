def moyenne(lst):
    somme = 0
    coef = 0
    for c in lst:
        somme = somme + c[0]*c[1]
        coef = coef + c[1]
        print(somme,coef)
    print("---------")
    return somme/coef


def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    print(C)
print(pascal(12))  
#print(moyenne([(15,2),(9,1),(12,3)]))