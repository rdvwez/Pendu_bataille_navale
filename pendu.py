import random

def choisir_mot():
    """Choisit un mot aléatoire parmi une liste prédéfinie."""
    mots = ["gagne", "raptor", "bouteille"]
    return random.choice(mots)

def afficher_mot(mot, lettres_trouvees):
    """Affiche le mot avec les lettres trouvées et des underscores pour les lettres manquantes."""
    affichage = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    return affichage

def jouer_pendu():
    mot_a_deviner = choisir_mot()
    lettres_deja_saisies = []
    essais = 0
    lettres_trouvees = set()

    print("Bienvenue au jeu du Pendu !")

    while essais < 10 and set(mot_a_deviner) != lettres_trouvees:
        print("\nMot à deviner :", afficher_mot(mot_a_deviner, lettres_trouvees))
        print("Lettres déjà saisies :", ", ".join(lettres_deja_saisies))
        lettre = input("Saisissez une lettre : ").lower()

        if lettre in lettres_deja_saisies:
            print("Vous avez déjà saisi cette lettre.")
        else:
            lettres_deja_saisies.append(lettre)
            if lettre in mot_a_deviner:
                lettres_trouvees.add(lettre)
                print("Bonne devinette !")
            else:
                essais += 1
                print("Cette lettre n'est pas dans le mot.")

    if set(mot_a_deviner) == lettres_trouvees:
        print("\nFélicitations ! Vous avez trouvé le mot :", mot_a_deviner)
    else:
        print("\nDommage, vous avez dépassé le nombre d'essais. Le mot était :", mot_a_deviner)

jouer_pendu()
