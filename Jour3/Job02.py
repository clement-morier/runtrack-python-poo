class CompteBancaire:
    def __init__(self,numero,nom,prenom,solde,decouvert=False):
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.solde = solde
        self.decouvert = decouvert
    
    def afficher(self):
        print(f"Numéro de compte : {self.numero}")
        print(f"Titulaire : {self.prenom} {self.nom}")
        print(f"Solde : {self.solde} €")

    def afficherSolde(self):
        print(f"Le solde du compte est de {self.solde} €")

    def versement(self,montantversement):
        self.solde += montantversement
        self.afficherSolde()

    def retrait(self,montantretrait):
        if self.solde >= montantretrait or self.decouvert:
            self.solde -= montantretrait
            self.afficherSolde()
        else:
            print("Solde insuffisant pour effectuer le retrait.")

    def agios(self):
        if self.solde < 0 :
            frais = abs(self.solde) * 0.05
            self.solde -= frais
            self.afficherSolde()
        
    def virement(self,reference,compte,montant):
        if self.solde >= montant or self.decouvert:
            self.solde -= montant
            compte.versement(montant)
            print(f"Virement {reference} de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Solde insuffisant pour effectuer le virement.")


compte1 = CompteBancaire("12345", "Doe", "John", 5000)
compte2 = CompteBancaire("54321", "Dupond", "Jean", -500, decouvert=True)

compte1.afficher()
compte2.afficher()

compte1.virement(compte2, 500)