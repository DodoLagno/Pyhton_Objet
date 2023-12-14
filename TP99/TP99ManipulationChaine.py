# TP99ManipulationChaine.py

# Import de la classe Salarie depuis le module Entites
from Entites import Salarie

# Déclaration de la chaîne de caractères
chaine = "Durand;Marcel;2 523.5"

premier_caractere = chaine[0]
print("1. Premier caractère: " + premier_caractere)

longueur_chaine = len(chaine)
print("2. Longueur de la chaîne: " + str(longueur_chaine))

index_point_virgule = chaine.index(";")
index_nom_debut = index_point_virgule + 1
index_nom_fin = chaine.index(";", index_nom_debut)
nom = chaine[index_nom_debut:index_nom_fin]
print("4. Nom de famille extrait : " + nom)

nom_majuscules = nom.upper()
print("5. Nom de famille en majuscules: " + nom_majuscules)

nom_minuscules = nom.lower()
print("6. Nom de famille en minuscules: " + nom_minuscules)

morceaux = chaine.split(";")
print("7. Liste obtenue après découpage: " + str(morceaux))

salaire_str = morceaux[2].replace(" ", "")
salaire_float = float(salaire_str)

# Création d'une instance de la classe Salarie
salarie_instance = Salarie(nom=morceaux[0], prenom=morceaux[1], salaire=salaire_float)

# Affichage des attributs de l'instance
print("8-9. Instance de Salarie créée:")
print(f"Nom: {salarie_instance.nom}")
print(f"Prénom: {salarie_instance.prenom}")
print(f"Salaire: {salarie_instance.salaire}")
