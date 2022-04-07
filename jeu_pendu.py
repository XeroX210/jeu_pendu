## Thème 3 : Types de base : les string en Python

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#d'abord le joueur 1 donne le mot à deviner...
#on vérifie que c'est bien un mot composé de lettres de l'alphabet !
pas_valide=True #variable booleenne qui vaut Vrai si le mot n'est pas valide et Vrai sinon
while pas_valide:
	print("--------------\n JEU DU PENDU\n--------------\n")
	mot=input("Joueur 1, entrez le mot mystère : ").upper() #on met le mot proposé en majuscules
	pas_valide=False
	for car in mot:														#teste si tous les caracteres
		if car not in alphabet:pas_valide=True							#sont des lettres
	if pas_valide:
		print("MOT NON VALIDE")
		input("Pressez Entrer pour recommencer")


ca_joue=True #variable booléenne pour continuer de jouer tant qu'on n'a pas trouvé le mot et qu'on a des jockers
gagne=False
perdu=False
jokers=6
chaine="-"*len(mot)			#chaine indice initialisee avec des tirets composée d'autant de tirets que le mot à deviner a de lettres
proposees=""                #lettres proposées
nouvelle_chaine = ""
while ca_joue:
    print("--------------\n JEU DU PENDU\n--------------\n")
    print("Mot inconnu : ",chaine)
    print("Lettres déjà proposées : ",proposees)
    print("Jokers : ",jokers)
    lettre=input("Joueur 2, proposez une lettre : ").upper()


    if jokers==0:
        print("Dommage! Tu as perdu..")
    if lettre in alphabet and len(lettre)==1 : #on verifie que le joueur 2 donne bien une lettre
        if lettre not in proposees:										#la lettre a-t-elle été proposée
            if lettre in mot:
                nouvelle_chaine=""
                for i in range(len(mot)):
                    if mot[i]==lettre:
                        nouvelle_chaine=nouvelle_chaine+lettre
                    else :
                         nouvelle_chaine=nouvelle_chaine+chaine[i]              #chaine=mot   ou joker=0 v
                chaine=nouvelle_chaine

                #a compléter pour créer le mot avec les bonnes lettres sinon les tirets et gérer les varaibles jockers, gagne
                # il faut créer une variable temporaire pour créer ce mot indice
                # puis actualiser la variable chaine
            else:
                jokers-=1

            proposees+=lettre
        else: print("LETTRE DEJA PROPOSEE!")
    else: print("CE N'EST PAS UNE LETTRE!")
    if chaine==mot:
        gagne=True
    if jokers==0:
        perdu=True
    ca_joue= not(gagne or perdu)


if gagne:
	print("\nVOUS AVEZ GAGNE")
	if jokers==0:print("C'ETAIT JUSTE!")
	elif jokers==6:print("0 FAUTE : DIVINATION!")
else: print("\nVOUS AVEZ PERDU")
print("Le mot etait ",mot)