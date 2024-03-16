import random

# Liste de mots à deviner
mots = ["gagne", "raptor", "bouteille"]

def choisir_mot_aleatoire():
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre
        else:
            mot_affiche += "_"
    return mot_affiche

def jouer():
    mot_a_deviner = choisir_mot_aleatoire()
    lettres_trouvees = set()
    essais = 0
    points = 0

    while True:
        print("\nMot à deviner :", afficher_mot_cache(mot_a_deviner, lettres_trouvees))
        lettre = input("Entrez une lettre : ").lower()

        if lettre in lettres_trouvees:
            print("Cette lettre a déjà été saisie.")
        elif lettre in mot_a_deviner:
            print("Bonne lettre !")
            lettres_trouvees.add(lettre)
            points += 2
        else:
            print("Lettre incorrecte.")
            points = max(0, points - 3)

        essais += 1

        if essais > 10 or set(mot_a_deviner) == lettres_trouvees:
            break

    print("\nMot à deviner :", mot_a_deviner)
    print("Nombre d'essais :", essais)
    print("Points :", points)

if __name__ == "__main__":
    jouer()

