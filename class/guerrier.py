from personnage import Personnage
from random import randint

class Guerrier(Personnage):

    def __init__(self, nom: str, vie: int, attaque: int, force: int):
        super().__init__(nom, vie, attaque)

        self._force = force

        self.force = force

    @property
    def force(self):
        return self._force 
    
    @force.setter()
    def force(self):

        if self.force >= 0 and self.force <= 50:
            self._force = self.force

        else:
            print("Erreur, votre valeur de force est invalide !")
            self._force = 0

    def attaquer(self) -> float:
        """Calcul les dégats d'une attaque

        Returns:
            float: Dégats de l'attaque
        """

        degat_attaque = (self.attaque + (self.force / 2) + randint(-2, 2))

        return degat_attaque