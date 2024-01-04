class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"Tâche : {self.titre} | Description : {self.description} | Statut : {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]


# Test pour les classes Tache et ListeDeTaches
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Répondre aux emails", "Vérifier la boîte de réception")
tache3 = Tache("Coder un projet", "Travailler sur le projet X")

liste_taches = ListeDeTaches()
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Afficher toutes les tâches
print("Toutes les tâches :")
liste_taches.afficherListe()

# Supprimer une tâche
print("\nSupprimer la tâche 'Répondre aux emails':")
liste_taches.supprimerTache(tache2)
liste_taches.afficherListe()

# Marquer une tâche comme terminée
print("\nMarquer la tâche 'Faire les courses' comme terminée:")
liste_taches.marquerCommeFinie(tache1)
liste_taches.afficherListe()

# Afficher les tâches à faire
print("\nTâches à faire :")
taches_a_faire = liste_taches.filterListe("à faire")
for tache in taches_a_faire:
    print(tache)
