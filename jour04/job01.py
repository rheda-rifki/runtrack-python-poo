class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"Âge de la personne : {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une personne
personne = Personne()
personne.afficherAge()  # Affiche l'âge par défaut (14) en console

# Instanciation d'un élève
eleve = Eleve()
eleve.afficherAge()  # Affiche l'âge par défaut (14) de la personne en console
