from classes.personnage import Personnage
from classes.armure import Armure
from random import randint

class Mage(Personnage):

    def __init__(self, nom: str, vie: int, attaque: int, armure: Armure, mana: int):
        super().__init__(nom, vie, attaque, armure)

        self._mana = mana

        self.mana = mana

        self._mana_max = mana

    def __str__(self):
        return f"┃ Mage : {self.nom}, Vie : {self.vie}, Attaque : {self.attaque}, Mana : {self.mana}, Points d'armures : {self._armure.points_armure}"
        
    @property
    def mana(self):
        return self._mana
    
    @property
    def mana_max(self):
        return self._mana_max

    @mana.setter
    def mana(self, new_mana: int):

        if new_mana >= 0 and new_mana <= 100:
            self._mana = new_mana

        else:
            print("┗ Erreur ⋅ Votre valeur de mana est invalide !")

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
        self._mana -= randint(15, 25)

    def reset_mana(self):

        self._mana = self._mana_max