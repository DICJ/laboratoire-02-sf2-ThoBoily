from personnage import Personnage
from random import randint

class Mage(Personnage):

    def __init__(self, nom: str, vie: int, attaque: int, mana: int):
        super().__init__(nom, vie, attaque)

        self._mana = mana

        self.mana = mana

        
    @property
    def mana(self):
        return self._mana
    
    @mana.setter()
    def mana(self):

        if self.mana >= 0 and self.mana <= 100:
            self._mana = self.mana

        else:
            print("Erreur, votre valeur de mana est invalide !")
            self._mana = 0

    def attaquer(self) -> float:
        """Calcul les dégats d'une attaque

        Returns:
            float: Dégats de l'attaque
        """

        if self.mana > 0:
            degat_attaque = (self.attaque + 60)
        else:
            degat_attaque = self.attaque

        self.diminuer_mana()

        return degat_attaque

    def diminuer_mana(self):
        """Diminue le mana d'une valeur entre 15 et 25
        """
        self.mana -= randint(15, 25)