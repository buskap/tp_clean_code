#!/usr/bin/python3
import string 

def keyVerification(id):
    """Verifie la validité de l'identifiant

    Args:
        id (str): l'id doit être de longueur 10 et contenir la clé en majuscule (A-Z) suivi des 9 chiffres de l'identifiant (ex: A123456789)

    Returns:
        Bool: True est retourné si l'identifiant correspond à la clé, false sinon
    """    
    print("keyVerification")
    if ( len (id) == 10):
        key = id[0]
        #Test de validité de la clé + calcul de l'id sans clé 
        if(key.isupper()):
            res = calculKey(id[1:])
            while( res > 15 ):
                res = calculKey(str(res))
            
            #Correspondance alphabetique
            values = dict()
            for index, letter in enumerate(string.ascii_uppercase):
                values[letter] = index + 1
            
            #Vérification de la validité de la clé
            if( (values[key] == res+1) or ( res==0 and key == "Z") ):
                return True
            
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