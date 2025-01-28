import random
import unicodedata
import string
import os.path

def strip_accent(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def GetRandom(Filename):
    File = open(Filename, "r", encoding="utf8")
    string = File.readlines()
    return strip_accent(random.choice(string))

def GetIndice(GameName,GuessHistory):
    Alphabet_String = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    Alphabet_List = Alphabet_String.split(",")
    GoodIndice = 0
    while GoodIndice == 0:
        Indice = random.choice(Alphabet_List)
        GoodIndice = 1
        for i in range(len(GameName)):
            if Indice == GameName[i]:
                GoodIndice = 0
        for i in range(len(GuessHistory)):
            if Indice == GuessHistory[i]:
                GoodIndice = 0

    return Indice


def CheckWin(VerifWin):
    for i in range(len(VerifWin)):
        if(VerifWin[i] == 0):
            return 0
    return 1

def JeuDuPendu(Filename):
    NbreChances = 6
    NameChosen = GetRandom(Filename).strip()
    VerifName = []
    GuessHistory = []
    print(NameChosen)
    for i in range(len(NameChosen)):
        VerifName.append(0)

    while(NbreChances > 0):
        #Affichage de l'état du mot à deviné
        print("\nVoici l'état du mot à deviner:")
        for i in range(len(NameChosen)):
            if VerifName[i] == 1:
                print(NameChosen[i],end="")
            else:
                print(" _ ",end="")

        #Interaction avec le joueur pour demander une lettre
        Guess = input("\n Veuillez entrer une lettre de l'alphabet\n")
        GuessHistory.append(Guess)

        #Vérification si la lettre est dans le mot
        GoodGuess = len(NameChosen)
        for i in range(len(NameChosen)):
            if(NameChosen[i] == Guess):
                VerifName[i] = 1
            else:
                GoodGuess -= 1 #À la fin de la boucle il me reste le nombre de bon guess effectué
        #Affichage du résultat du guess, si la lettre était dans le mot ou pas.
        if(GoodGuess > 0):
            print(f"Félicitation! Il y a {GoodGuess} '{Guess}' dans le mot.")
            #Petite fonction qui détermine si le joueur a deviner le mot en entier ou s'il reste des lettres à deviner
            if(CheckWin(VerifName)):
                print(f"VICTOIRE !\nFélicitation vous avez gagné!\nLe mot était '{NameChosen}'")
                return 1
        else:
            NbreChances -= 1
            print(f"Malheuresement il n'y a pas de '{Guess}' dans le mot\n Vous perdez une chance.")
            print(f"Il vous reste {NbreChances} chances")
            if (NbreChances == 1):
                if (input("\nIl ne vous reste plus qu'une seule vie !\n Voulez-vous un indice ? (o/n) ") == "o"):
                    print(f"\n\nCette lettre ne fait pas partie du mot: {GetIndice(NameChosen, GuessHistory)}")
                #Partie terminé lorsque le joueur n'a plus de chance.
                elif NbreChances == 0:
                    print("\n#####################\nVous n'avez plus de chance !\nPartie terminée\n#####################\n")
                    print(f"Le mot était {NameChosen}")
                    return 0

def ChangementFile():
    print("À noter que le format du fichier devra être le suivant:\n"
          "mot1\n"
          "mot2\n"
          "mot3\n"
          "Ainsi de suite\n")
    return input("\n\n Veuillez entrer le nom du fichier a utiliser (Exemple : 'names.txt')\n")

def menu():
    customFile = input("Bienvenue dans le jeu du pendu ! \n"
          "Voulez-vous utiliser une liste de mot personnalisé? (o/n) ")

    if(customFile == "o"):
        Filename = ChangementFile()
    else:
        Filename = "names.txt"

    #Lancement de la première partie
    result = JeuDuPendu(Filename)
    #Demande au joueur s'il veut rejouer, jusqu'à ce qu'il ne veule plus.
    choix = "o"
    while(choix == "o"):
        if result == 1:
            choix = input("Voulez vous continuer sur votre lancer ?\n Rejouer ? (o/n) ")
        else:
            choix = input("Voulez vous votre revanche ?\n Rejouer ? (o/n) ")
        if choix == "o":
            result = JeuDuPendu()
        else:
            print("\n\n\nÀ bientot!")

menu()