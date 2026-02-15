from utils import tester_var
from classes.arene import Arene
from classes.armure import Armure
from classes.guerrier import Guerrier
from classes.mage import Mage
from classes.archer import Archer
from classes.soldat import Soldat
from classes.berserker import Berserker

def afficher_menu() -> int:
    """Affiche le menu principal

    Returns:
        int: Réponse de l'utilisateur
    """

    # Impression du menu
    print(f"┏━━━━━━━━━━━━━━━━━━┓")
    print(f"┃  Menu Principal  ┃")
    print(f"┗━━━━━━━━━━━━━━━━━━┛")
    print("┃ [1] Ajouter un personnage")
    print("┃ [2] Voir les personnages dans l'arène")
    print("┃ [3] Faire combattre deux personnages")
    print("┃ [4] Afficher l'historique des combats")
    print("┃ [5] Soigner un personnage")
    print("┃ [6] Nettoyer l'arène")
    print("┃ [7] Voir le nombre de combatants dans l'arène")
    print("┃ [8] Lancer un BattleRoyal")
    print("┃ [9] Quitter")
    reponse_usr = tester_var(input("┗ ⋅ Quel est votre choix ? "), int)

    return reponse_usr

# Boolean de la boucle principale
programme = True

# Liste vide pour les personnages et l'historique
lst_personnage = []
lst_historique = []

# Création de l'arène
arene = Arene(lst_personnage, lst_historique)


while programme:

    # Affichage du menu
    choix = afficher_menu()

    match choix:
        
        # Ajouter un personnage
        case 1:
            
            # Questions sur la créations des personnages
            print(f"┏━━━━━━━━━━━━━━━┓")
            print(f"┃  Personnages  ┃")
            print(f"┗━━━━━━━━━━━━━━━┛")
            type = tester_var(input("┗ ⋅ Quel est le type de votre personnage \n┃ [1] : Guerrier, \n┃ [2] : Mage, \n┃ [3] : Archer, \n┃ [4] : Soldat, \n┃ [5] : Berserker ? "), int) 
            nom = tester_var(input("┗ ⋅ Quel est le nom de votre personnage ? "), str)
            vie = tester_var(input("┗ ⋅ Quel est le niveau de vie de votre personnage. Entre 0 et 500 ? "), int)
            attaque = tester_var(input("┗ ⋅ Quel est le niveau d'attaque de votre personnage. Entre 0 et 50 ? "), int)

            match type:
                
                # Geurrier
                case 1:

                    force = tester_var(input("┗ ⋅ Quel est le niveau de force de votre personnage. Entre 0 et 50 ? "), int)

                    # Ajout du personnage à l'arène
                    arene.ajouter_personnage(Guerrier(nom, vie, attaque, Armure("Armure de plaque", 12), force))

                # Mage
                case 2:

                    mana = tester_var(input("┗ ⋅ Quel est le niveau de mana de votre personnage. Entre 0 et 100 ? "), int)
                    
                    # Ajout du personnage à l'arène
                    arene.ajouter_personnage(Mage(nom, vie, attaque, Armure("Armure magique", 7), mana))

                # Archer
                case 3:

                    dexterite = tester_var(input("┗ ⋅ Quel est le niveau de dexterite de votre personnage. Entre 40 et 70 ? "), int)

                    # Ajout du personnage à l'arène
                    arene.ajouter_personnage(Archer(nom, vie, attaque, Armure("Tunique de cuire", 5), dexterite))

                # Soldat
                case 4:
                    
                    # Ajout du personnage à l'arène
                    arene.ajouter_personnage(Soldat(nom, vie, attaque, Armure("Cotte de maille", 15)))

                # Berserker
                case 5:
                    
                    force = tester_var(input("┗ ⋅ Quel est le niveau de force de votre personnage. Entre 0 et 50 ? "), int)
                    
                    # Ajout du personnage à l'arène
                    arene.ajouter_personnage(Berserker(nom, vie, attaque, Armure("Armure de plaque", 12), force))

        # Voir les personnages dans l'arène
        case 2:
            
            # Affichage des personnages
            arene.afficher_personnages()

        # Faire combattre deux personnages
        case 3:
            
            # Vérifie s'il y a au moins deux personnages dans l'arène
            if len(arene.lst_personnage) >= 2:
                
                # Récupération des index des personnages dans la liste des personnages
                index_pers_1 = tester_var(input(f"┗ ⋅ Quel est l'index du personnage 1. Entre 0 et {len(arene.lst_personnage)-1} ? "), int)
                index_pers_2 = tester_var(input(f"┗ ⋅ Quel est l'index du personnage 2. Entre 0 et {len(arene.lst_personnage)-1} ? "), int)
                
                # Combat des personnages
                arene.combattre(index_pers_1, index_pers_2)
            
            else:
                
                # Message d'erreur
                print("┗ Erreur ⋅ Vous devez minimalement ajouter deux personnages à votre arène pour les faires se combattre !")

        # Afficher l'historique des combats
        case 4:
            
            # Afficher l'historique des combats
            arene.afficher_historique(lst_historique)
        
        # Soigner un personnage
        case 5:
            
            # Récupération de l'index du personnage
            index_pers= tester_var(input(f"┗ ⋅ Quel est l'index du personnage que vous voulez soigner. Entre 0 et {len(arene.lst_personnage)-1} ? "), int)

            # Soigner le personnage dans l'arène
            arene.soigner_personnage(index_pers, lst_personnage)
        
        # Nettoyer l'arène
        case 6:

            # Retirer les personnages morts de l'arène
            arene.nettoyer_arene(lst_personnage)
        
        # Voir le nombre de combattants dans l'arène
        case 7:

            # Afficher le nombre de combattants vivants dans l'arène
            print(arene.__len__())
        
        # Lancer un BattleRoyal
        case 8:
            
            # Combat battle-royal
            arene.battle_royal(lst_personnage)
        
        # Quitter
        case 9:
            
            # Arrêt de la boucle
            programme = False

            
        # *** Option de TEST ***
        case 15:

            # Ajout de personnages de chaque types dans l'arène 
            lst_personnage.append(Guerrier("Guerrier", 500, 50, Armure("Armure de plaque", 12), 50))
            lst_personnage.append(Mage("Mage", 500, 50, Armure("Armure magique", 7), 50))
            lst_personnage.append(Archer("Archer", 500, 50, Armure("Tunique de cuire", 5), 50))
            lst_personnage.append(Soldat("Soldat", 500, 50, Armure("Cotte de maille", 15)))
            lst_personnage.append(Berserker("Berserker", 500, 50, Armure("Armure de plaque", 12), 50))