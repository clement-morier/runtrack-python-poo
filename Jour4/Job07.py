import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']

        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        if len(self.paquet) > 0:
            return self.paquet.pop(0)
        else:
            return None

jeu = Jeu()
jeu.melanger_paquet()
main_joueur = [jeu.tirer_carte(), jeu.tirer_carte()]
main_croupier = [jeu.tirer_carte(), jeu.tirer_carte()]

def afficher_main(main):
    for carte in main:
        print(f"{carte.valeur} de {carte.couleur}")

print("Main du joueur:")
afficher_main(main_joueur)

print("\nMain du croupier:")
afficher_main(main_croupier)