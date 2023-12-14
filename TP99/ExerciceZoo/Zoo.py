# zoo.py
from Zone import SavaneAfricaine, FermeAuxReptiles, Aquarium, ZoneCarnivore, Voliere
from Animal import Animal


class Zoo:
    def __init__(self, nom):
        self.nom = nom
        self.zones = []

    def ajouter_animal(self, animal):
        if animal.comportement == "carnivore" and animal.categorie == "Mammifere":
            self.ajouter_animal_zone(animal, ZoneCarnivore)
        elif animal.comportement != "carnivore" and animal.categorie == "Mammifere":
            self.ajouter_animal_zone(animal, SavaneAfricaine)
        elif animal.categorie == "Poisson":
            self.ajouter_animal_zone(animal, Aquarium)
        elif animal.categorie == "Reptile":
            self.ajouter_animal_zone(animal, FermeAuxReptiles)
        elif animal.categorie == "Oiseau":
            self.ajouter_animal_zone(animal, Voliere)

    def ajouter_animal_zone(self, animal, type_zone):
        for zone in self.zones:
            if isinstance(zone, type_zone):
                zone.animaux.append(animal)
                return
        new_zone = type_zone(f"{type_zone.__name__}_{len(self.zones) + 1}")
        new_zone.animaux.append(animal)
        self.zones.append(new_zone)

    def get_quantite_nourriture(self):
        total_nourriture = 0
        for zone in self.zones:
            total_nourriture += zone.get_quantite_nourriture()
        return total_nourriture

    def afficher_infos(self):
        for zone in self.zones:
            print(f"{zone.nom}:")
            for animal in zone.animaux:
                print(f" - {animal.nom} ({animal.categorie}, {animal.comportement})")


# Test
if __name__ == "__main__":
    zoo_instance = Zoo("Mon Zoo")

    # Ajout de plusieurs animaux
    lion = Animal("Lion", "Mammifere", "carnivore")
    girafe = Animal("Girafe", "Mammifere", "herbivore")
    requin = Animal("Requin", "Poisson", "carnivore")
    serpent = Animal("Serpent", "Reptile", "carnivore")
    aigle = Animal("Aigle", "Oiseau", "carnivore")

    # Ajout des animaux dans le zoo
    zoo_instance.ajouter_animal(lion)
    zoo_instance.ajouter_animal(girafe)
    zoo_instance.ajouter_animal(requin)
    zoo_instance.ajouter_animal(serpent)
    zoo_instance.ajouter_animal(aigle)

    # Affichage des informations
    zoo_instance.afficher_infos()

    # Affichage de la quantité de nourriture
    total_nourriture = zoo_instance.get_quantite_nourriture()
    print(f"\nBesoins totaux en nourriture : {total_nourriture} kg")
