class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
        self._disponible = False

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, nouveau_titre):
        self._titre = nouveau_titre

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, nouveau_auteur):
        self._auteur = nouveau_auteur

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valeur):
        self._disponible = valeur

    def __repr__(self):
        disponibilite = "Oui" if self.disponible else "Non"
        return f"Titre: {self.titre}, Auteur: {self.auteur}, Disponible: {disponibilite}"


class LivrePapier(Livre):
    def __init__(self, titre, auteur, etat):
        super().__init__(titre, auteur)
        self._etat = etat

    @property
    def etat(self):
        return self._etat

    @etat.setter
    def etat(self, nouveau_etat):
        self._etat = nouveau_etat

    def __repr__(self):
        return super().__repr__() + f", État: {self.etat}"


class LivreNumerique(Livre):
    def __init__(self, titre, auteur, version):
        super().__init__(titre, auteur)
        self._version = version

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, nouvelle_version):
        self._version = nouvelle_version

    def __repr__(self):
        return super().__repr__() + f", Version: {self.version}"
