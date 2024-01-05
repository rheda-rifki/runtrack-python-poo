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
personne.bonjour()  # Affiche "Hello" en console
personne.modifierAge(25)
personne.afficherAge()  # Affiche le nouvel âge (25) en console

# Instanciation d'un élève
eleve = Eleve()
eleve.afficherAge()  # Affiche l'âge par défaut (14) en console
eleve.bonjour()  # Affiche "Hello" en console
eleve.allerEnCours()  # Affiche "Je vais en cours" en console
eleve.modifierAge(16)
eleve.afficherAge()  # Affiche le nouvel âge (16) en console

# Instanciation d'un professeur
professeur = Professeur(matiereEnseignee="Mathématiques", age=35)
professeur.afficherAge()  # Affiche l'âge spécifié (35) en console
professeur.bonjour()  # Affiche "Hello" en console
professeur.enseigner()  # Affiche "Le cours va commencer" en console
