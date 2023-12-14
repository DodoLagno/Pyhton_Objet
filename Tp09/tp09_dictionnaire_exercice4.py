# Exercice 4: tp09_dictionnaire_exercice4.py

# Créez une classe Salarie
class Salarie:
    def __init__(self, nom, matricule, service):
        self.nom = nom
        self.matricule = matricule
        self.service = service


# Créez une liste de Salariés
salaries = [
    Salarie("Antoine Dupont", 127, "DSI/JAVA"),
    Salarie("Berthe Casa", 238, "DSI/PHP"),
    Salarie("Fatima Ouassa", 478, "DSI/JAVA"),
    Salarie("Cassian Andor", 156, "DSI/PYTHON"),
    Salarie("Lee Wu", 559, "DSI/PHP"),
    Salarie("Hassan Missen", 96, "DSI/PYTHON"),  # Matricule corrigé
    Salarie("Aurélien PIC", 889, "DSI/JAVA")
]

# Créez un dictionnaire du nombre de salariés par service
nombre_par_service = {}
for salarie in salaries:
    nombre_par_service[salarie.service] = nombre_par_service.get(salarie.service, 0) + 1

# Afficher le résultat
print(nombre_par_service)
