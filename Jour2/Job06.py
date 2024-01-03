class Commande:
    def __init__(self, numero_commande):
        selfnumero_commande = numero_commande
        selfplats_commandes = {}
        selfstatut_commande = "en cours"
    
    defcalculer_total(self):
        total = 0
        for plat, details in selfplats_commandes.items():
            total += details[0]  
        return total
    
    def ajouter_plat(self, nom_plat, prix_plat):
        selfplats_commandes[nom_plat] = [prix_plat, "non livré"]

    def annuler_commande(self):
        selfstatut_commande = "annulée"

    def afficher_commande(self):
        total = selfcalculer_total()
        print("Numéro de commande:", selfnumero_commande)
        print("Plats commandés:")
        for plat, details in selfplats_commandes.items():
            print(f"- {plat}: {details[0]} €")
        print(f"Total à payer: {total} €")

    def calculer_tva(self):
        total = self.calculer_total() 
        tva = total * 0.2
        return tva
      