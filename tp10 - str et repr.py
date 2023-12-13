# tp10_str_repr.py

class Ville:
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population

    def __str__(self):
        return f"{self.nom} - Population: {self.population}"

    def __repr__(self):
        return f"Ville('{self.nom}', {self.population})"


# Créez une instance de Ville
Brest = Ville("Brest", 1000000)

# Affichez la Ville avec print
print(Brest)

# Affichez la représentation de la Ville avec print
print(repr(Brest))

# Créez une liste de villes
liste_de_villes = [
    Ville("Nantes", 500000),
    Ville("Montpellier", 700000),
    Ville("Rennes", 200000),
]

# Affichez la liste de villes, en utilisant la représentation (__repr__)
print(liste_de_villes)
