# Fichier tp4_methode_static.py

class ChaineUtils:
    @staticmethod
    def est_anagramme(chaine1, chaine2):
        # Méthode statique pour vérifier si deux chaînes sont des anagrammes
        return sorted(chaine1) == sorted(chaine2)

    @staticmethod
    def comptage_chaine(chaine, sous_chaine):
        # Méthode statique pour compter le nombre d'occurrences d'une sous-chaîne dans une chaîne
        return chaine.count(sous_chaine)


# Exemple d'utilisation
chaine1_example = "listen"
chaine2_example = "silent"

# Vérifier si les chaînes sont des anagrammes
resultat_anagramme = ChaineUtils.est_anagramme(chaine1_example, chaine2_example)
print(f"Les chaînes '{chaine1_example}' et '{chaine2_example}' sont des anagrammes : {resultat_anagramme}")

# Compter le nombre d'occurrences de la sous-chaîne dans la chaîne
sous_chaine_example = "is"
nombre_occurrences = ChaineUtils.comptage_chaine(chaine1_example, sous_chaine_example)
print(f"La sous-chaîne '{sous_chaine_example}' apparaît {nombre_occurrences} fois dans '{chaine1_example}'")
