class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée horizontale x : {self.x}")

    def afficherY(self):
        print(f"La coordonnée verticale y : {self.y}")

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y

# Exemple d'utilisation de la classe Point
point1 = Point(2, 3)

# Afficher les coordonnées du point
point1.afficherLesPoints()

# Afficher les coordonnées x et y séparément
point1.afficherX()
point1.afficherY()

# Changer les valeurs de x et y
point1.changerX(5)
point1.changerY(8)

# Afficher à nouveau les coordonnées du point après les modifications
point1.afficherLesPoints()