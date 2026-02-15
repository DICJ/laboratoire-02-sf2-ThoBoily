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
        
        # Si le mana est entre 0 et 100 et qu'il est un int
        if new_mana >= 0 and new_mana <= 100 and isinstance(new_mana, int):

            # Attribution du nouveau mana
            self._mana = new_mana

        else:

            # Message d'erreur
            print("┗ Erreur ⋅ Votre valeur de mana est invalide !")

    def attaquer(self) -> float:
        """Calcul les dégats d'une attaque

        Returns:
            float: Dégats de l'attaque
        """

        # Si le personnage a du mana
        if self.mana > 0:

            # Ajout de 60 à ses dégats
            degat_attaque = (self.attaque + 60)
        else:

            # Dégat de base
            degat_attaque = self.attaque
        
        # Diminuer le mana
        self.diminuer_mana()

        return degat_attaque

    def diminuer_mana(self):
        """Diminue le mana d'une valeur entre 15 et 25
        """

        # Diminution du mana
        self._mana -= randint(15, 25)

    def reset_mana(self):

        # Remet le mana à sa valeur initiale
        self._mana = self._mana_max