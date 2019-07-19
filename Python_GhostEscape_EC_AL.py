#Projet python
#Python3
#Elsa CLAUDE Alexandre LAMBARD

import random

### FUNCTIONS ###
def create_matrice(chateau,tailleligne,taillecolonne): #créer base du chateau en iste de liste (matrice), ajoute les limites horizontales et verticales et les couloirs
    for ligne in range(tailleligne): #Ajoute le nombre de listes correspondant au nombre de lignes dans la matrice
        chateau.append([])
        for colonne in range(taillecolonne):
            if ligne==0 or ligne==10: #détermine les limites (notées X) horizontales du jeu càd liste 0 et 10
                chateau[ligne].append("X")
            elif (ligne in(2,4,6) and colonne in(3,5,7)) or (ligne in(4,6) and colonne in(1,9)) or (ligne==8 and colonne in(3,5)): #séries de "if" pour ajouter les couloirs
                chateau[ligne].append(u'\u2551') #codage permettant d'afficher du ASCII "étendu"
            elif (ligne in(3,5,7) and colonne in(2,8)) or (ligne in(1,9,4) and colonne==4):
                chateau[ligne].append(u'\u2550')
            elif (ligne in (3,5,7) and colonne in(3,5)) or (ligne in(3,5) and colonne==7):
                chateau[ligne].append(u'\u256c')
            elif ligne==1 and colonne==3:
                chateau[ligne].append(u'\u2554')
            elif ligne==9 and colonne==3:
                chateau[ligne].append(u'\u255a')
            elif ligne==1 and colonne==5:
                chateau[ligne].append(u'\u2557')
            elif ligne==9 and colonne==5:
                chateau[ligne].append(u'\u255d')
            elif ligne==7 and colonne==7:
                chateau[ligne].append(u'\u2569')
            else :
                chateau[ligne].append(0)
    for ligne in range(len(chateau)): #détermine les limites verticales du jeu c'est à dire la colonne 0 et 10
        chateau[ligne][0]="X"
        chateau[ligne][10]="X"

def creer_pieces(chateau):
    for ligne in range(len(chateau)): #parcourt la matrice en liste de liste (les lignes) puis en indice de ces listes (les colonnes)
        for colonne in range(len(chateau[ligne])):
            if ligne in (3,5,7) and colonne in (1,4,6,9):
                chateau[ligne][colonne]="O"

def position_salles(chateau): #créé une liste avec les coordonnées des salles O
    salles=[]
    for ligne in range(len(chateau)): #parcourt la matrice pour trouver les coordonnées des salles (notées "O") et stock les coordonnées dans des listes positionsalle elles-mêmes dans la liste salles
        for colonne in range (len(chateau[ligne])):
            if chateau[ligne][colonne]=="O":
                lignesalle=ligne
                colonnesalle=colonne
                positionsalle=[lignesalle,colonnesalle]
                salles.append(positionsalle)               
    return salles

def case(chateau): #trouver une case random (salle, couloir ou réception) sauf limite, paradis et le savant, fonction destinée à chateau'action du savant fou
    exceptX="X"
    while True:
        if exceptX=="X" or exceptX=="S" or exceptX=="M" or exceptX=="B" or exceptX==1 or exceptX==2 or exceptX==3:
            quelleligne=random.randrange(len(chateau)) #cherche un indice de ligne au hasard
            quellecolonne=random.randrange(len(chateau[quelleligne])) #cherche un indice de colonne au hasard
            exceptX=chateau[quelleligne][quellecolonne] #change valeur du exceptX si c'est tombé sur une limite, un monstre ou de chateau'énergie
        else:
            return quelleligne,quellecolonne #si c'est tombé sur une case autre que limite/monstre/energie alors on return valeur de la ligne et de la colonne aléatoires

def limites_internes(chateau): #parcourt la matrice et met en place des if pour ajouter les limites notées "X"
    for ligne in range(len(chateau)): 
        for colonne in range(len(chateau[ligne])):
            if (ligne in (1,2,4,6) and colonne in (2,6,8)) or (ligne in (1,2) and colonne in (1,9)) or (ligne in (2,4,6) and colonne==4):
                chateau[ligne][colonne]="X"
            if (ligne in(8,9) and colonne in(1,2,6,7,8,9)) or (ligne==8 and colonne==4):
                chateau[ligne][colonne]="X"

