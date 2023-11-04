# Devoir 4

def transl(d, s):
    
    if s in d:
        af = d[s]

    elif s in d.values():
        for englais, value in d.items():
            if value == s:
                af = englais
    else:
        af = "Unknown"
    return af

d = {"apple": "pomme", "banana": "banane", "pear": "poire", "plum": "prune"}
# Exemples
print(transl(d, "apple"))  
print(transl(d, "banane"))  
print(transl(d, "pear"))  
print(transl(d, "prune"))  
print(transl(d, "cy"))  
