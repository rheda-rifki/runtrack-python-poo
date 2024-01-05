import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, cible):
        degats = random.randint(5, 20)
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts.")
        cible.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 normal, 3 difficile) : "))

    def lancerJeu(self):
        self.choisirNiveau()

        # Initialisation des personnages en fonction du niveau
        if self.niveau == 1:
            joueur = Personnage("Hakim", 100)
            ennemi = Personnage("Maxence", 50)
        elif self.niveau == 2:
            joueur = Personnage("Hakim", 80)
            ennemi = Personnage("Maxence", 60)
        elif self.niveau == 3:
            joueur = Personnage("Hakim", 60)
            ennemi = Personnage("Maxence", 80)
        else:
            print("Niveau invalide. Choisissez un niveau entre 1 et 3.")
            return

        print(f"Vous commencez le combat contre l'ennemi {ennemi.nom} avec {joueur.vie} points de vie.")

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            print(f"{ennemi.nom} a maintenant {ennemi.vie} points de vie.")

            if ennemi.vie <= 0:
                print(f"Félicitations, vous avez vaincu {ennemi.nom} !")
                break

            ennemi.attaquer(joueur)
            print(f"{joueur.nom} a maintenant {joueur.vie} points de vie.")

            if joueur.vie <= 0:
                print(f"{ennemi.nom} a vaincu {joueur.nom}. Game Over.")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()
