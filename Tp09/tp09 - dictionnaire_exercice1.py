# tp09_dictionnaire_exercice1.py

# Créer un dictionnaire nommé dicoVilles
dicoVilles = {13: "Marseille", 34: "Montpellier", 44: "Nantes", 75: "Paris", 31: "Toulouse"}

# Afficher les clés du dictionnaire
print("Clés du dictionnaire:")
for key in dicoVilles.keys():
    print(key)

# Afficher les valeurs du dictionnaire
print("\nValeurs du dictionnaire:")
for value in dicoVilles.values():
    print(value)

# Afficher la taille du dictionnaire
print("\nTaille du dictionnaire:", len(dicoVilles))
