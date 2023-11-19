# Groupe 23
# Nom : Nicola Baker - Samuel Dicaire
# Numéro étudiant : 300360908 - 300355587
# Devoir 4 Jeu Sudoku

def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    # CODE AJOUTER ***
    linge = True                     # Initialise la variable "linde" a True

    for i in range (1,9):            # Parcour les collone de la ligne de 1 a 8
        if num == grille[row][i]:    # Regarde si num existe deja dans la ligne
            linge = False            # Si oui on remet la variable "linge" a False
    return linge                     # Retourne la valeur de linge

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    # CODE AJOUTER ***
    ligne = True                     # Initialise la variable "ligne" a True       
    for i in range (1,9) :           # Parcour les ligne de la collone de 1 a 8
        if num == grille[i][col]:    # Regarde si num existe deja dans la collone
            ligne = False            # Si oui on remet la variable "ligne" a False
    return ligne                     # Retourne la valeur de ligne


def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    # CODE AJOUTER ***
    verifier = True          # Initialise la variable "verifier" a True

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

    return verifier                              # Retourne la valeur de verifier

def verifierGagner(grille):

    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    
   # CODE AJOUTER ***
    gagner = True                   # Initialise la variable "gagner" a True
    for i in range (1,9) :            # Regarde toute les ligne et collone de la grille
        for x in range (1,9) :        
            if 0 == grille[i][x]:   # Regarde si il y as une casse qui est egal a 0
                gagner = False      # Si oui on mais "gagner" a False
    return gagner                   # Retourne la valeur de gagner
  
def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
   * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''  

   # CODE AJOUTER ***
   
   ''' Verifie les nombre et si aumoin un des nombre nest pas bon "valide" = False sinon "valide" = True'''

   if verifierLigne(grille, row, num) == False:
        valide = False
   elif verifierCol(grille, col, num) == False :
        valide = False
   elif verifierSousGrille(grille, row, col, num) == False:
        valide = False
   else : 
        valide = True

   return valide                # Retourne la valeur de "valide"