def position_mechants(chateau): #Définir de façon aléatoire les positions des différents méchants
    listemechants=["M","S","B","B","B"] #5 méchants, la liste contient 5 indices de 0 à 4
    salles=position_salles(chateau)
    for indice in range(5):
        quelmechant=random.randrange(len(listemechants)) #on récupère un chiffre aléatoire entre 0 et 4 à utiliser comme indice pour choisir dans la liste des méchants
        quellesalle=random.randrange(len(salles)) #prend chateau'indice méchant et parcours la liste des salles pour savoir dans quelle salle le placer
        chateau[salles[quellesalle][0]][salles[quellesalle][1]]=listemechants[quelmechant] #Ajoute dans dans une salle choisie aléatoirement le méchant choisi aléatoirement, jusqu'à ce que la liste de méchants soit vide
        del(listemechants[quelmechant])
        del(salles[quellesalle])

def position_energie(chateau): #Ajoute les 5 pintes d'énergie dans le chateau avec 1 à 3 pintes possible par salles
    listeenergie=[1,2,3]
    salles=position_salles(chateau)
    reste=5 #nombre d'energie à placer encore
    while True:
        if reste>=3:
            combienenergie=random.randrange(len(listeenergie))
            quellesalle=random.randrange(len(salles))
            chateau[salles[quellesalle][0]][salles[quellesalle][1]]=listeenergie[combienenergie]
            del(salles[quellesalle])
            reste=reste-listeenergie[combienenergie] #met à jour le nombre d'énergie qu'il reste à placer
        elif reste==2: #s'il reste 2 énergies alors rentre dans ce if pour chateau'empêcher d'ajouter 3 pintes dans une salle
            combienenergie=random.randrange(len(listeenergie)-1) #empêche la boucle d'utiliser chateau'indice "2" de listeenergie (c'est à dire, le fait d'ajouter 3 pintes d'énergie)
            quellesalle=random.randrange(len(salles))
            chateau[salles[quellesalle][0]][salles[quellesalle][1]]=listeenergie[combienenergie]
            del(salles[quellesalle])
            reste=reste-listeenergie[combienenergie]
        elif reste==1:
            combienenergie=random.randrange(len(listeenergie)-2)
            quellesalle=random.randrange(len(salles))
            chateau[salles[quellesalle][0]][salles[quellesalle][1]]=listeenergie[combienenergie]
            del(salles[quellesalle])
            reste=reste-listeenergie[combienenergie]
        elif reste==0:
            break
        
def creation_chateau(chateau,nblignes,nbcolonnes,lignepos,colpos,tmp): #concentre les différentes fonctions pour créer le chateau (couloirs, salles, paradis, méchants, énergies etc.)
    create_matrice(chateau,nblignes,nbcolonnes)
    limites_internes(chateau)
    creer_pieces(chateau)
    chateau[1][7]="P"
    position_salles(chateau)
    tmp=chateau[lignepos][colpos] #tmp est une variable qui permet de stocker temporairement la valeur de la position où le joueur compte se placer (à chateau'initialisation, tmp stock le couloir de la réception)
    chateau[9][4]="*"
    position_mechants(chateau)
    position_energie(chateau)
    affichage_joueur(chateau)
    return chateau,nblignes,nbcolonnes,lignepos,colpos,tmp

def limites(chateau,lignepos,colpos): #test si le joueur tente de rentrer dans une limite
    if chateau[lignepos][colpos]!="X":
        return True
    else:
        print("Il y a un mur magique, vous ne pouvez pas le traverser !")
        return False

def test_salle(chateau,tmp,lignepos,colpos,energie):
    if tmp=="M": #maître du château
        chateau,tmp,lignepos,colpos=maitre(chateau,tmp,lignepos,colpos)
    elif tmp=="S": #savant fou
        chateau,tmp,lignepos,colpos,energie=savant(energie,chateau,tmp,lignepos,colpos)
    elif tmp=="B": #Bibbendum
        energie=bibben(energie)
    elif tmp in (1,2,3): #salle avec énergie
        chateau,tmp,energie=salles_energie(chateau,tmp,energie)
    return chateau,tmp,lignepos,colpos,energie
    

