class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instancier un objet Animal
mon_animal = Animal()

# Afficher l'âge initial de l'animal
print(f"Age de l'animal : {mon_animal.age}ans")

# Faire vieillir l'animal
mon_animal.vieillir()

# Afficher le nouvel âge de l'animal
print(f"Age de l'animal après avoir vieilli : {mon_animal.age}ans")

# Nommer l'animal
mon_animal.nommer("L'animal se nomme Fido")

# Afficher le nom de l'animal
print(f"Nom de l'animal : {mon_animal.prenom}")
