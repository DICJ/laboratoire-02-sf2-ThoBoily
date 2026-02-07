from utils import tester_var
from classes.arene import Arene
from classes.guerrier import Guerrier
from classes.mage import Mage
from classes.archer import Archer

def afficher_menu() -> int:
    print(f"┏━━━━━━━━━━━━━━━━━━┓")
    print(f"┃  Menu Principal  ┃")
    print(f"┗━━━━━━━━━━━━━━━━━━┛")
    print("┃ [1] Ajouter un personnage")
    print("┃ [2] Voir les personnages dans l'arène")
    print("┃ [3] Faire combattre deux personnages")
    print("┃ [4] Quitter")
    reponse_usr = tester_var(input("┗ ⋅ Quel est votre choix ? "), int)

    return reponse_usr

programme = True

lst_personnage = []
arene = Arene(lst_personnage)

while programme:

    choix = afficher_menu()

    match choix:

        case 1:
            
            print(f"┏━━━━━━━━━━━━━━━┓")
            print(f"┃  Personnages  ┃")
            print(f"┗━━━━━━━━━━━━━━━┛")
            type = tester_var(input("┗ ⋅ Quel est le type de votre personnage [1] : Guerrier, [2] : Mage, [3] : Archer ? "), int) 
            nom = tester_var(input("┗ ⋅ Quel est le nom de votre personnage ? "), str)
            vie = tester_var(input("┗ ⋅ Quel est le niveau de vie de votre personnage. Entre 0 et 500 ? "), int)
            attaque = tester_var(input("┗ ⋅ Quel est le niveau d'attaque de votre personnage. Entre 0 et 50 ? "), int)

            match type:

                case 1:

                    force = tester_var(input("┗ ⋅ Quel est le niveau de force de votre personnage. Entre 0 et 50 ? "), int)

                    arene.ajouter_personnage(Guerrier(nom, vie, attaque, force))

                case 2:

                    mana = tester_var(input("┗ ⋅ Quel est le niveau de mana de votre personnage. Entre 0 et 100 ? "), int)

                    arene.ajouter_personnage(Mage(nom, vie, attaque, mana))

                case 3:

                    dexterite = tester_var(input("┗ ⋅ Quel est le niveau de dexterite de votre personnage. Entre 40 et 70 ? "), int)

                    arene.ajouter_personnage(Archer(nom, vie, attaque, dexterite))

        case 2:
            
            arene.afficher_personnages()

        case 3:

            index_pers_1 = tester_var(input(f"┗ ⋅ Quel est l'index du personnage 1. Entre 0 et {len(arene._lst_personnage)} ? "), int)
            index_pers_2 = tester_var(input(f"┗ ⋅ Quel est l'index du personnage 2. Entre 0 et {len(arene._lst_personnage)} ? "), int)
            
            arene.combattre(index_pers_1, index_pers_2)

        case 4:
            
            programme = False