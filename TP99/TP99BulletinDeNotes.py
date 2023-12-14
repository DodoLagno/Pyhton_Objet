from datetime import datetime
import random

class Note:
    def __init__(self, valeur, date):
        self.valeur = valeur
        self.date = date

class Discipline:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, valeur):
        self.notes.append(Note(valeur, datetime.now()))

class Etudiant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Bulletin:
    def __init__(self, etudiant):
        self.etudiant = etudiant
        self.disciplines = []

    def ajouter_discipline(self, discipline):
        self.disciplines.append(discipline)

    def ajouter_note(self, discipline, valeur):
        for disc in self.disciplines:
            if disc.nom == discipline:
                disc.ajouter_note(valeur)
                return
        print(f"Discipline '{discipline}' non trouvée.")

    def calculer_moyenne(self):
        moyennes = {}
        for disc in self.disciplines:
            if disc.notes:
                moyennes[disc.nom] = sum(note.valeur for note in disc.notes) / len(disc.notes)
            else:
                moyennes[disc.nom] = 0
        return moyennes

    def afficher_moyenne(self):
        moyennes = self.calculer_moyenne()
        print(f"Moyennes de {self.etudiant.prenom} {self.etudiant.nom}:")
        for discipline, moyenne in moyennes.items():
            print(f"{discipline}: {moyenne:.2f}")

# Exemple d'utilisation
if __name__ == "__main__":
    etudiant = Etudiant("Dupont", "Jean")
    bulletin = Bulletin(etudiant)

    disciplines = ["Maths", "Physique", "Anglais", "Français", "Espagnol", "Sport"]

    for discipline_nom in disciplines:
        discipline = Discipline(discipline_nom)
        bulletin.ajouter_discipline(discipline)

        # Ajout de 10 notes par discipline
        for _ in range(10):
            valeur_note = random.uniform(10, 20)  # Valeur de la note entre 10 et 20
            bulletin.ajouter_note(discipline_nom, valeur_note)

    # Affichage des informations
    bulletin.afficher_moyenne()
