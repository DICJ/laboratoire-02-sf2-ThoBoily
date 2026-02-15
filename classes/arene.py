from classes.personnage import Personnage
from classes.details_combat import Details_Combats

from random import randint

class Arene():

    def __init__(self, lst_personnage: list, lst_historique: list):
        
        self._lst_personnage: list[Personnage] = lst_personnage
        self._lst_historique: list[Details_Combats] = lst_historique

    def __len__(self):

        compteur_personnages = 0

        for personnage in self._lst_personnage:

            if personnage.vie > 0:

                compteur_personnages += 1

        return f"┃ Il y a {compteur_personnages} personnages qui sont prêts à combattres !"

    @property
    def lst_personnage(self):
        return self._lst_personnage
    
    @property
    def lst_historique(self):
        return self._lst_historique

    def ajouter_personnage(self, personnage: Personnage):
        """Ajoute le personnage en argument dans la liste

        Args:
            personnage (Personnage): Personnage à ajouter
        """

        self._lst_personnage.append(personnage)

    def afficher_personnages(self):
        """Affiche les personnages contenus dans la liste des personnages
        """
        
        if len(self._lst_personnage) > 0:

            for index, personnage in enumerate(self._lst_personnage):
                        
                print(f"┃ [{index}] {personnage}")
        
        else:

            print("┗ Erreur ⋅ Vous devez ajouter un personnage à la liste")

    def combattre(self, index_pers_1: int, index_pers_2: int) -> Details_Combats:
        """Faire combattre deux personnages ensembles

        Args:
            index_pers_1 (int): Position (index) du personnage 1 dans la liste
            index_pers_2 (int): Position (index) du personnage 1 dans la liste

        Returns:
            Details_Combats: L'historique du combat
        """

        personnage_1 = self._lst_personnage[index_pers_1]
        personnage_2 = self._lst_personnage[index_pers_2]

        detail = Details_Combats(personnage_1, personnage_2)

        if personnage_1.vie >= 0 and personnage_2.vie >= 0:

            while (personnage_1.vie >= 0 and personnage_2.vie >= 0):

                degat_attaquant = personnage_1.attaquer()
                personnage_2.subir_degat(degat_attaquant)

                print(f"┃ {personnage_1.nom} inflige {degat_attaquant} à {personnage_2.nom}")

                if personnage_2.vie <= 0:
                    gagnant = 0
                    detail.incrementer_tour()
                
                    break

                degat_attaquant = personnage_2.attaquer()
                personnage_1.subir_degat(degat_attaquant)

                print(f"┃ {personnage_2.nom} inflige {degat_attaquant} à {personnage_1.nom}")

                if personnage_1.vie <= 0:
                    gagnant = 1
                    detail.incrementer_tour()

                    break
                
                detail.incrementer_tour()

            if personnage_1.vie < 0:
                print(f"┃ {personnage_2.nom} est le gagnant !")
                detail.definir_vainqueur(personnage_2)

            elif personnage_2.vie < 0:
                print(f"┃ {personnage_1.nom} est le gagnant !")
                detail.definir_vainqueur(personnage_1)
            
            self.lst_historique.append(detail)
        
        else:
            print("┗ Erreur ⋅ Un de vos personnages est déjà mort")
    
    def afficher_historique(self, lst_historique: list):
        """Affiche l'historique des combats

        Args:
            lst_historique (list): Liste des historiques des combats
        """

        for num_combat, combat in enumerate(lst_historique):
            print(f"┃ Combat #{num_combat}\n┃")
            print(f"┃ Nom Personnage 1 : {combat.nom_personnage_1.nom}")
            print(f"┃ Nom Personnage 2 : {combat.nom_personnage_2.nom}")
            print(f"┃ Nom Gagnant : {combat.vainqueur.nom}")
            print(f"┃ Nombre de tour : {combat.nombre_tours}")
            print("┃\n┃")

    def soigner_personnage(self, index_personnage: int, lst_personnage: list):

        personnage = lst_personnage[index_personnage]

        personnage.vie = personnage.vie_max


    def nettoyer_arene(self, lst_personnage: list):

        for personnage in lst_personnage:

            if personnage.vie <= 0:

                lst_personnage.remove(personnage)

    def battle_royal(self, lst_personnage: list):

        combat = True

        lst_personnage_tmp = list(lst_personnage)

        while combat:

            if len(lst_personnage_tmp) != 1:

                index_personnage_1 = randint(0, (len(lst_personnage_tmp)-1))
                index_personnage_2 = randint(0, (len(lst_personnage_tmp)-1))

                if index_personnage_1 == index_personnage_2:
                    continue

                else:

                    personnage_1 = lst_personnage_tmp[index_personnage_1]
                    personnage_2 = lst_personnage_tmp[index_personnage_2]

                    degat_personnage_1 = personnage_1.attaquer()
                    personnage_2.subir_degat(degat_personnage_1)
                    
                    print(f"┃ {personnage_1.nom} inflige {degat_personnage_1} à {personnage_2.nom}")

                    if personnage_2.vie <= 0:

                        
                        print(f"┃ {personnage_2.nom} est mort")
                        
                        lst_personnage_tmp.remove(personnage_2)

            else:
            
                print(f"┃ {lst_personnage_tmp[0].nom} est le gagnant !")

                combat = False
