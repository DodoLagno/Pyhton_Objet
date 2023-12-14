# tp09_dictionnaire_exercice3.py

# Mettez en place une fonction qui retourne un dictionnaire du nombre d'occurrences des clés
def compter_occurrences(liste_cles):
    return {cle: liste_cles.count(cle) for cle in set(liste_cles)}


# Exemple d'utilisation
liste_cles = ["Ananas", "Banane", "Orange", "Ananas", "Banane"]
resultat = compter_occurrences(liste_cles)
print(resultat)
