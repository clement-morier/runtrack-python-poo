class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def get_longueur(self):
        return self.longueur
    
    def get_largeur(self):
        return self.largeur
    
    def set_longueur(self, nouvelle_longueur):
        self.longueur = nouvelle_longueur
    
    def set_largeur(self, nouvelle_largeur):
        self.largeur = nouvelle_largeur

mon_rectangle = Rectangle(10, 5)

print("Longueur:", mon_rectangle.get_longueur())
print("Largeur:", mon_rectangle.get_largeur())

mon_rectangle.set_longueur(20)
mon_rectangle.set_largeur(7)

print("Nouvelle longueur:", mon_rectangle.get_longueur())
print("Nouvelle largeur:", mon_rectangle.get_largeur())