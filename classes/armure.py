class Armure():

    def __init__(self, nom: str, points_armure: int):
        self.nom = nom
        self._points_armure = points_armure

        self.points_armure = points_armure

    @property
    def points_armure(self) -> str:

        return self._points_armure 
    
    @points_armure.setter
    def vie(self, nouveau_point_armure: int):

        if nouveau_point_armure >= 0 and nouveau_point_armure <= 15 and isinstance(nouveau_point_armure, int):
            self._points_armure = nouveau_point_armure

        else:
            print("┗ Erreur ⋅ Votre valeur de points d'armure est invalide !")
            self._vie = 0