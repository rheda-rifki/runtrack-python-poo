class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True

    # Assesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    # Méthode de vérification de disponibilité
    def verification(self):
        return self.__disponible

    # Méthode d'emprunt
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    # Méthode de rendu
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté, impossible de le rendre.")

# Exemple d'utilisation
mon_livre = Livre("Titre du Livre", "Auteur du Livre", 300)

# Affichage de la disponibilité initiale
print("Le livre est disponible :", mon_livre.verification())

# Emprunt du livre
mon_livre.emprunter()

# Tentative d'emprunt du livre à nouveau
mon_livre.emprunter()

# Rendu du livre
mon_livre.rendre()

# Tentative de rendu du livre à nouveau
mon_livre.rendre()
