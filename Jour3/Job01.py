class Ville:
    def __init__(self, nom, habitants):
        self.nom = nom
        self.habitants = habitants

    def get_habitants(self):
        return self.habitants


class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouterPopulation(self):
        self.ville.habitants += 1


ville_paris = Ville("Paris", 1000000)
ville_marseille = Ville("Marseille", 861635)

print(f"Population de la ville de Paris : {ville_paris.get_habitants()} habitants")
print(f"Population de la ville de Marseille : {ville_marseille.get_habitants()} habitants")

john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(f"Mise a jour de la population de la ville de Paris : {ville_paris.get_habitants()} habitants")
print(f"Mise a jour de la population de la ville de Marseille : {ville_marseille.get_habitants()} habitants")