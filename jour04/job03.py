class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs et mutateurs pour longueur
    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    # Assesseurs et mutateurs pour largeur
    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    # Assesseur et mutateur pour hauteur
    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur


# Instanciation de la classe Rectangle
rectangle = Rectangle(longueur=5, largeur=3)
print(f"Longueur du rectangle : {rectangle.get_longueur()}")
print(f"Largeur du rectangle : {rectangle.get_largeur()}")
print(f"Périmètre du rectangle : {rectangle.perimetre()}")
print(f"Surface du rectangle : {rectangle.surface()}")

# Modification des attributs du rectangle
rectangle.set_longueur(8)
rectangle.set_largeur(4)
print(f"Nouvelle longueur du rectangle : {rectangle.get_longueur()}")
print(f"Nouvelle largeur du rectangle : {rectangle.get_largeur()}")
print(f"Nouveau périmètre du rectangle : {rectangle.perimetre()}")
print(f"Nouvelle surface du rectangle : {rectangle.surface()}")

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(longueur=5, largeur=3, hauteur=2)
print(f"Longueur du parallelepipede : {parallelepipede.get_longueur()}")
print(f"Largeur du parallelepipede : {parallelepipede.get_largeur()}")
print(f"Hauteur du parallelepipede : {parallelepipede.get_hauteur()}")
print(f"Volume du parallelepipede : {parallelepipede.volume()}")
