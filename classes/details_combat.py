class Details_Combats():

    def __init__(self, nom_personnage_1: str, nom_personnage_2: str):

        self._nom_personnage_1 = nom_personnage_1
        self._nom_personnage_2 = nom_personnage_2
        self.vainqueur = ""
        self.nombre_tours = 0

    @property
    def nom_personnage_1(self):
        return self._nom_personnage_1
    
    @property
    def nom_personnage_2(self):
        return self._nom_personnage_2

    def incrementer_tour(self):
        """Incrémente la variable du nombre de tours de un
        """
        self.nombre_tours += 1

    def definir_vainqueur(self, nom_vainqueur: str):
        """Défini la personne entré en argument comme vainqueur

        Args:
            nom_vainqueur (str): Nom du vainqueur
        """

        self.vainqueur = nom_vainqueur