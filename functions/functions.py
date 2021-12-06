#!/usr/bin/python3
import string 

def keyVerification(id):
    """Verifie la validité de l'identifiant

    Args:
        id (str): l'id doit être de longueur 10 et contenir la clé en majuscule (A-Z) suivi des 9 chiffres de l'identifiant (ex: A123456789)

    Returns:
        Bool: True est retourné si l'identifiant correspond à la clé, false sinon
    """    
    if(estValide(id)):
        res = calculKey(id[1:])
        while( res > 15 ):
            res = calculKey(str(res))
        key = id[0]
        #Correspondance alphabetique
        values = dict()
        for index, letter in enumerate(string.ascii_uppercase):
            values[letter] = index + 1
        
        #Vérification de la validité de la clé
        if( (values[key] == res+1) or ( res==0 and key == "Z") ):
            return True
        
    else: 
        return False

def calculKey( id ):
    """Calcul la somme de des chiffres de l'id
    Args:
        id (str): 
    Returns:
        int: retourne le resultat de la somme sous forme de int
    """    
    if(len(id) > 1 ):
        return int(id[0]) + calculKey( id[1:])
    else: 
        return int(id)

def estValide(id):
    """Verifie la validité du format de l'identifiant
    Args:
        id (str): String de longueur 10 contenant une clé : caractère alpha en majuscule en première position (A-Z) suivie d'une suite de 9 chiffres (identifiant)
    Returns:
        bool: True est retourné si l'id est valide, False sinon
    """    
    if ( len (id) == 10):
        key = id[0]
        #Test de validité de la clé 
        if(key.isupper()):
            #test que l'id est une suite de neuf chiffres
            identifiant = id[1:]
            for element in identifiant:
                try:
                    int(element)
                    break
                except:
                    return False
            return True
        else:
            return False
    else:
        return False
    