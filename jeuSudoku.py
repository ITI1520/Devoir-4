# Groupe 23
# Nom : Nicola Baker - Samuel Dicaire
# Numéro étudiant : 300360908 - 
# Devoir 4 Jeu Sudoku

def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    linge = True

    for i in range (1,9):
        if num == grille[row][i]:
            linge = False
    return linge

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    ligne = True
    for i in range (1,9) :
        if num == grille[i][col]:
            ligne = False
    return ligne


def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    verifier = True
    #1ere ligne:
    if 0<=row<=2:
        for i in range (3) :

            #1ere case:
            if 0<=col<=2:
                for x in range (3) :
                    if grille[i][x] == num :
                        verifier = False

            #2e case:
            elif 3<=col<=5:
                for x in range (3,6) :
                    if grille[i][x] == num :
                        verifier = False

            #3e case:
            elif 6<=col<=8:
                for x in range (6,9) :
                    if grille[i][x] == num :
                        verifier = False
                             
    # MILIEU : 
    elif 3<=row<=5:
        for i in range (3,6) :

            #4e case:
            if 0<=col<=2 :
                for x in range (3) :
                    if grille[i][x] == num :
                        verifier = False
                        
            #5e case:
            elif 3<=col<=5 :
                for x in range (3,6) :
                    if grille[i][x] == num :
                        verifier = False
                        
            #6e case:
            elif 6<=col<=8 :
                for x in range (6,9) :
                    if grille[i][x] == num :
                        verifier = False

    # BAS :
    elif 6<=row<=8:
        for i in range (6,9) :

        #si c'est la 7e case:
            if 0<=col<=2 :
                for x in range (3) :
                    if grille[i][x] == num :
                        verifier = False
                
            #si c'est la 8e case:       
            if 3<=col<=5 :
                for x in range (3,6) :
                    if grille[i][x] == num :
                        verifier = False
                        
            #si c'est la 9e case:
            if 6<=col<=8 :
                for x in range (6,9) :
                    if grille[i][x] == num :
                        verifier = False

    return verifier

def verifierGagner(grille):

    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    
   # A COMPLETER
    gagner = True
    for i in range (9) :
        for x in range (9) :
            if 0 == grille[i][x]:
                gagner = False
    return gagner
  
def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
   * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''  
   # A COMPLETER
   if verifierLigne(grille, row, num) == False:
        valide = False
   elif verifierCol(grille, col, num) == False :
        valide = False
   elif verifierSousGrille(grille, row, col, num) == False:
        valide = False
   else : 
        valide = True

   return valide   

