from classes.personnage import Personnage
from classes.details_combat import Details_Combats

from random import randint

class Arene():

    def __init__(self, lst_personnage: list, lst_historique: list):
        
        self._lst_personnage: list[Personnage] = lst_personnage
        self._lst_historique: list[Details_Combats] = lst_historique

    def __len__(self):
        
        # Compteur de personnages
        compteur_personnages = 0

        # Itération de la liste de personnages
        for personnage in self._lst_personnage:
            
            # Si le personnage est vivant
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

        # Ajout du personnage à la liste
        self._lst_personnage.append(personnage)

    def afficher_personnages(self):
        """Affiche les personnages contenus dans la liste des personnages
        """
        
        # Si il y a au mois un personnages dans la liste de personnages
        if len(self._lst_personnage) > 0:
            
            # Itération de la liste
            for index, personnage in enumerate(self._lst_personnage):
                
                # Impression de la liste des personnages
                print(f"┃ [{index}] {personnage}")
        
        else:
            
            # Message d'erreur
            print("┗ Erreur ⋅ Vous devez ajouter un personnage à la liste")

    def combattre(self, index_pers_1: int, index_pers_2: int) -> Details_Combats:
        """Faire combattre deux personnages ensembles

        Args:
            index_pers_1 (int): Position (index) du personnage 1 dans la liste
            index_pers_2 (int): Position (index) du personnage 1 dans la liste

        Returns:
            Details_Combats: L'historique du combat
        """

        # Récupération des deux personnages
        personnage_1 = self._lst_personnage[index_pers_1]
        personnage_2 = self._lst_personnage[index_pers_2]

        # Initialisation des détails pour le combat
        detail = Details_Combats(personnage_1, personnage_2)

        # Si les personnages ne sont pas déjà mort
        if personnage_1.vie >= 0 and personnage_2.vie >= 0:
            
            # Tant que les personnages ne sont pas mort
            while (personnage_1.vie >= 0 and personnage_2.vie >= 0):
                
                # Dégats d'attaque du perso1 
                degat_attaquant = personnage_1.attaquer()

                # Attaque du perso1
                personnage_2.subir_degat(degat_attaquant)
                print(f"┃ {personnage_1.nom} inflige {degat_attaquant} à {personnage_2.nom}")

                # Si le perso2 est mort
                if personnage_2.vie <= 0:

                    # Ajouter un tour
                    detail.incrementer_tour()
                
                    break
                
                # Dégats d'attaque du perso2
                degat_attaquant = personnage_2.attaquer()

                # Attaque du perso1
                personnage_1.subir_degat(degat_attaquant)
                print(f"┃ {personnage_2.nom} inflige {degat_attaquant} à {personnage_1.nom}")

                # Si le perso1 est mort
                if personnage_1.vie <= 0:

                    # Ajouter un tour
                    detail.incrementer_tour()

                    break
                
                # Ajouter un tour
                detail.incrementer_tour()

            # Si le perso1 est mort
            if personnage_1.vie < 0:

                # Vainqueur
                print(f"┃ {personnage_2.nom} est le gagnant !")
                detail.definir_vainqueur(personnage_2)

            # Si le perso2 est mort
            elif personnage_2.vie < 0:
                
                # Vainqueur
                print(f"┃ {personnage_1.nom} est le gagnant !")
                detail.definir_vainqueur(personnage_1)
            
            # Ajouter l'historique du combat à la liste
            self.lst_historique.append(detail)
        
        else:

            # Message d'erreur
            print("┗ Erreur ⋅ Un de vos personnages est déjà mort")
    
    def afficher_historique(self, lst_historique: list):
        """Affiche l'historique des combats

        Args:
            lst_historique (list): Liste des historiques des combats
        """

        # Itération de la liste d'historique des combats
        for num_combat, combat in enumerate(lst_historique):

            # Impression de l'historique
            print(f"┃ Combat #{num_combat}\n┃")
            print(f"┃ Nom Personnage 1 : {combat.nom_personnage_1.nom}")
            print(f"┃ Nom Personnage 2 : {combat.nom_personnage_2.nom}")
            print(f"┃ Nom Gagnant : {combat.vainqueur.nom}")
            print(f"┃ Nombre de tour : {combat.nombre_tours}")
            print("┃\n┃")

    def soigner_personnage(self, index_personnage: int, lst_personnage: list):
        """Remet la vie du personnage à l'index choisis à la valeur maximale

        Args:
            index_personnage (int): Index du personnage à soigner
            lst_personnage (list): Liste des personnage
        """
        
        # Récupération du personnage
        personnage = lst_personnage[index_personnage]

        # Reset de la vie
        personnage.vie = personnage.vie_max


    def nettoyer_arene(self, lst_personnage: list):
        """Retire tous les personnages morts

        Args:
            lst_personnage (list): Liste des personnages
        """

        # Itération de la liste des personnages
        for personnage in lst_personnage:
            
            # Si le personnage est mort
            if personnage.vie <= 0:
                
                # Retirer le personnage de la liste
                lst_personnage.remove(personnage)

    def battle_royal(self, lst_personnage: list):
        """Combat de type Battle-Royal

        Args:
            lst_personnage (list): Liste des personnages
        """

        # Boolean du combat
        combat = True

        # Nouvelle liste temporaire
        lst_personnage_tmp = list(lst_personnage)

        while combat:
            
            # Si il reste plus d'un personnage dans la liste
            if len(lst_personnage_tmp) != 1:
                
                # Index random du personnage qui attaquera (perso1) et qui subira les dégats (perso2)
                index_personnage_1 = randint(0, (len(lst_personnage_tmp)-1))
                index_personnage_2 = randint(0, (len(lst_personnage_tmp)-1))

                # Si les deux index sont pareils
                if index_personnage_1 == index_personnage_2:

                    # Sauter un tour de boucle
                    continue

                else:
                    
                    # Récupération des deux personnages dans la liste
                    personnage_1 = lst_personnage_tmp[index_personnage_1]
                    personnage_2 = lst_personnage_tmp[index_personnage_2]
                    
                    # Dégats d'attaque du perso1
                    degat_personnage_1 = personnage_1.attaquer()

                    # Attaque du perso1
                    personnage_2.subir_degat(degat_personnage_1)
                    print(f"┃ {personnage_1.nom} inflige {degat_personnage_1} à {personnage_2.nom}")

                    # Si le perso2 est mort
                    if personnage_2.vie <= 0:

                        # Message de mort
                        print(f"┃ {personnage_2.nom} est mort")
                        
                        # Retirer le personnage de la liste
                        lst_personnage_tmp.remove(personnage_2)

            else:
                
                # Message du gagnant
                print(f"┃ {lst_personnage_tmp[0].nom} est le gagnant !")

                # Arrêter la boucle
                combat = False
