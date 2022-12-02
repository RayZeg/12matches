from math import *
from random import *

allumettes=[i for i in range(12)]
print("| "*len(allumettes))
while len(allumettes)>1:
    sub=int(input("Choisir un nb entre 1 et 3:"))
    for i in range(sub):
        allumettes.remove(allumettes[-1])
        print("| "*len(allumettes))
        if len(allumettes)==1:
            print("Vous avez ́gagne")
        else:
            ia=randint(1,3 if len(allumettes)>3 else len(allumettes)-1)
            print("L'IA ̀enleve",ia)
        for i in range(ia):
            allumettes.remove(allumettes[-1])
            print("| "*len(allumettes))
            if len(allumettes)==1:
                print("Vous avez perdu !")


                #CHIKHI_Med_Wassim Jeux_12_Allumetes
