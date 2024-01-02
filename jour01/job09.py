class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        print(f"Nom du produit : {self.nom}")
        print(f"Prix HT : {self.prixHT}")
        print(f"TVA : {self.TVA}%")
        print(f"Prix TTC : {self.CalculerPrixTTC()}")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

# Créer plusieurs produits
produit1 = Produit("Produit1", 10, 20)
produit2 = Produit("Produit2", 15, 15)

# Afficher les informations des produits
print("Avant modification :")
produit1.afficher()
print("\n")
produit2.afficher()
print("\n")

# Modifier le nom et le prix de chaque produit
produit1.modifierNom("NouveauProduit1")
produit1.modifierPrixHT(12)

produit2.modifierNom("NouveauProduit2")
produit2.modifierPrixHT(18)

# Afficher les nouvelles informations des produits
print("Après modification :")
produit1.afficher()
print("\n")
produit2.afficher()
