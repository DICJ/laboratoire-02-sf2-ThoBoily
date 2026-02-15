from classes.armure import Armure

class Personnage():

    def __init__(self, nom: str, vie: int, attaque: int, armure: Armure):
        self.nom = nom
        self._vie = vie
        self._attaque = attaque
        self._armure = armure

        self.vie = vie
        self.attaque = attaque
        
        self._vie_max = vie

    def __eq__(self, autre_personnage: 'Personnage'):

        if self.nom == autre_personnage.nom and self.vie == autre_personnage.vie:
            return True
        else:
            return False

    @property
    def vie(self) -> str:
        return self._vie 
    
    @property
    def vie_max(self) -> str:
        return self._vie_max 
    
    @property
    def attaque(self):
        return self._attaque 
    
    @vie.setter
    def vie(self, nouvelle_vie: int):

        # Si la vie est entre 0 et 500 et qu'elle est un int
        if nouvelle_vie >= 0 and nouvelle_vie <= 500 and isinstance(nouvelle_vie, int):

            # Attribution de la nouvelle vie
            self._vie = nouvelle_vie

        else:

            # Message d'erreur
            print("┗ Erreur ⋅ Votre valeur de vie est invalide !")

            # Vie par défaut
            self._vie = 0
    
    @attaque.setter
    def attaque(self, nouvelle_attaque: int):

        
        # Si l'attaque est entre 0 et 50 et qu'elle est un int
        if nouvelle_attaque >= 0 and nouvelle_attaque <= 50 and isinstance(nouvelle_attaque, int):

            # Attribution de la nouvelle attaque
            self._attaque = nouvelle_attaque

        else:

            # Message d'erreur
            print("┗ Erreur ⋅ Votre valeur d'attaque est invalide !")

            # Attque par défaut
            self._attaque = 0

    def subir_degat(self, degat: int):
        """Fait subir des dégats au personnage

        Args:
            degat (int): Dégat subi.
        """

        # Formule des dégat
        degat_final = degat - self._armure.points_armure
        
        # Retirer les dégats à la vie
        self._vie -= degat_final