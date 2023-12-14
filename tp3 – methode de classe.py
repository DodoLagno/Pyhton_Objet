# Fichier tp3_methode_de_classe.py

class Zoo:
    # Attributs de classe
    liste_animaux = []
    nombre_total_animaux = 0

    @classmethod
    def ajouter_animaux(cls, espece, nombre):
        # Méthode de classe pour ajouter des animaux au zoo
        animal_existe = False

        # Vérifier si l'espèce existe déjà dans la liste
        for animal in cls.liste_animaux:
            if animal['espece'] == espece:
                animal['nombre'] += nombre
                cls.nombre_total_animaux += nombre
                animal_existe = True
                break

        # Si l'espèce n'existe pas, l'ajouter à la liste
        if not animal_existe:
            cls.liste_animaux.append({'espece': espece, 'nombre': nombre})
            cls.nombre_total_animaux += nombre

    @classmethod
    def afficher_animaux(cls):
        # Méthode de classe pour afficher les animaux du zoo
        print("Animaux dans le ExerciceZoo:")
        for animal in cls.liste_animaux:
            print(f"{animal['espece']}: {animal['nombre']}")

        print(f"Nombre total d'animaux dans le ExerciceZoo: {cls.nombre_total_animaux}")


# Exemple d'utilisation du ExerciceZoo
Zoo.ajouter_animaux("Lion", 3)
Zoo.ajouter_animaux("Tigre", 2)
Zoo.ajouter_animaux("Lion", 2)

Zoo.afficher_animaux()
