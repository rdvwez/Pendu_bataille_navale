import random

# Création d'une matrice 2D pour représenter l'état des bateaux
TAILLE_GRILLE = 10
bateau_vide = 0
bateau_non_coule = 1
bateau_coule = 2
tir_rate = 3

def creer_grille():
    return [[bateau_vide] * TAILLE_GRILLE for _ in range(TAILLE_GRILLE)]

def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(str(case) for case in ligne))

def placer_bateaux(grille, nb_bateaux):
    for _ in range(nb_bateaux):
        x, y = random.randint(0, TAILLE_GRILLE - 1), random.randint(0, TAILLE_GRILLE - 1)
        while grille[x][y] != bateau_vide:
            x, y = random.randint(0, TAILLE_GRILLE - 1), random.randint(0, TAILLE_GRILLE - 1)
        grille[x][y] = bateau_non_coule

def jouer():
    joueur = creer_grille()
    ordinateur = creer_grille()
    nb_bateaux = 5

    placer_bateaux(joueur, nb_bateaux)
    placer_bateaux(ordinateur, nb_bateaux)

    while True:
        print("\nGrille du joueur :")
        afficher_grille(joueur)
        print("\nGrille de l'ordinateur :")
        afficher_grille(ordinateur)

        x, y = map(int, input("\nEntrez les coordonnées (x y) pour tirer : ").split())
        if joueur[x][y] == bateau_non_coule:
            print("Touché !")
            joueur[x][y] = bateau_coule
        elif joueur[x][y] == bateau_coule:
            print("Déjà touché ici !")
        else:
            print("Raté !")
            joueur[x][y] = tir_rate

        # Vérification si tous les bateaux ont été coulés
        if all(all(case == bateau_coule for case in ligne) for ligne in joueur):
            print("Félicitations ! Vous avez gagné !")
            break

        # L'ordinateur tire aléatoirement
        x, y = random.randint(0, TAILLE_GRILLE - 1), random.randint(0, TAILLE_GRILLE - 1)
        if ordinateur[x][y] == bateau_non_coule:
            print("L'ordinateur a touché votre bateau !")
            ordinateur[x][y] = bateau_coule
        else:
            print("L'ordinateur a raté son tir.")

        # Vérification si tous les bateaux de l'ordinateur ont été coulés
        if all(all(case == bateau_coule for case in ligne) for ligne in ordinateur):
            print("L'ordinateur a gagné !")
            break

if __name__ == "__main__":
    jouer()
