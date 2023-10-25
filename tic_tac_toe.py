from typing import List

# Définition de la taille de la grille de jeu pour simplifier l'exécution du programme
DIMENSION_GRILLE = 3

def affichage_grille(matrix_modele_jeu: List[List[str]])->None:
    """
    Affiche une grille de jeu représentée par une matrice de Strings
    """
    # On déduit les dimensions de la matrice
    largeur = DIMENSION_GRILLE
    hauteur = DIMENSION_GRILLE

    # Constantes pour aider à l'affichage
    SEPARATEUR_COLONNE = "|"
    SEPARATEUR_LIGNE = "_" * (largeur*2-1) # On a n cases et n-1 séparateurs à chaque ligne

    # Affichage d'une ligne
    for i in range(hauteur):
        ligne_str = ""
        # Affichage d'une case
        for j in range(largeur):
            ligne_str += matrix_modele_jeu[i][j]
            # Séparateur de colonne si on n'est pas à la dernière case de la ligne
            if j < (largeur-1):
                ligne_str += SEPARATEUR_COLONNE
        print(ligne_str)
        # Séparateur de ligne si on n'est pas à la dernière ligne
        if i < (hauteur-1):
            print(SEPARATEUR_LIGNE)

def jouer_symbole(
        symbole_a_jouer: str,
        matrix_modele_jeu: List[List[str]],
        symbole_case_vide: str=" "
    ) -> bool:
    """
    Tente de jouer un symbole dans une case de la grille
    Si la case est vide, joue le symbole et renvoie True
    Sinon, ne joue pas et renvoie False
    """
    # On déduit les coups possibles pour aider à la saisie
    max_colonne = len(matrix_modele_jeu) - 1
    max_ligne = len(matrix_modele_jeu[0]) - 1

    # On récupère les intentions du joueur courant
    ligne = int(input(f"Choisissez une ligne (0-{max_ligne}):\n"))
    colonne = int(input(f"Choisissez une colonne (0-{max_colonne}):\n"))

    # Si la case visée n'est pas vide, on annule le coup
    if matrix_modele_jeu[ligne][colonne] != symbole_case_vide:
        print("Impossible, la case est déjà prise")
        return False
    # Si la case est bien vide, on joue le coup
    matrix_modele_jeu[ligne][colonne] = symbole_a_jouer
    return True

def verifier_grille_gagnee(
        matrix_modele_jeu: List[List[str]],
        symbole_vide: str = " ",
    ) -> bool:
    """
    Vérifie si un joueur a aligné 3 pions sur une ligne, une colonne ou une diagonale de la grille
    On ne comptera pas les cases vides indiquées par le paramètre symbole_vide
    Retourne True si un joueur a gagné, sinon retourne False
    """
    # On déduit les dimensions de la matrice
    hauteur = DIMENSION_GRILLE
    largeur = DIMENSION_GRILLE

    # On génère toutes les valeurs que l'on souhaite vérifier pour les traiter de la même manière
    # On lira les lignes directement depuis la matrice
    lignes = [
        [], [], []
    ]
    # On recomposera les colonnes au fur et à mesure de la lecture de la matrice
    colonnes = [
        [""]*hauteur,
        [""]*hauteur,
        [""]*hauteur,
    ]
    for i in range(hauteur):
        # Lecture directe d'une ligne
        lignes[i] = matrix_modele_jeu[i]
        # Recomposition partielle d'une colonne
        for j in range(largeur):
            colonnes[j][i] = matrix_modele_jeu[i][j]

    # On récupère les cases qui composent les diagonales
    # Cette partie ne marchera pas si on change DIMENSION_GRILLE
    diagonales = [
        [matrix_modele_jeu[0][0], matrix_modele_jeu[1][1], matrix_modele_jeu[2][2]],
        [matrix_modele_jeu[0][2], matrix_modele_jeu[1][1], matrix_modele_jeu[2][0]],
    ]

    data_to_check = lignes + colonnes + diagonales

    # Pour chaque donnée ainsi reconstituée, on vérifie que les 3 symboles qui la composent sont identiques et ne sont pas vides
    for data in data_to_check:
        if symbole_vide != data[0] == data[1] == data[2]:
            # On return directement pour éviter de vérifier l'intégralité de la matrice
            return True
        # équivalent à :
        # if symbole_vide!=data[0] and data[0]==data[1] and data[1]==data[2]:
        #     return True

    return False


def verifier_grille_complete(
        matrix_modele_jeu: List[List[str]],
        symbole_vide: str = " ",
    ) -> bool:
    """
    Vérifie si toutes les cases de la matrice ont été jouées.
    Return True s'il n'y a plus de case vide (indiquées par le paramètre symbole_vide)
    Sinon retourne False
    """
    # On déduit les dimensions de la matrice
    hauteur = DIMENSION_GRILLE
    largeur = DIMENSION_GRILLE

    # On parcourt l'intégralité de la matrice à la recherche d'une case vide
    for i in range(hauteur):
        for j in range(largeur):
            # Si on trouve une case vide, on renvoie directement pour ne pas continuer la lecture
            if matrix_modele_jeu[i][j] == symbole_vide:
                return False

    return True


def play_tic_tac_toe(
        symbole_1: str = "X",
        symbole_2: str = "O",
        symbole_vide: str = " "
    ) -> None:
    """
    Permet de lancer une partie de TicTacToe à deux joueurs sur une grille
    """
    # On initialise une grille totalement vide
    grille = [
        [symbole_vide] * DIMENSION_GRILLE,
        [symbole_vide] * DIMENSION_GRILLE,
        [symbole_vide] * DIMENSION_GRILLE,
    ]
    # Le joueur 1 commence
    symbole = symbole_1
    # On joue tant que personne n'a gagné et que des cases sont libres
    while not(
        verifier_grille_gagnee(grille, symbole_vide) 
        or
        verifier_grille_complete(grille, symbole_vide)
    ):
        affichage_grille(grille)
        # Si le joueur a réussi à placer un pion, on change de joueur (et donc de symbole)
        if (jouer_symbole(symbole, grille)):
            symbole = symbole_1 if symbole==symbole_2 else symbole_2
            # équivalent à
            # if symbole == symbole_1:
            #     symbole = symbole_2
            # else:
            #     symbole = symbole_1
    
    print("La partie est terminée !")
    affichage_grille(grille)

play_tic_tac_toe()

# Qu’aura-t-on besoin de faire, si on souhaite désormais programmer un jeu de
# Puissance 4 
"""
Il faudra modifier la dimension de la grille de jeu, la façon dont un joueur pose un pion et la condition de victoire
- Pour la dimension de la grille, on pourra se référer aux règles officiles (par exemple 6 lignes et 8 colonnes)
    Cela peut être un choix des joueurs, du moment qu'on a au moins 4 lignes et au moins 4 colonnes
- Pour la façon de poser un pion, il faudra uniquement demander dans quelle colonne on souhaite jouer
    La ligne sur laquelle placer le pion sera déterminée automatiquement en fonction du nombre de pions déjà joués dans la colonne
    On placera les nouveaux pions le plus "en bas" possible par rapport à l'affichage de la grille, de sorte à simuler la gravité
- Pour la condition de victoire, il faudra s'assure qu'on trouve une suite de 4 fois le même symbole (hors symbole de case vide)
    Cette suite pourra être trouvée dans chaque ligne, colonne et diagonale
"""