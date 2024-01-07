class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print('Hello')
    
    def modifierAge(self,newage):
        self.age = newage

class Eleve(Personne):
    def allerEnCours(self):
        print('Je vais en cours')
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

une_personne = Personne()
un_eleve = Eleve()

un_eleve.afficherAge()