# Exercise 1 Labo

def somme_matrices(m_1,m_2) :
    l = len(m_1)
    c = len(m_1[0])

    m_3 = []
    i = 0
    j = 0
    while i < l :
        m_3.append([])    
        while j < c :
            m_3[i].append(m_1[i][j] + m_2[i][j])
            j = j + 1
        i = i + 1
        j = 0

    return m_3

print(somme_matrices([[1,2],[3,4]], [[1,1],[1,1]]))

###################################################


# Devoir 4
# Q1
def transl(d, s):
    """()"""
    af = "Unknown"
    if s in d:
        af = d[s]
    elif s in d.values():
        for englais, value in d.items():
            if value == s:
                af = englais
    return af
# Q2
def setOp(list1, list2):
    """()"""
    list = set(list1 + list2)
    return list
# Q3
def matrixMinMax(m):
    """() pas sur"""
    maxx = max(m[0])
    minn = min(m[0]) # max dans la première rangée
 #utilise la fonction Python max 
    rang = 1 # verification de la rangée 1
 
    while rang < len(m):
        rangMax = max(m[rang])
        rangMin = min(m[rang]) 
        if rangMax > maxx: 
            maxx = rangMax
        if rangMin < minn: 
            minn = rangMin
        rang = rang + 1 
    return (minn, maxx)


# Exemples
print("Question 1")
d = {"apple": "pomme", "banana": "banane", "pear": "poire", "plum": "prune"}
print(transl(d,"pear"))
print(transl(d,"poire"))  
print(transl(d,"appricot"))  
print()

# Exemples 2
print("Question 2")
print(setOp([1,2,2,3],[2,-6,8,7]))
print(setOp([],[1,4,2,4,6]))
print(setOp([1,1,1,1],[]))
print(setOp([1],[2,3,2,2]))
print()

# Exemple 3
print("Question 3")
print(matrixMinMax([[1,5],[2,8]])) 
print(matrixMinMax([[1,5,10],[2,8,-1]]))
print(matrixMinMax([[2,8,-1]]))
print(matrixMinMax([[1],[1]]))