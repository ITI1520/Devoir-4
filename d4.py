# Devoir 4
# Q1
def transl(d, s):                        # Fonction trans1 qui prend en entrez d(dictionaire), s(string)
    """ (dict, str) -> str """           # Contrat de type
    af = "Unknown"                       # Initialise af a "Unknown"

    if s in d:                           # Vérifie si "s" est une clée dans le dictionaire "d"         
        af = d[s]                        # Si oui on affiche la traduction qui est dans le dictionaire "d"
    elif s in d.values():                # 
        for anglais, value in d.items(): # 
            if value == s:               # Si value est égal a s
                af = anglais             # On initialise af a "anglais"
    return af                            # Retourne la valeur de af
# Q2
def setOp(list1, list2):                                   # Fonction setOp qui prend en entrez list1(list), list2(list)
    """ (List) -> dict  """         # Contrat de type
    list = set(list1 + list2)                              # Initialise list a "set(list1 + list2)" et le tranforme en dictionaire
    return list                                            # Retourne list en dictionaire
# Q3
def matrixMinMax(m):                                       # Fonction matrixMinMax qui prend en entrez une liste avec 2 liste a l'interieure                        
    """ (List) -> Tuple """   # Contrat de type
    maxx, minn = max(m[0]), min(m[0])                      # On initialise maxx a "max(m[0])" et minn a "min(m[0])"
    
 
    rang = 1                                            # On initialise rang avec une valeur de 1
 
    while rang < len(m):                                # Boucle while qui s'exécute tant que rang est plus petit que la longeur de m 
        rangMax, rangMin = max(m[rang]), min(m[rang])   # Initialise ranMax a "max(m[rang])" et rangMin a "max(m[rang])"

        if rangMax > maxx:                              # Si rangMax est supérieur a maxx
            maxx = rangMax                              # maxx devient rangMax
        if rangMin < minn:                              # Si rangMin est inferieur a minn
            minn = rangMin                              # minn devient rangMin
        rang = rang + 1                                 # On fait l'incrementation de la valeur de rang

    return (minn, maxx)                                 # On retourne (minn, maxx) en tuples


# Exemple question 1
print("Question 1")                                                          # Imprimer le message pour la question 1
d = {"apple": "pomme", "banana": "banane", "pear": "poire", "plum": "prune"} # Le dictionaire "d" pour la question 1
# Imprimer les 4 exemples de la question 1
print(transl(d,"pear"))
print(transl(d,"poire"))  
print(transl(d,"appricot"))  
print()

# Exemples question 2
print("Question 2")                 # Imprimer le message pour la question 2
# Imprimer les 4 exemples de la question 2
print(setOp([1,2,2,3],[2,-6,8,7]))
print(setOp([],[1,4,2,4,6]))
print(setOp([1,1,1,1],[]))
print(setOp([1],[2,3,2,2]))
print()                             

# Exemple de la question 3
print("Question 3")                       # Imprimer le message pour la question 3
# Imprimer les 4 exemple de la question 3
print(matrixMinMax([[1,5],[2,8]])) 
print(matrixMinMax([[1,5,10],[2,8,-1]]))
print(matrixMinMax([[2,8,-1]]))
print(matrixMinMax([[1],[1]]))