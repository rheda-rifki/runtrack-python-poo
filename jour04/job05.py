import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius**2

# Instanciation de la classe Rectangle
rectangle = Rectangle(largeur=5, hauteur=3)

# Affichage du résultat de la méthode aire pour le rectangle
print(f"L'aire du rectangle est : {rectangle.aire()}")

# Instanciation de la classe Cercle
cercle = Cercle(radius=4)

# Affichage du résultat de la méthode aire pour le cercle
print(f"L'aire du cercle est : {cercle.aire()}")
