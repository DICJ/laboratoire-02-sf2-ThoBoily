from classes.personnage import Personnage
from classes.armure import Armure
from random import randint

class Guerrier(Personnage):

    def __init__(self, nom: str, vie: int, attaque: int, armure: Armure, force: int):
        super().__init__(nom, vie, attaque, armure)

        self._force = force

        self.force = force

    def __str__(self):
        return f"┃ Guerrier : {self.nom}, Vie : {self.vie}, Attaque : {self.attaque}, Force : {self.force}, Points d'armures : {self._armure.points_armure}"

    @property
    def force(self):
        return self._force 
    
    @force.setter
    def force(self, new_force: int):
        
        # Si la force est entre 0 et 50 et qu'elle est un int
        if new_force >= 0 and new_force <= 50 and isinstance(new_force, int):

            # Attribution de la nouvelle valeur de force
            self._force = new_force

        else:

            # Message d'erreur
            print("┗ Erreur ⋅ Votre valeur de force est invalide !")

    def attaquer(self) -> float:
        """Calcul les dégats d'une attaque

        Returns:
            float: Dégats de l'attaque
        """

        # Formule des dégats d'une attaque
        degat_attaque = (self.attaque + (self.force / 2) + randint(-2, 2))

        return degat_attaque