def deplacement_haut(chateau,tmp,lignepos,colpos,energie): #fonction de déplacement vers le haut avec prise en compte de rencontre avec une limite, un méchant, de chateau'énergie ou un simple couloir
    if limites(chateau,lignepos-1,colpos)==True: #On applique les déplacements seulement si le joueur n'essaie pas de rentrer dans une limite
        chateau[lignepos][colpos]=tmp #on réapplique à la position du joueur, la valeur tmp stockée
        tmp=chateau[lignepos-1][colpos] #on stock la valeur de la prochaine position avant que le joueur ne se déplace
        chateau[lignepos-1][colpos]="*" #place le joueur
        lignepos-=1 #modifie une coordonnée du joueur
        chateau,tmp,lignepos,colpos,energie=test_salle(chateau,tmp,lignepos,colpos,energie) #applique conséquences d'une rencontre avec monstre ou énergie
    return chateau,tmp,lignepos,colpos,energie

def deplacement_bas(chateau,tmp,lignepos,colpos,energie):
    if limites(chateau,lignepos+1,colpos)==True:
        chateau[lignepos][colpos]=tmp
        tmp=chateau[lignepos+1][colpos]
        chateau[lignepos+1][colpos]="*"
        lignepos+=1
        chateau,tmp,lignepos,colpos,energie=test_salle(chateau,tmp,lignepos,colpos,energie)
    return chateau,tmp,lignepos,colpos,energie

def deplacement_gauche(chateau,tmp,lignepos,colpos,energie):
    if limites(chateau,lignepos,colpos-1)==True:
        chateau[lignepos][colpos]=tmp
        tmp=chateau[lignepos][colpos-1]
        chateau[lignepos][colpos-1]="*"
        colpos-=1
        chateau,tmp,lignepos,colpos,energie=test_salle(chateau,tmp,lignepos,colpos,energie)
    return chateau,tmp,lignepos,colpos,energie

def deplacement_droite(chateau,tmp,lignepos,colpos,energie):
    if limites(chateau,lignepos,colpos+1)==True:
        chateau[lignepos][colpos]=tmp 
        tmp=chateau[lignepos][colpos+1]
        chateau[lignepos][colpos+1]="*"
        colpos+=1
        chateau,tmp,lignepos,colpos,energie=test_salle(chateau,tmp,lignepos,colpos,energie)
    return chateau,tmp,lignepos,colpos,energie

def maitre(chateau,tmp,lignepos,colpos): #gère les conséquences d'une rencontre avec le maître
    print("Le maître du château vous a attrapé ! Il vous chuchote : ""Retourne à la réception, là où est ta place")
    chateau[lignepos][colpos]=tmp
    lignepos=9 #redéfini les coordonnées du joueur sur la réception qui est en 9,4
    colpos=4
    tmp=chateau[lignepos][colpos] #modifie le tmp pour qu'il stock temporairement la valeur du couloir de la réception avant d'y déplacer le "*" du joueur
    chateau[lignepos][colpos]="*"
    return chateau,tmp,lignepos,colpos

def savant(energie,chateau,tmp,lignepos,colpos): #conséquences d'une rencontre avec le savant fou
    print("Vous rencontrez le savant fou et avant que vous ne vous en rendiez compte il vous a soutiré 1 d'énergie et vous a téléporté quelque part dans le château !")
    energie=energie-1 #retire 1 énergie au compteur
    chateau[lignepos][colpos]=tmp
    lignepos,colpos=case(chateau) #redéfini aléatoirement via la fonction case les coordonnées du joueur
    tmp=chateau[lignepos][colpos]
    chateau[lignepos][colpos]="*" #replace le joueur aux nouvelles coordonnées
    environnement(chateau,lignepos,colpos)
    return chateau,tmp,lignepos,colpos,energie

def bibben(energie): #conséquence d'une rencontre avec un Bibbendum
    print("Vous pensiez trouver un chamallow à la fraise... Malheureusement vous tombez sur un Bibbendum qui vous poursuit et vous prend 2 d'énergie")
    energie=energie-2 #retire 2 énergies au compteur
    return energie

def salles_energie(chateau,tmp,energie): #conséquence d'une rencontre avec de l'énergie
    print("Vous avez trouvé",tmp," pinte(s) d'énergie !")
    energie=energie+tmp #met à jour le compteur en ajoutant la valeur stockée par tmp
    tmp="O" #Permet d'éviter de pouvoir reprendre lénergie à l'infini
    return chateau,tmp,energie

def aide(chateau):
    print("Voici le manuel d'aide:")
    print("-le but du jeux est d'atteindre le paradis P présent à la sortie du chateau")
    print("-si vous entendez un bruit de clé , le maître du chateau rôde peut-être autour de vous")
    print("-si vous entendez un rire sardonique , un savant fou est peut-être tout proche")
    print("-si vous sentez une odeur de chamallow fraise , un bibbendum est sans doute à côté")
    print("-vous avez 3 points d'énergie que vous pouvez perdre si vous rencontrez de méchantes créatures et en gagner si vous trouvez des pintes d'énergies sur votre chemin")

