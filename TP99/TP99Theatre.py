# TP99Theatre.py

# Définition de la classe Theatre
class Theatre:
    def __init__(self, nom, capacite_max):
        # Initialisation des attributs de l'instance
        self.nom = nom
        self.capacite_max = capacite_max
        self.total_clients_inscrits = 0
        self.recette_totale = 0

    def inscrire(self, nb_clients, prix_place):
        # Méthode pour inscrire des clients au théâtre
        if self.total_clients_inscrits + nb_clients <= self.capacite_max:
            self.total_clients_inscrits += nb_clients
            recette_actuelle = nb_clients * prix_place
            self.recette_totale += recette_actuelle
            print(f"{nb_clients} clients inscrits avec succès. Recette actuelle : {recette_actuelle}")
        else:
            print("Capacité maximale atteinte. Impossible d'inscrire plus de clients.")

# Mise en oeuvre
if __name__ == "__main__":
    # Créez une instance de Theatre
    theatre_instance = Theatre("Le Grand Théâtre", capacite_max=100)

    # Appelez plusieurs fois la méthode jusqu'à obtention du message d'erreur
    theatre_instance.inscrire(50, 20)
    theatre_instance.inscrire(30, 20)
    theatre_instance.inscrire(40, 20)  # Atteint la capacité maximale

    # Affichez le total de clients inscrits
    print(f"Total de clients inscrits : {theatre_instance.total_clients_inscrits}")

    # Affichez la recette totale de l'établissement
    print(f"Recette totale de l'établissement : {theatre_instance.recette_totale}")
