class Voiture:
    def __init__(self,marque,modèle,année,kilométrage):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.kilométrage = kilométrage
        self.en_marche = False
        self.reservoir = 50

    def get_marque(self):
        return self.marque
    
    def get_modele(self):
        return self.modèle
    
    def get_annee(self):
        return self.année
    
    def get_kilometrage(self):
        return self.kilométrage
    
    def get_en_marche(self):
        return self.en_marche

    def set_marque(self, nouvelle_marque):
        self.marque = nouvelle_marque
    
    def set_modele(self, nouveau_modele):
        self.modèle = nouveau_modele
    
    def set_annee(self, nouvelle_annee):
        self.année = nouvelle_annee
    
    def set_kilometrage(self, nouveau_kilometrage):
        self.kilométrage = nouveau_kilometrage
    
    def set_en_marche(self, en_marche):
        self.en_marche = en_marche
    
    def demarrer(self):
        if self.en_marche :
            print('La voiture est deja en demarrer')
        else:
            if verifier_plein() > 5 :
                self.en_marche = True
            else:
                print("Il n'y a pas asser de carburant")
        
    def arreter(self):
        if self.en_marche = False :
            print('La voiture est deja arreter')
        else:
            self.en_marche = False
        
    def verifier_plein(self):
        return self.reservoir