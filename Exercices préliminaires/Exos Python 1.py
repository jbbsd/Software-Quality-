#!/usr/bin/env python3

def main ():
    #Récupération des données
    phrase = input("Veuillez entrer une phrase :")
    #Affichage de la phrase comme demandé
    chaine=phrase.split()
    print(chaine)
    #On détermine le type de la phrase 
    if phrase.endswith("."):
        print("C'est une phrase normal")
    elif phrase.endswith("?"):
        print("C'est une phrase interrogative")
    elif phrase.endswith("!"):
        print("C'est une phrase exclamative")
    else : 
        print("Il n'y a pas de point")




main()

