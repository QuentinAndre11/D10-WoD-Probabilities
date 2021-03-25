import random

# résultat obtenu en tapant statsLancers( nombre de dés, difficulté, True/False selon si vous avec l'avantage héroïque ou non)
# il est sous la forme [ nombre de succès moyen, taux de réussite, taux d'échec, taux d'échec critique ]

def lancer(des,diff, heros) :
    succes = 0
    L = []

    for i in range(des) :
        L.append(random.randint(1,10))
    L.sort(reverse = True)

    R = []
    for r in L :
        if r == 10 :
            if L[-1] == 1 :
                L.pop()
            else :
                R.append(r)
        else :
            R.append(r)

    for r in R :
        if r == 1 :
            succes -= 1
        elif r == 10 :
            if heros :
                succes += 2
            else :
                succes += 1
        elif r >= diff :
            succes += 1
    return succes

def statsLancers(des,diff,heros) :
    m = 0
    successRate = 0
    failureRate = 0
    criticRate = 0
    for i in range (10000) :
        succes = lancer(des,diff,heros)
        m += succes
        if succes < 0 :
            criticRate +=1
        elif succes == 0 :
            failureRate += 1
        else :
            successRate += 1
    S = [m,successRate,failureRate,criticRate]
    res = []
    for s in S :
        res.append(round(s/100)/100)
    return res

def tableau(heros) :
    T = []
    for des in range (20) :
        print(des)
        T.append([])
        for d in range(10) :
            stats = statsLancers(des+1,d+1,heros)
            T[des].append(stats)
    return T

def afficheSucces(heros) :
    matrice = tableau(heros)
    for ligne in matrice:
       for elt in ligne:
          print(elt[0], end=", ")
       print()