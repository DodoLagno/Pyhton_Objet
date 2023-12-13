# tp11_redefinition_eq.py

# Définition de la classe Ville
class Ville:
    # Constructeur de la classe Ville avec les attributs nom et population
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population

    # Méthode pour obtenir une représentation lisible de l'objet
    def __str__(self):
        return f"{self.nom} - Population: {self.population}"

    # Méthode pour obtenir une représentation de l'objet pouvant être utilisée pour recréer l'objet
    def __repr__(self):
        return f"Ville('{self.nom}', {self.population})"

    # Redéfinition de la méthode __eq__ pour comparer les attributs de deux objets de type Ville
    def __eq__(self, autre_ville):
        if isinstance(autre_ville, Ville):  # Vérifie si l'autre objet est une instance de Ville
            # Compare les attributs nom et population des deux objets
            return (self.nom == autre_ville.nom) and (self.population == autre_ville.population)
        return False


# Test 1 : Instanciation de deux villes avec des valeurs d'attributs différentes
ville1 = Ville("Paris", 2000000)
ville2 = Ville("Londres", 3000000)
egalite = ville1 == ville2
print(f"Test 1 : Les deux villes sont-elles égales ? {egalite}")

# Test 2 : Deux villes avec le même nom mais une population différente
ville1 = Ville("Paris", 2000000)
ville2 = Ville("Paris", 3000000)
egalite = ville1 == ville2
print(f"Test 2 : Les deux villes sont-elles égales ? {egalite}")

# Test 3 : Deux villes identiques
ville1 = Ville("Paris", 2000000)
ville2 = Ville("Paris", 2000000)
egalite = ville1 == ville2
print(f"Test 3 : Les deux villes sont-elles égales ? {egalite}")

# Test 4 : Comparaison avec un objet non-Ville
ville1 = Ville("Paris", 2000000)
ville2 = "Je ne suis pas une ville"
egalite = ville1 == ville2
print(f"Test 4 : Les deux objets sont-ils égaux ? {egalite}")
