import random

def AlgoNaif(tab):
    for i in tab:
        for j in tab:
            if(i+j==0):
                return (i,j)
    return "i don't find x,y that verifiy x+y=0"

def AlgoOn(tab):
    i=0
    j=len(tab)-1
    while(i<j):
        if(tab[i]+tab[j]==0):
            return (tab[i],tab[j])
        elif(abs(tab[i])>abs(tab[j])):
            i+=1
        else:
            j-=1
    return "not find "


tab=[-5,-3,-1,2,3,6.9]
print(tab)
print(AlgoOn(tab))


