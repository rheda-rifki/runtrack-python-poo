class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Prix: {self.prix} $")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print("Vroum vroum! La moto démarre.")


# Instanciation d'un objet Voiture
voiture = Voiture(marque="Nissan", modele="GT-R34", annee=2002, prix=100000)
voiture.informationsVehicule()
voiture.demarrer()

# Instanciation d'un objet Moto
moto = Moto(marque="MT 07", modele="Roadster", annee=2022, prix=10000)
moto.informationsVehicule()
moto.demarrer()
