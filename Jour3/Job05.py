import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self,adversaire,degats): 
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Sélectionnez le niveau de défi (1 pour facile, 2 pour normal, 3 pour difficile): "))

    def lancerJeu(self):
        niveaux = {1: (1000, 500), 2: (1500, 750), 3: (2000, 1000)}
        joueur = Personnage("Joueur", niveaux[self.niveau][0])
        ennemi = Personnage("Ennemi", niveaux[self.niveau][1])
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi,random.randint(1, 1000))
            if ennemi.vie <= 0:
                print("Vous avez gagner !")
                break
            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print("Vous avez perdu !")
                break

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()