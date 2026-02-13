from classes.personnage import Personnage
from classes.armure import Armure
from random import randint

class Archer(Personnage):

    def __init__(self, nom: str, vie: int, attaque: int, armure: Armure, dexterite: int):
        super().__init__(nom, vie, attaque, armure)

        self._dexterite = dexterite

        self.dexterite = dexterite

    def __str__(self):
        return f"┃ Archer : {self.nom}, Vie : {self.vie}, Attaque : {self.attaque}, Dextérité : {self.dexterite}, Points d'armures : {self._armure.points_armure}"

    @property
    def dexterite(self):
        return self._dexterite
    
    @dexterite.setter
    def dexterite(self, new_dexterite: int):

        if new_dexterite >= 40 and new_dexterite <= 70:
            self._dexterite = new_dexterite

        else:
            print("┗ Erreur ⋅ Votre valeur de dexterité est invalide !")

    def attaquer(self) -> float:
        """Calcul les dégats d'une attaque

        Returns:
            float: Dégats de l'attaque
        """

        nb_aleatoire = randint(0, 100)

        degat_attaque = self.attaque + 15

        if nb_aleatoire < self._dexterite:
            degat_attaque *= 2

        return degat_attaque