def narration(chateau):
    print("Vous contrôlez Gasper un gentil fantôme qui n'a qu'une seule envie : c'est de retrouver ses amis dans le monde des fantômes où il fait toujours beau! Mais Gasper se retrouve à la récéption d'un château qui a l'air lugubre et sombre. Vous devez trouver la sortie mais peut-être que ce chateau cache des pièges ...")
    print("~~ Déplacez Gasper en faisant bouger l'étoile (*) ~~")
    print("")

def environnement(chateau,lignepos,colpos): #gère les conséquences d'une présence de monstre à une case du joueur
    if chateau[lignepos+1][colpos]=="B" or chateau[lignepos-1][colpos]=="B" or chateau[lignepos][colpos+1]=="B" or chateau[lignepos][colpos-1]=="B":
        print("Vous sentez une odeur très alléchante de chamallow à la fraise")
    if chateau[lignepos+1][colpos]=="M" or chateau[lignepos-1][colpos]=="M" or chateau[lignepos][colpos+1]=="M" or chateau[lignepos][colpos-1]=="M":
        print("Vous entendez un bruit metallique ressemblant à un trousseau de clé")
    if chateau[lignepos+1][colpos]=="S" or chateau[lignepos-1][colpos]=="S" or chateau[lignepos][colpos+1]=="S" or chateau[lignepos][colpos-1]=="S":
        print("Vous entendez un étrange rire sardonique")

def affichage_programmeur(chateau): #fonction d'affichage non utilisée pour le joueur, elle permet au programmeur de print le chateau en montrant les limites, les méchants, chateau'énergie, les salles
    for ligne in chateau:
            for colonne in ligne:
                print (colonne,end=" ")
            print("")

def affichage_joueur(chateau): #affichage pour le joueur qui transpose les limites X par des espaces, et print des O à la place des monstres et des pintes d'énergie
    for ligne in chateau:
            for colonne in ligne:
                if colonne=="X":
                    colonne=" "
                if colonne in ("M","B","S",1,2,3):
                    colonne="O"
                print (colonne,end=" ")
            print("")

### MAIN ###
if __name__=="__main__":
    chateau=[] #défini le chateau de base : limites + couloirs + salles
    nblignes=11
    nbcolonnes=11
    reception=""
    lignepos=9
    colpos=4
    tmp=""
    energie=3
    chateau,nblignes,nbcolonnes,lignepos,colpos,tmp=creation_chateau(chateau,nblignes,nbcolonnes,lignepos,colpos,tmp) #créé le chateau
    choix=""
    narration(chateau)
    print("8 : aller en haut \n2 : aller en bas \n4 : aller à gauche \n6 : aller à droite \n? : accéder à l'aide \nx : quitter le jeu") #print du menu
    while energie>0: #le jeu continue tant que le compteur d'énergie est strictement supérieur à 0
        choix=str(input("faites un choix:"))
        if choix=="8":
            chateau,tmp,lignepos,colpos,energie=deplacement_haut(chateau,tmp,lignepos,colpos,energie)
            print("Il vous reste",energie,"energie(s)")
            if tmp=="P": #le paradis ne peut être atteint que par le mouvement vers le haut
                print("Vous avez gagné, vous avez atteint le paradis!")
                break
        elif choix=="2":
            chateau,tmp,lignepos,colpos,energie=deplacement_bas(chateau,tmp,lignepos,colpos,energie)
            print("Il vous reste",energie,"energie(s)")
        elif choix=="4":
            chateau,tmp,lignepos,colpos,energie=deplacement_gauche(chateau,tmp,lignepos,colpos,energie)
            print("Il vous reste",energie,"energie(s)")
        elif choix=="6":
            chateau,tmp,lignepos,colpos,energie=deplacement_droite(chateau,tmp,lignepos,colpos,energie)
            print("Il vous reste",energie,"energie(s)")
        elif choix=="?":
            aide(chateau)
        elif choix=="x":
            break
        else : #gère chateau'erreur d'une commande autre qu'un déplacement
            print("Commande inconnue")
        environnement(chateau,lignepos,colpos)
        affichage_joueur(chateau)
    if energie<=0: #gère le game over
        print("energie:0 game over")
