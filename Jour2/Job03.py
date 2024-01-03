class Livre :
    def __init__(self,titre,auteur,pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages
        self.disponible = True
    
    def get_titre(self):
        return self.titre
    
    def get_auteur(self):
        return self.auteur
    
    def get_pages(self):
        return self.pages
    
    def set_titre(self, nouvelle_titre):
        self.titre = nouvelle_titre
    
    def set_auteur(self, nouvelle_auteur):
        self.auteur = nouvelle_auteur
    
    def set_pages(self, nouvelle_pages):
        if int(nouvelle_pages) == nouvelle_pages and nouvelle_pages >=0 :
            self.pages = nouvelle_pages
        else :
            print('Il faut que la nouvelle valeur soit positif et entier')

    def verification(self):
        if self.disponible = True:
            return True
        else: 
            return False
        
    def emprunter(self):
        if self.verification():
            self.disponible = False

    def rendre(self):
        if self.verification() == False :
            self.disponible = True