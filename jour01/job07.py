class Personnage:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Exemple d'utilisation de la classe Personnage
personnage1 = Personnage()

# Afficher la position initiale du personnage
print(f"Position initiale : {personnage1.position()}")

# Déplacer le personnage à droite et en bas
personnage1.droite()
personnage1.bas()

# Afficher la nouvelle position du personnage
print(f"Nouvelle position : {personnage1.position()}")

