import random
import unicodedata
import os.path

def strip_accent(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def get_random(Filename):
    file = open(Filename, "r", encoding="utf8")
    string = file.readlines()
    return strip_accent(random.choice(string))

def get_indice(GameName,GuessHistory):
    alphabetString = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    alphabetList = alphabetString.split(",")
    goodIndice = 0
    while goodIndice == 0:
        indice = random.choice(alphabetList)
        goodIndice = 1
        for i in range(len(GameName)):
            if indice == GameName[i]:
                goodIndice = 0
        for i in range(len(GuessHistory)):
            if indice == GuessHistory[i]:
                goodIndice = 0

    return indice


def check_win(verifWin):
    for i in range(len(verifWin)):
        if(verifWin[i] == 0):
            return 0
    return 1

def jeu_du_pendu(filename):
    nbreChances = 6
    nameChosen = get_random(filename).strip()
    verifName = []
    guessHistory = []
    print(nameChosen)
    for i in range(len(nameChosen)):
        verifName.append(0)

    while(nbreChances > 0):
        #Affichage de l'état du mot à deviné
        print("\nVoici l'état du mot à deviner:")
        for i in range(len(nameChosen)):
            if verifName[i] == 1:
                print(nameChosen[i],end="")
            else:
                print(" _ ",end="")

        #Interaction avec le joueur pour demander une lettre
        guess = input("\n Veuillez entrer une lettre de l'alphabet\n")
        guessHistory.append(guess)

        #Vérification si la lettre est dans le mot
        goodGuess = len(nameChosen)
        for i in range(len(nameChosen)):
            if(nameChosen[i] == guess):
                verifName[i] = 1
            else:
                goodGuess -= 1 #À la fin de la boucle il me reste le nombre de bon guess effectué
        #Affichage du résultat du guess, si la lettre était dans le mot ou pas.
        if(goodGuess > 0):
            print(f"Félicitation! Il y a {goodGuess} '{guess}' dans le mot.")
            #Petite fonction qui détermine si le joueur a deviner le mot en entier ou s'il reste des lettres à deviner
            if(check_win(verifName)):
                print(f"VICTOIRE !\nFélicitation vous avez gagné!\nLe mot était '{nameChosen}'")
                return 1
        else:
            nbreChances -= 1
            print(f"Malheuresement il n'y a pas de '{guess}' dans le mot\n Vous perdez une chance.")
            print(f"Il vous reste {nbreChances} chances")
            if (nbreChances == 1):
                if (input("\nIl ne vous reste plus qu'une seule vie !\n Voulez-vous un indice ? (o/n) ") == "o"):
                    print(f"\n\nCette lettre ne fait pas partie du mot: {get_indice(nameChosen, guessHistory)}")
                #Partie terminé lorsque le joueur n'a plus de chance.
                elif nbreChances == 0:
                    print("\n#####################\nVous n'avez plus de chance !\nPartie terminée\n#####################\n")
                    print(f"Le mot était {nameChosen}")
                    return 0

def changement_filename():
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
        filename = changement_filename()
        if(not os.path.exists(filename)):
            print("Fichier introuvable, Arrêt du programme")
            quit()
    else:
        filename = "names.txt"

    #Lancement de la première partie
    result = jeu_du_pendu(filename)
    #Demande au joueur s'il veut rejouer, jusqu'à ce qu'il dise non.
    choix = "o"
    while(choix == "o"):
        if result == 1:
            choix = input("Voulez vous continuer sur votre lancer ?\n Rejouer ? (o/n) ")
        else:
            choix = input("Voulez vous votre revanche ?\n Rejouer ? (o/n) ")
        if choix == "o":
            result = jeu_du_pendu(filename)
        else:
            return "\n\n\nÀ bientot !\n\n"

#Appelle la fonction principale du programme
print(menu())