class AdressePostale:
    def __init__(self, numero_rue, libelle_rue, code_postal, ville):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville


class Personne:
    def __init__(self, nom, prenom, adresse):
        """

        :param nom:
        :param prenom:
        :param adresse:
        """
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

    def __hash__(self):
        return hash((self._nom, self._prenom, self._adresse))

    def __eq__(self, other):
        return isinstance(other, Personne) and self._nom == other._nom and self._prenom == other._prenom and self._adresse == other._adresse


if __name__ == "__main__":
    # Instanciez deux personnes avec les mêmes valeurs d'attributs
    personne1 = Personne(nom="Doe", prenom="John",
                         adresse=AdressePostale(numero_rue="1", libelle_rue="Street", code_postal="12345",
                                                ville="City"))
    personne2 = Personne(nom="Doe", prenom="John",
                         adresse=AdressePostale(numero_rue="1", libelle_rue="Street", code_postal="12345",
                                                ville="City"))

    # Mettez ces personnes dans un set (avant la redéfinition de __hash__)
    personnes_set_avant = {personne1, personne2}

    # Affichez le contenu du set (avant la redéfinition de __hash__)
    print("Contenu du set avant la redéfinition de __hash__ :", personnes_set_avant)

    # Redéfinissez la méthode __hash__ et __eq__ à l'intérieur de la classe Personne
    # ...

    # Instanciez à nouveau deux personnes avec les mêmes valeurs d'attributs
    personne3 = Personne(nom="Doe", prenom="John",
                         adresse=AdressePostale(numero_rue="1", libelle_rue="Street", code_postal="12345",
                                                ville="City"))
    personne4 = Personne(nom="Doe", prenom="John",
                         adresse=AdressePostale(numero_rue="1", libelle_rue="Street", code_postal="12345",
                                                ville="City"))

    # Mettez ces personnes dans un set (après la redéfinition de __hash__)
    personnes_set_apres = {personne3, personne4}

    # Affichez le contenu du set (après la redéfinition de __hash__)
    print("Contenu du set après la redéfinition de __hash__ :", personnes_set_apres)
