from classes.guerrier import Guerrier
from classes.armure import Armure

class Berserker(Guerrier):
    def __init__(self, nom: str, vie: int, attaque: int, armure: Armure, force: int):
        super().__init__(nom, vie, attaque, armure, force)

    def __str__(self):
        return f"┃ Berserker : {self.nom}, Vie : {self.vie}, Attaque : {self.attaque}, Force : {self.force}, Points d'armures : {self._armure.points_armure}"

    def attaquer(self):

        # Vie perdu
        diff_vie = self.vie_max - self.vie

        # Nombre de fois qu'il faut lui attribuer le bonus
        nb_fois_bonus = diff_vie // 10

        # Nouveau dégat de ses attaques
        degat_attaque = super().attaquer() + nb_fois_bonus * 5

        return degat_attaque
    

    def subir_degat(self, degat):
        
        # Si il est a 50% et moin de sa vie
        if self.vie // self.vie_max < 0.5:

            # Impression du message
            print(f"┃ Le Berserker {self.nom} entre en FUREUR !")

        return super().subir_degat(degat)