poids =   [3,6,3,2,4,5,2,6,8,6,9]
utilite = [30,54,24,14,24,25,8,36,10,24,18]

capaciteSac1 = 16
capaciteSac2 = 24

sac1 = []
sac2 = []

def calculerUtilite(poids, utilite):
    poidsUtilite = []
    for i in range(len(poids)):
        poidsUtilite.append((utilite[i] / poids[i]))
    return print (poidsUtilite)

calculerUtilite(poids, utilite)

def trierSelonUtilitDecroissante(calculerUtilite):
    poidsUtilite = calculerUtilite
    poidsUtilite.sort(reverse=True)
    return print (poidsUtilite)


def insertionSac1et2(poids, utilite, capaciteSac1, capaciteSac2):
    poidsSac1 = []
    poidsSac2 = []
    utiliteSac1 = []
    utiliteSac2 = []
    for i in range(len(poids)):
        if poids[i] <= capaciteSac1:
            poidsSac1.append(poids[i])
            utiliteSac1.append(utilite[i])
        else:
            poidsSac2.append(poids[i])
            utiliteSac2.append(utilite[i])
    return print (poidsSac1, utiliteSac1, poidsSac2, utiliteSac2)


#Appels
print("trierSelonUtilitDecroissante(calculerUtilite(poids, utilite))")
trierSelonUtilitDecroissante(calculerUtilite(poids, utilite))

print("insertionSac1et2(poids, utilite, capaciteSac1, capaciteSac2)")
insertionSac1et2(poids, utilite, capaciteSac1, capaciteSac2)










