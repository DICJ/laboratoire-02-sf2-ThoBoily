class Personnage():

    def __init__(self, nom: str, vie: int, attaque: int):
        self.nom = nom
        self._vie = vie
        self._attaque = attaque

        self.vie = vie
        self.attaque = attaque

    @property
    def vie(self) -> str:
        """Getter de la variable vie

        Returns:
            (str): La vie du personnage
        """

        return self._vie 
    
    @vie.setter
    def vie(self, nouvelle_vie: int):

        if nouvelle_vie >= 0 and nouvelle_vie <= 500 and isinstance(nouvelle_vie, int):
            self._vie = nouvelle_vie

        else:
            print("┗ Erreur ⋅ Votre valeur de vie est invalide !")
            self._vie = 0

    @property
    def attaque(self):
        return self._attaque 
    
    @attaque.setter
    def attaque(self, nouvelle_attaque: int):

        if nouvelle_attaque >= 0 and nouvelle_attaque <= 50 and isinstance(nouvelle_attaque, int):
            self._attaque = nouvelle_attaque

        else:
            print("┗ Erreur ⋅ Votre valeur d'attaque est invalide !")
            self._attaque = 0

    def subir_degat(self, degat: int):
        """Fait subir des dégats au personnage

        Args:
            degat (int): Dégat subi.
        """
        
        self._vie -= degat