class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self._numero = numero
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self._numero}")
        print(f"Nom : {self._nom}")
        print(f"Prénom : {self._prenom}")
        print(f"Solde : {self._solde}")
        print(f"Autorisation de découvert : {self._decouvert}")

    def afficherSolde(self):
        print(f"Le solde du compte est de : {self._solde}")

    def versement(self, montant):
        self._solde += montant
        print(f"Versement de {montant} effectué. Nouveau solde : {self._solde}")

    def retrait(self, montant):
        if self._solde - montant >= 0 or self._decouvert:
            self._solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde : {self._solde}")
        else:
            print("Opération impossible : solde insuffisant.")

    def agios(self, taux):
        if self._solde < 0:
            agios = abs(self._solde) * taux
            self._solde -= agios
            print(f"Agios appliqués. Nouveau solde : {self._solde}")

    def virement(self, compte_destinataire, montant):
        if self._solde - montant >= 0 or self._decouvert:
            self._solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} effectué vers le compte {compte_destinataire._numero}.")
        else:
            print("Opération impossible : solde insuffisant.")


# Création des instances de la classe CompteBancaire
compte1 = CompteBancaire(12345, "Doe", "John", 1000)
compte2 = CompteBancaire(54321, "Smith", "Jane", -500, decouvert=True)

# Affichage des détails des comptes
print("Compte 1:")
compte1.afficher()

print("\nCompte 2:")
compte2.afficher()

# Effectuer un versement du compte 1 vers le compte 2 pour remettre le compte 2 à zéro
compte1.virement(compte2, 500)

# Affichage des nouveaux solde après le virement
print("\nNouveaux soldes après virement:")
compte1.afficherSolde()
compte2.afficherSolde() 
