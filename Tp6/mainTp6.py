from tp6redefinitionmethode import LivrePapier, LivreNumerique

# Créer une liste contenant 2 livres papier et 2 livres numériques
bibliotheque = [
    LivrePapier(titre="Harry Potter", auteur="J.K. Rowling", etat="Neuf"),
    LivrePapier(titre="Le Seigneur des Anneaux", auteur="J.R.R. Tolkien", etat="Moyen"),
    LivreNumerique(titre="Clean Code", auteur="Robert C. Martin", version="PDF"),
    LivreNumerique(titre="Dune", auteur="Frank Herbert", version="Kindle")
]

# Mettre le premier livre en disponible (True)
bibliotheque[0].disponible = True

# Faire une boucle qui affiche les informations des divers livres
for livre in bibliotheque:
    print(livre)
    print()
