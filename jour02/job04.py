class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    # Mutateur pour ajouter des crédits
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
            print(f"{credits} crédits ajoutés. Total de crédits : {self.__credits}")
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    # Méthode d'évaluation du niveau (privée)
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode d'affichage des informations de l'étudiant
    def student_info(self):
        print(f"Informations de l'étudiant :")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Identifiant : {self.__numero_etudiant}")
        print(f"Niveau : {self.__level}")

# Instanciation de l'objet représentant l'étudiant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(30)
john_doe.add_credits(20)
john_doe.add_credits(40)

# Affichage des informations de l'étudiant
john_doe.student_info()
