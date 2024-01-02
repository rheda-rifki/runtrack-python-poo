class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}."

# Instancier plusieurs personnes avec des valeurs de construction
personne1 = Personne("Doe", "John")
personne2 = Personne("Smith", "Alice")
personne3 = Personne("Dupont", "Pierre")

# Appeler la méthode SePresenter et imprimer en console
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
