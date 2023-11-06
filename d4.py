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
    min = m[0][0]
    max = m[0][0]
    
    for val in m:
        for x in val:
            if x < min:
                min = x
            if x > max:
                max = x
    
    return (min, max)


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