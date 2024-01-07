class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimètre(self):
        self.perimètre = 2*self.largeur + 2*self.longueur
        print(self.perimètre)

    def surface(self):
        self.surface = self.longueur * self.largeur
        print(self.surface)

    def getLongueur(self):
        return self.longueur

    def getLargeur(self):
        return self.largeur

    def setLongueur(self, longueur):
        self.longueur = longueur

    def setLargeur(self, largeur):
        self.largeur = largeur
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def getHauteur(self):
        return self.hauteur

    def setHauteur(self, hauteur):
        self.hauteur = hauteur

    def volume(self):
        return self.hauteur * self.getLongueur() * self.getLargeur()

une_personne = Personne()
un_eleve = Eleve()
un_eleve.afficherAge()