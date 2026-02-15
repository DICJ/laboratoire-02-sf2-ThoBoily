from classes.personnage import Personnage
from classes.armure import Armure

class Soldat(Personnage):

    def __init__(self, nom: str, vie: int, attaque: int, armure: Armure):
        super().__init__(nom, vie, attaque, armure)

    def __str__(self):
        return f"┃ Soldat : {self.nom}, Vie : {self.vie}, Attaque : {self.attaque}, Points d'armures : {self._armure.points_armure}"

    def subir_degat(self, degat: int):
        """Dégats que le personnage subi

        Args:
            degat (int): Dégat de l'attaque
        """

        self._vie -= degat*0.9

    def attaquer(self) -> int:
        """Calcul des dégats d'une attaque

        Returns:
            int: Les dégats de l'attaque
        """

        # Dégat
        degat_attaque = self.attaque

        return degat_attaque