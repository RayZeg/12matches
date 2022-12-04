from math import *
from random import *

def matchgame():
    alumette = [i for i in range(12)]
    while len(alumette) > 0:
        print("I "*len(alumette))
        sub = int(input("choisir un nb entre 1 et 3:"))
        for i in range(sub):
            alumette.remove(alumette[-1])
        if len(alumette) == 0:
            print("vous aver gagner")            
            return
        print("pc a choisie ",4-sub)
        for i in range(4-sub):
            alumette.remove(alumette[-1])
        if len(alumette) == 0:
            print("pc a gagner")
            return
matchgame()