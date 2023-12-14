# Définition de la classe AdressePostale
class AdressePostale:
    def __init__(self, numero_rue, libelle_rue, code_postal, ville):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville  # Ajout de l'attribut 'ville'


# Création de deux instances d'AdressePostale
adresse1 = AdressePostale(numero_rue=123, libelle_rue="Rue de la Paix", code_postal="75001", ville="Paris")
adresse2 = AdressePostale(numero_rue=456, libelle_rue="Avenue des Champs-Élysées", code_postal="75008", ville="Paris")

# Affichage des instances AdressePostale avec la fonction print
print("Adresse 1:")
print(f"{adresse1.numero_rue} {adresse1.libelle_rue}, {adresse1.code_postal} {adresse1.ville}")

print("\nAdresse 2:")
print(f"{adresse2.numero_rue} {adresse2.libelle_rue}, {adresse2.code_postal} {adresse2.ville}")
