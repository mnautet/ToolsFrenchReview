# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:51:52 2025

@author: maelys.nautet
"""
Figures_d_analogie={"Mise en relation de deux éléments avec un comparatif":"comparaison",
                    "Comparaison sans outil comparatif":"metaphore",
                    "Attribuer des traits humains à un objet ou une idée":"personnification",
                    "Représentation concrète d'une idée abstraite":"allegorie",
                    "Remplacer un mot par un autre lié":"metonymie"}
Figures_d_insistance_et_d_amplification={"Répétition d un mot en début de phrase ou de vers":"anaphore",
                                        "Répétition de mot ayant le meme sens":"pleonasme",
                                        "Énumération de plusieurs éléments":"accumulation",
                                        "Énumération d éléments de plus en plus forts (ou décroissants)":"gradation",
                                        "Exagération":"hyperbole",
                                        "Dire moins pour faire entendre plus":"litote",
                                        "Atténuer une réalité choquante ou désagréable":"euphemisme"}
Figures_d_opposition={"Opposition entre deux idées dans une meme phrase":"antithese",
                    "Deux mots opposés côte à côte":"oxymore",
                    "Énoncé qui semble contradictoire":"paradoxe",
                    "Croisement dans la construction":"chiasme"}
Figures_de_substitution_et_d_expression_détournée={"Remplacer un mot par une expression qui le définit":"periphrase",
                                                "Dire le contraire de ce que l’on pense":"antiphrase",
                                                "Dire qu’on ne va pas parler de quelque chose tout en le faisant":"preterition"}
Figures_de_construction={"Omission volontaire d’un ou plusieurs mots":"ellipse",
                        "Absence de lien entre des groupe (je suis venu, j ai vu..)":"asyndete",
                        "Répétition exagérée de liens de coordination(et ,et ,et ...)":"polysyndete",
                        "Répétition de la même structure syntaxique":"parallelisme"}
Figures_sonores={"Répétition d’un même son consonantique":"alliteration",
                "Répétition d’un même son vocalique":"assonance",
                "Mot qui imite un son":"onomatopee",
                "Rapprochement de mots au son proche mais au sens différent":"paronomase"}
liste=[Figures_d_analogie,Figures_d_insistance_et_d_amplification,Figures_d_opposition,Figures_de_substitution_et_d_expression_détournée,Figures_de_construction,Figures_sonores]    
for i in liste:
    non_connue=[]
    for cle, valeur in i.items():
        print(cle)
        reponse_joueur=input("=")
        if reponse_joueur==valeur:
            print("bien joué!")
            print()
        else:
            non_connue.append(valeur)
            print("dommage la reponse etait",valeur)
            print()
            
    print("===========================")
    print("Bien jouer") 
    print()    
    print()
    if non_connue!=[]:
        print("tu devrais reviser",non_connue)
        print()
        print("===========================")
        reponse=input("veux tu revoir tes erreurs?")
        if reponse=="oui":
            for cle,valeur in i.items():
                if valeur in non_connue:
                    while reponse_joueur!=valeur:
                        print(cle)
                        reponse_joueur=input("=")
            print()
            print()
                        
                        

print("Bien joué :)")   
