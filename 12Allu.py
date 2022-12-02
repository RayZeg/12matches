
# -*- coding: utf-8 -*-
from random import*
 
def menu(rejouer):
    fin=False
    while fin==False: # S'écrit 'while not fin:'
         print("\n\n******** Menu ********")            #  \n = sauter une ligne
         print("Bienvenue dans le jeu des allumettes!")
         print("Le but du jeu est simple : Choisissez un nombre d'allumette puis decidez du nombre (entre 1 et 3) a enlever.\n A son tour, l'ordinateur en fera de meme et ainsi de suite jusqu'a ce qu'il n'y ait plus d'allumettes.\n Le perdant est celui qui retirera la derniere allumette.")
         print("(1) Jouer ")
         print("(2) Quitter le programme ")
 
         if rejouer==2:
            fin=True
 
         return rejouer # !! 'rejouer' est donné en argument à la fonction,
                        # quelle était ton intention ?
 
def PartieJoueur(nbrAllumettes,nbrAlluAretirer,reponse): # A quoi sert l'argument 'reponse' ?
    print("/"*nbrAllumettes,end='')  # Tâche ménagère, ne devrait pas être ici.
    print(" Vous jouez avec",alluaffiche,"allumettes") # Pareil
    # C'est ici qu'il faudrait saisir le nombre d'allumettes choisi par le joueur
    while 1:
        if (nbrAlluAretirer<1):
            print("Entrer un nombre SUPERIEUR ou egal a 1 ")
            # Ici, on dit au joueur de rectifier son choix ...
            reponse = False
        elif (nbrAlluAretirer>3):
            print("Entrer un nombre INFERIEUR ou egal 3")
            # .. ici encore ...
            reponse = False
        # ... sans lui donner la possibilité de le faire.
        if reponse == True: #
            break
 
            # !! Les lignes qui suivent ne s'exécuteront jamais',
            # est-ce le but ? !!
            print("/"*alluaffiche,end='')  # Tâche ménagère, ne devrait pas être ici.
            if(alluaffiche<=1):
                print(" Vous avez gagne :D")
 
def tourOrdi(nbrAlluAretirer,alluaffiche):
    if (nbrAlluAretirer > 8):
        print(" L'ordinateur a retirer",nbrAlluAretirer,"Allumettes")
    # Voir à créer un algo qui simplifie ces 14 lignes
    elif (nbrAlluAretirer == 8):
        nbrAlluAretirer = 3
    elif (nbrAlluAretirer == 7):
        nbrAlluAretirer = 2
    elif (nbrAlluAretirer == 6):
        nbrAlluAretirer = 1
    elif (nbrAlluAretirer == 5):
        nbrAlluAretirer = 1
    elif (nbrAlluAretirer == 4):
        nbrAlluAretirer = 3
    elif (nbrAlluAretirer == 3):
        nbrAlluAretirer = 2
    elif (nbrAlluAretirer == 2):
        nbrAlluAretirer = 1
 
        # !! Les lignes qui suivent s'exécuteront si 'nbrAlluAretirer == 2' !!
        alluaffiche=alluaffiche-nbrAlluAretirer
 
        print("/"*alluaffiche,end='')  # Tâche ménagère, ...
        print(" Il reste",alluaffiche,"allumettes")
        if(alluaffiche<=1):
             print(" Vous avez perdu :(")
 
    return alluaffiche # 1 chance sur 8 d'avoir été modifiée
 
 
#Programme principal #
rejouer=1
menu(rejouer)
rejouer=input("Quel est votre choix? : ") # Devrait être retourné par la fonction menu()
 
nbrAllumettes=int(input("Rentrer un nombre entier d'allumettes : ")) # >> fonction menu()
alluaffiche=nbrAllumettes
 
# Mettre ceci dans une fonction
nbrAlluAretirer=int(input("Combien d'allumettes (entre 1 et 3) voulez-vous retirer? : "))
reponse = True
PartieJoueur(nbrAllumettes,nbrAlluAretirer,reponse)
nbrAlluAretirer = (int(random()*3+1))
alluaffiche=alluaffiche-nbrAlluAretirer
 
tourOrdi(nbrAlluAretirer,alluaffiche)
rejouer = True
while rejouer:
    nbrAllumettes=int(input("Rentrer un nombre entier d'allumettes : "))
    alluaffiche=nbrAllumettes
    while alluaffiche>1: 
        # !!! Boucle infinie s'il reste plus d'une allumette !!!
        print("/"*nbrAllumettes,end='')
        print(" Vous jouez avec",alluaffiche,"allumettes")
 
    rejouer = menu() # !! menu() demande un argument
 
# Fin du programme #
print("*** Fin ***")