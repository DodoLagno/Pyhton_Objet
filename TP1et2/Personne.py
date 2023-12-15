from Adresse_Postale import AdressePostale

class Personne:
    def __init__(self, nom, prenom, adresse):
        self._nom = nom
        self._prenom = prenom
        self._adresse = adresse

    def afficher_nom_prenom_majuscules(self):
        print(f"{self._nom.upper()}, {self._prenom.upper()}")

    def modifier_nom(self, nouveau_nom):
        self._nom = nouveau_nom

    def modifier_prenom(self, nouveau_prenom):
        self._prenom = nouveau_prenom

    def modifier_adresse(self, nouvelle_adresse):
        self._adresse = nouvelle_adresse

    def retourner_nom(self):
        return self._nom

    def retourner_prenom(self):
        return self._prenom

    def retourner_adresse(self):
        return self._adresse

    def afficher_attributs(self):
        print(
            f"Nom: {self._nom}, Prénom: {self._prenom}, Adresse: {self._adresse.numero_rue} {self._adresse.libelle_rue}, {self._adresse.code_postal} {self._adresse.ville}")

    def __str__(self):
        return f"Nom: {self._nom}, Prénom: {self._prenom}, Adresse: {self._adresse.numero_rue} {self._adresse.libelle_rue}, {self._adresse.code_postal} {self._adresse.ville}"

    def get_identite(self):
        return f"{self._prenom} {self._nom}"

    def __eq__(self, other):
        return isinstance(other, Personne) and self._nom == other._nom and self._prenom == other._prenom and self._adresse == other._adresse

    def __hash__(self):
        return hash((self._nom, self._prenom, self._adresse))

# Reste du code inchangé
# Créez une instance de AdressePostale
adresse_personne = AdressePostale(numero_rue="Rue de la Paix", libelle_rue="Paris", code_postal="75001", ville="Paris")

# Créez une instance de Personne avec l'adresse créée
une_personne = Personne(nom="Doe", prenom="John", adresse=adresse_personne)

# Créez une nouvelle adresse
nouvelle_adresse_personne = AdressePostale(numero_rue="Rue Royale", libelle_rue="Nice", code_postal="06000",
                                           ville="Nice")

# Modifiez l'adresse de la personne avec la nouvelle adresse
une_personne.modifier_adresse(nouvelle_adresse_personne)

# Affichez les attributs de la personne
print(une_personne)

# Utilisez la nouvelle méthode get_identite
print("Identité de la personne:", une_personne.get_identite())
