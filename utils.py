from typing import Any
import os

def tester_var(
    var: Any, 
    cible: type,
    val_defaut: Any | None = None
) -> Any:
    """
    Permet de s'assurer que le type d'une variable est la bonne
    
    Parameters :
        var (Any) : La valeur à tester.
        cible (type) : Type de la valeur à tester.
        val_defaut (Any) : Valeur par défaut si il y une erreur.

    Returns:
        (Any) : La valeur tester ou la valeur par défaut.
    """

    # Essaie de transformer la variable
    try:
        var = cible(var)
        return var

    # S'il n'y arrive pas
    except:
        return val_defaut     

def styliser_texte(
    texte: str, 
    r: int | None = None, 
    g: int | None = None, 
    b: int | None = None, 
    modificateur: str | None = None
) -> str:
    """
    Permet de rajouter de la couleur et des éléments de style dans le texte
    
    Parameters :
        texte (str) : Textes à styliser.
        r (int) : Taux d'intencité de rouge dans la couleur.
        g (int) : Taux d'intencité de vert dans la couleur.
        b (int) : Taux d'intencité de bleu dans la couleur.
        mondificateur (str) : Lettre (B) pour gras, (I) pour italique, (F) pour foncé, (U) pour sousligné.
    
    Returns:
        (str) : Le texte styliser.
    """

    # Si la couleur existe
    if r and b and g:
        code = f"\033[38;2;{r};{g};{b}m"

    else:
        code = "\033["
    
    # Liste des éléments de modification du texte
    element_modif_lst = []

    # Si le modificateur existe
    if modificateur:

        # Met le texte en gras
        if "b" in modificateur:
            element_modif_lst.append("1;")

        # Met le texte plus foncé
        if "f" in modificateur:
            element_modif_lst.append("2;")

        # Met le texte en italique
        if "i" in modificateur:
            element_modif_lst.append("3;")

        # Souligne le texte
        if "u" in modificateur:
            element_modif_lst.append("4;")

    # Diviser le string du code en deux au niveau de "["
    code_lst = code.split("[")

    # Si la couleur n'existe pas
    if not r and not g and not b:

        # Remplacer le "point virgule" par un "m" car le "m" est l'élément fermant
        element_modif_lst[-1] = element_modif_lst[-1].replace(";", "m")

    # Faire une chaine de caractère avec la liste
    modif_txt = "".join(element_modif_lst)

    # Liste final du code de style
    code = f"{code_lst[0]}[{modif_txt}{code_lst[1]}"

    # Texte final
    return f"{code}{texte}\033[0m"
