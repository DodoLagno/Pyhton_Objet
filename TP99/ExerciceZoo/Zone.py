# Zone.py

class Zone:
    def __init__(self, nom):
        self.nom = nom
        self.animaux = []


class SavaneAfricaine(Zone):
    def get_quantite_nourriture(self):
        return len(self.animaux) * 100


class FermeAuxReptiles(Zone):
    def get_quantite_nourriture(self):
        return len(self.animaux) * 0.1


class Aquarium(Zone):
    def get_quantite_nourriture(self):
        return len(self.animaux) * 1


class ZoneCarnivore(Zone):
    def get_quantite_nourriture(self):
        return len(self.animaux) * 10


class Voliere(Zone):
    def get_quantite_nourriture(self):
        return len(self.animaux) * 0.25
