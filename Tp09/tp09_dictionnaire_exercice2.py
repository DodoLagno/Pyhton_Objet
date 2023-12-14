# tp09_dictionnaire_exercice2.py

# Mettez en place une fonction qui retourne un dictionnaire de la longueur des clés
def longueur_des_cles(liste_cles):
    return {cle: len(cle) for cle in liste_cles}


# Exemple d'utilisation
liste_cles = ["Coucou", "Hi"]
resultat = longueur_des_cles(liste_cles)
print(resultat)
