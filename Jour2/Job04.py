class Student:
    def __init__(self,nom,prenom,numéro):
        self.nom = nom
        self.prenom = prenom
        self.numéro = numéro
        self.crédits = 0
    
    def add_crédits(self,ajout):
        if ajout > 0:
            for i in range(ajout):
                self.crédits += 10
    
    def get_credits(self):
        return self.crédits

John_Doe = Student("Doe","John",145)
John_Doe.add_crédits(3)
print(f"Le nombre de crédits de John Doe est de {John_Doe.get_credits()} points")