# exercice 1
import random


def ChargerTable(n):
    tab=[]
    for i in range(n):
        t=random.randint(0,9) #get imber integeer between 0 and 9
        tab.append(t) #add the number to the table
    return tab # retturn the table

def ChargerTableZero(n):
    tab=[]
    for i in range(n):
        tab.append(0)
    return tab

# the main page
n =int(input("give the taille :"))
tab=ChargerTable(n)
print(tab)
print("\n")
max=max(tab)
min=min(tab)
M=max-min
if(n>M):
    P=ChargerTableZero(M+1)
    print(len(P))
    for i in range(n):
        P[tab[i]-min]+=1
    print(P)

    i=0
    j=0
    while(i<M+1):
        if (P[i]!=0):
            tab[j]=i+min
            j+=1
            P[i]-=1
        else:
            i+=1
    print(tab)
else:
    print("the condition is not satisfied !!\n")

