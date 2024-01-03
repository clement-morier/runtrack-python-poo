class Student:
    def __init__(self,nom,prenom,numéro,level):
        self.nom = nom
        self.prenom = prenom
        self.numéro = numéro
        self.crédits = 0
        self.level = StudentEval()
    
    def add_crédits(self,ajout):
        if ajout > 0:
            for i in range(ajout):
                self.crédits += 10
    
    def get_credits(self):
        return self.crédits
    
    def StudentEval(self):
        if self.crédits >= 90 :
            return "Excellent"
        if self.crédits >= 80 :
            return "Très bien"
        if self.crédits >= 70 :
            return "Bien"
        if self.crédits >= 60 :
            return "Passable"
        else:
            return "Insuffisant"
    
    def StudentInfo(self)
        print("Nom =", self.nom)
        print("Prénom =", self.prenom)
        print("Id =", self.numéro)
        print("Niveau =", self.level)
        

John_Doe = Student("Doe","John",145)
John_Doe.add_crédits(3)
print(f"Le nombre de crédits de John Doe est de {John_Doe.get_credits()} points")