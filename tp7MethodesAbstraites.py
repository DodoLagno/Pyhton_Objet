from tp6redefinitionmethode import LivrePapier, LivreNumerique


# Classe abstraite Sortie
class Sortie:
    def __init__(self, date, livre):
        self.date = date
        self.livre = livre

    def get_montant(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(date={self.date}, livre={self.livre})"


# Classe Emprunt héritant de Sortie
class Emprunt(Sortie):
    def __init__(self, date, livre, duree):
        super().__init__(date, livre)
        self.duree = duree

    def get_montant(self):
        if isinstance(self.livre, LivrePapier):
            return self.duree * 0.5
        elif isinstance(self.livre, LivreNumerique):
            return self.duree * 0.25
        else:
            return 0

    def __repr__(self):
        return f"{self.__class__.__name__}(date={self.date}, livre={self.livre}, duree={self.duree} jours, montant={self.get_montant()}€)"


# Classe Achat héritant de Sortie
class Achat(Sortie):
    def __init__(self, date, livre, montant):
        super().__init__(date, livre)
        self.montant = montant

    def get_montant(self):
        return self.montant

    def __repr__(self):
        return f"{self.__class__.__name__}(date={self.date}, livre={self.livre}, montant={self.montant}€)"


# Fonction pour le montant global d'une liste de sorties
def montant_global(liste_sorties):
    total = sum(sortie.get_montant() for sortie in liste_sorties)
    return total


# Fonction pour le montant total par type de sortie
def montant_par_type(liste_sorties):
    montants = {"Achat": 0, "Emprunt": 0}
    for sortie in liste_sorties:
        if isinstance(sortie, Achat):
            montants["Achat"] += sortie.get_montant()
        elif isinstance(sortie, Emprunt):
            montants["Emprunt"] += sortie.get_montant()

    # Ajout du symbole € à la sortie
    montants["Achat"] = f"{montants['Achat']}€"
    montants["Emprunt"] = f"{montants['Emprunt']}€"

    return montants


# Création d'une liste de sorties
liste_sorties = [
    Achat(date="2023-12-01", livre=LivrePapier("Harry Potter", "J.K. Rowling", etat="Neuf"), montant=20),
    Emprunt(date="2023-12-02", livre=LivreNumerique("Clean Code", "Robert C. Martin", version="PDF"), duree=7),
    Achat(date="2023-12-03", livre=LivrePapier("Le Seigneur des Anneaux", "J.R.R. Tolkien", etat="Moyen"), montant=15),
    Achat(date="2023-12-04", livre=LivreNumerique("Dune", "Frank Herbert", version="Kindle"), montant=25),
    Emprunt(date="2023-12-05", livre=LivrePapier("Python Crash Course", "Eric Matthes", etat="Neuf"), duree=14),
    Achat(date="2023-12-06", livre=LivreNumerique("The Pragmatic Programmer", "Andrew Hunt", version="PDF"),
          montant=30),
    Achat(date="2023-12-07", livre=LivrePapier("1984", "George Orwell", etat="Moyen"), montant=18),
    Emprunt(date="2023-12-08",
            livre=LivreNumerique("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", version="Kindle"), duree=10),
    Achat(date="2023-12-09", livre=LivrePapier("To Kill a Mockingbird", "Harper Lee", etat="Neuf"), montant=22),
    Emprunt(date="2023-12-10", livre=LivreNumerique("The Great Gatsby", "F. Scott Fitzgerald", version="PDF"), duree=5),
]

# Affichage des résultats
print("Liste des sorties:")
for sortie_affichage in liste_sorties:
    print(sortie_affichage)
    print()  # Ajout d'une ligne vide entre chaque sortie

# Utilisation d'un autre nom pour la variable à l'intérieur de la boucle
montant_total = montant_global(liste_sorties)
montants_par_type = montant_par_type(liste_sorties)

print()
print("Montant global:", montant_total, "euros")
print("Montant par type:", montants_par_type)
