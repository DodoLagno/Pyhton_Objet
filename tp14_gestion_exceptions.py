class PersonneException(Exception):
    pass


class PersonneService:
    @staticmethod
    def valider(personne):
        try:
            # Vérifications des conditions
            if not personne.retourner_nom() or not personne.retourner_nom().strip():
                raise PersonneException("Le nom est obligatoire.")

            if len(personne.retourner_nom().strip()) < 2:
                raise PersonneException("Le nom doit faire au moins 2 caractères.")

            if not personne.retourner_prenom() or not personne.retourner_prenom().strip():
                raise PersonneException("Le prénom est obligatoire.")

            if len(personne.retourner_prenom().strip()) < 2:
                raise PersonneException("Le prénom doit faire au moins 2 caractères.")

            if not personne.retourner_adresse() or not personne.retourner_adresse().strip():
                raise PersonneException("L'adresse est obligatoire.")

            # Si toutes les vérifications passent, aucune exception n'est levée
            print("Personne valide :", personne)

        except PersonneException as e:
            print(f"Erreur de validation : {e}")
        else:
            print("Aucune erreur de validation.")


class Personne:
    def __init__(self, nom, prenom, adresse):
        self._nom = nom
        self._prenom = prenom
        self._adresse = adresse

    def retourner_nom(self):
        return self._nom

    def retourner_prenom(self):
        return self._prenom

    def retourner_adresse(self):
        return self._adresse


# Exemple d'utilisation
if __name__ == "__main__":
    # Créez diverses instances de Personne, certaines avec des erreurs et d'autres sans erreur
    personne_valide = Personne(nom="Doe", prenom="John", adresse="123 Main Street")
    personne_nom_vide = Personne(nom="", prenom="Alice", adresse="456 Second Street")
    personne_nom_trop_court = Personne(nom="A", prenom="Bob", adresse="789 Third Street")
    personne_sans_adresse = Personne(nom="Smith", prenom="Jane", adresse="")
    personne_adresse_vide = Personne(nom="Taylor", prenom="Sam", adresse="   ")

    personne_complete = Personne(nom="Brown", prenom="Emma", adresse="987 Fourth Avenue")
    personne_prenom_trop_court = Personne(nom="Johnson", prenom="M", adresse="654 Fifth Road")

    # Créez une instance de PersonneService
    service = PersonneService()

    # Mettez en œuvre la méthode valider avec try/catch/else
    service.valider(personne_valide)
    service.valider(personne_nom_vide)
    service.valider(personne_nom_trop_court)
    service.valider(personne_sans_adresse)
    service.valider(personne_adresse_vide)

    # Personne complète sans erreurs
    service.valider(personne_complete)

    # Personne avec prénom trop court
    service.valider(personne_prenom_trop_court)
