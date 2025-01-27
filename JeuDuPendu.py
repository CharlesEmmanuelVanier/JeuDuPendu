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




JeuDuPendu()
