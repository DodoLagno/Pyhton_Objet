# Tp5 - Encapsulation.py

class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
        self._disponible = False

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, nouveau_titre):
        self._titre = nouveau_titre

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, nouveau_auteur):
        self._auteur = nouveau_auteur

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valeur):
        self._disponible = valeur


# Créez une instance de Livre
mon_livre = Livre(titre="Python 101", auteur="John Doe")

# Modifiez les différentes informations du livre avec les setters
mon_livre.titre = "Python 102"
mon_livre.auteur = "Jane Smith"
mon_livre.disponible = True

# Affichez les attributs du Livre en utilisant les getters
print(f"Titre: {mon_livre.titre}")
print(f"Auteur: {mon_livre.auteur}")
print(f"Disponible: {mon_livre.disponible}")
