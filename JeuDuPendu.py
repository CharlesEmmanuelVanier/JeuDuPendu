import random
import unicodedata

#Fichier texte utilisé par défaut
Filename = "names.txt"

def strip_accent(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def GetRandom(File):
    File = open(Filename, "r", encoding="utf8")
    string = File.readlines()
    return strip_accent(random.choice(string))

def CheckWin(VerifWin):
    for i in range(len(VerifWin)):
        if(VerifWin[i] == 0):
            return 0
    return 1

def JeuDuPendu():
    NbreChances = 6
    NameChosen = GetRandom(Filename).strip()
    VerifName = []
    print(NameChosen)
    for i in range(len(NameChosen)):
        VerifName.append(0)

    while(NbreChances > 0):
        print("\nVoici l'état du mot à deviner:")
        for i in range(len(NameChosen)):
            if VerifName[i] == 1:
                print(NameChosen[i],end="")
            else:
                print(" _ ",end="")
        Guess = input("\n Veuillez entrer une lettre de l'alphabet\n")
        GoodGuess = len(NameChosen)
        for i in range(len(NameChosen)):
            if(NameChosen[i] == Guess):
                VerifName[i] = 1
            else:
                GoodGuess -= 1 #À la fin de la boucle il me reste le nombre de bon guess effectué
        if(GoodGuess > 0):
            print(f"Félicitation! Il y a {GoodGuess} '{Guess}' dans le mot.")
            if(CheckWin(VerifName)):
                print(f"VICTOIRE !\n Félication vous avez gagné!\nLe mot était {NameChosen}")
                break
        else:
            NbreChances -= 1
            print(f"Malheuresement il n'y a pas de {Guess} dans le mot\n Vous perdez une chance.")
            print(f"Il vous reste {NbreChances} chances")
            if NbreChances == 0:
                print("\n#####################\nVous n'avez plus de vie !\nPartie terminée\n#####################\n")

JeuDuPendu()
