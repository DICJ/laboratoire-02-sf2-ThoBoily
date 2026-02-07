from classes.personnage import Personnage

class Arene():

    def __init__(self, lst_personnage: list):
        
        self._lst_personnage = lst_personnage

    def ajouter_personnage(self, personnage: Personnage):

        self._lst_personnage.append(personnage)

    def afficher_personnages(self):
        
        if len(self._lst_personnage) > 0:

            for index, personnage in enumerate(self._lst_personnage):

                print(f"┃ [{index}] {personnage}")
        
        else:

            print("Vous devez ajouter un personnage à la liste")

    def combattre(self, index_pers_1: int, index_pers_2: int):

        if len(self._lst_personnage) >= 2:

            personnage_1 = self._lst_personnage[index_pers_1]
            personnage_2 = self._lst_personnage[index_pers_2]

            while (personnage_1.vie > 0 and personnage_2.vie > 0):

                degat_attaquant = personnage_1.attaquer()
                personnage_2.subir_degat(degat_attaquant)

                print(f"{personnage_1.nom} inflige {degat_attaquant} à {personnage_2.nom}")

                if personnage_2.vie < 0:
                    break

                degat_attaquant = personnage_2.attaquer()
                personnage_1.subir_degat(degat_attaquant)

                print(f"{personnage_2.nom} inflige {degat_attaquant} à {personnage_1.nom}")

                if personnage_1.vie < 0:
                    break

            if personnage_1.vie > personnage_2.vie:
                print(f"{personnage_1.nom} est le gagnant !")

            else:
                print(f"{personnage_2.nom} est le gagnant !")

        else:

            print("Vous devez minimalement ajouter deux personnages à votre arène pour les faires se combattre !")