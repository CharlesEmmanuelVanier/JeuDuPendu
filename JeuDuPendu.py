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
        #Affichage de l'état du mot à deviné
        print("\nVoici l'état du mot à deviner:")
        for i in range(len(NameChosen)):
            if VerifName[i] == 1:
                print(NameChosen[i],end="")
            else:
                print(" _ ",end="")

        #Interaction avec le joueur pour demander une lettre
        Guess = input("\n Veuillez entrer une lettre de l'alphabet\n")

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
                print(f"VICTOIRE !\n Félication vous avez gagné!\nLe mot était {NameChosen}")
                return 1
        else:
            NbreChances -= 1
            print(f"Malheuresement il n'y a pas de {Guess} dans le mot\n Vous perdez une chance.")
            print(f"Il vous reste {NbreChances} chances")
            #Partie terminé lorsque le joueur n'a plus de chance.
            if NbreChances == 0:
                print("\n#####################\nVous n'avez plus de chance !\nPartie terminée\n#####################\n")
                return 0

def restart():
    result = JeuDuPendu()
    choix = "o"
    while(choix == "o"):
        if result == 1:
            choix = input("Voulez vous continuer sur votre lancer ?\n Rejouer ? (o/n)")
        else:
            choix = input("Voulez vous votre revanche ?\n Rejouer ? (o/n")
        if choix == "o":
            result = JeuDuPendu()
        else:
            print("\n\n\nÀ bientot!")

restart()