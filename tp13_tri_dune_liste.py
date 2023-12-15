class AdressePostale:
    def __init__(self, numero_rue, libelle_rue, code_postal, ville):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville


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

    def afficher_details(self):
        print(f"Nom: {self._nom}, Prénom: {self._prenom}, Adresse: {self._adresse.numero_rue} {self._adresse.libelle_rue}, {self._adresse.code_postal} {self._adresse.ville}")

    def __str__(self):
        return f"Nom: {self._nom}, Prénom: {self._prenom}, Adresse: {self._adresse.numero_rue} {self._adresse.libelle_rue}, {self._adresse.code_postal} {self._adresse.ville}"

    def get_identite(self):
        return f"{self._prenom} {self._nom}"

    def __lt__(self, other):
        return self._nom < other._nom

# ...

if __name__ == "__main__":
    # Créez une liste de personnes
    personnes = [
        Personne(nom="Doe", prenom="John", adresse=AdressePostale(numero_rue="1", libelle_rue="Street", code_postal="12345", ville="City")),
        Personne(nom="Smith", prenom="Alice", adresse=AdressePostale(numero_rue="2", libelle_rue="Avenue", code_postal="67890", ville="Town")),
        Personne(nom="Johnson", prenom="Bob", adresse=AdressePostale(numero_rue="3", libelle_rue="Boulevard", code_postal="45678", ville="Village"))
    ]

    # Affichez la liste non triée
    print("Liste non triée :")
    for personne in personnes:
        personne.afficher_details()

    # Triez la liste par nom
    personnes_triees_nom = sorted(personnes)
    print("\nListe triée par nom :")
    for personne in personnes_triees_nom:
        personne.afficher_details()

    # Triez la liste par prénom
    personnes_triees_prenom = sorted(personnes, key=lambda x: x._prenom)
    print("\nListe triée par prénom :")
    for personne in personnes_triees_prenom:
        personne.afficher_details()
