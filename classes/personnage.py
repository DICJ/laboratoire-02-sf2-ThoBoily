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

    @property
    def vie(self) -> str:

        return self._vie 
    
    @property
    def vie_max(self) -> str:

        return self._vie_max 
    
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

        degat_final = degat - self._armure.points_armure
        
        self._vie -= degat_final

    def reset_vie(self):

        self._vie = self._vie_max