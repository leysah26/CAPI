"""
@file
@brief Description du fichier

@mainpage Documentation principale

@section intro_sec Introduction
Bienvenue dans la documentation de mon projet. Cette documentation a été générée en utilisant Doxygen.

@section install_sec Installation
- Installez Doxygen sur votre système.
- Exécutez `doxygen -g config_file` pour générer un fichier de configuration Doxygen.
- Modifiez le fichier de configuration (`config_file`) selon vos besoins.
- Exécutez `doxygen config_file` pour générer la documentation.

@section usage_sec Utilisation
- Exécutez le script Python.

@section note_sec Remarques
- Assurez-vous d'avoir Doxygen installé sur votre système.

@section author_sec Auteur
Auteur du code: Robin Martin, Lysa Mesbahi


"""

#pip install tk
import tkinter as tk

#pip install customtkinter
import customtkinter

import json

################################

customtkinter.set_appearance_mode("Light") 
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Planning Poker")
root.geometry("1280x720")

################################ Passage d'une fenetre a une autre

def Changement_Fenetre(fenetre):
    """
    @brief Fonction pour changer de fenêtre dans l'application.

    Cette fonction détruit tous les widgets de la fenêtre actuelle et affiche la nouvelle fenêtre.

    @param fenetre: La fonction de la nouvelle fenêtre à afficher.
    """

    for widget in root.winfo_children():
        widget.destroy()

    if fenetre in [Menu, Creation_Partie]:
        L_Titre = customtkinter.CTkLabel(
            master = root, width = 550, height = 80,
            text = "PLANNING POKER ", text_color = "#555555", font = customtkinter.CTkFont("Brush Script MT", size = 60, weight = "bold"),
            fg_color = "#f9f9fa", corner_radius = 25) 
        L_Titre.place(x = 365, y = 30)

    fenetre()

################################ Verification de la validité du fichier json pour le chargement de partie ou pour la selection

def Verification_fichier():
    """
    @brief Fonction pour vérifier la validité d'un fichier JSON.

    Cette fonction vérifie la validité d'un fichier JSON en s'assurant qu'il respecte une structure spécifique.
    """

    global chemin_fichier
    chemin_fichier = tk.filedialog.askopenfilename()

    L_Message.configure(text = f"Le fichier sélectionné n'est pas de syntaxe correct.", text_color = "#e43d3d")
    L_Upload_Path.configure(text = "", text_color = "#ebebeb")

    if chemin_fichier[-5:] == ".json":
        with open(chemin_fichier, 'r') as file:
            fichier_tache = json.load(file)
        try:
            for i in range(len(fichier_tache['taches'])):
                if isinstance(fichier_tache['taches'],list) and isinstance(fichier_tache['parametre'],list):
                    if isinstance(fichier_tache['taches'][i]["nom"],str):
                        if isinstance(fichier_tache['taches'][i]["description"],str):
                            if isinstance(fichier_tache['taches'][i]["note"],str) or isinstance(fichier_tache['taches'][i]["note"],int):
                                pass
            if isinstance(fichier_tache['parametre'][0]["en_cours"],bool):
                if isinstance(fichier_tache['parametre'][0]["numero_tache"],str) or isinstance(fichier_tache['parametre'][0]["numero_tache"],int):
                    if isinstance(fichier_tache['parametre'][0]["mode"],str):
                        if isinstance(fichier_tache['parametre'][0]["joueur"],list) or isinstance(fichier_tache['parametre'][0]["joueur"],str):
                            if isinstance(fichier_tache['parametre'][0]["nom_partie"],str):
                                pass
        except Exception:
            chemin_fichier = ""

        else:
            if str(fichier_tache['parametre'][0]["numero_tache"]) == str(len(fichier_tache['taches'])):
                L_Message.configure(text = "La partie selectionée est deja terminée !", text_color = "#e43d3d")
                chemin_fichier = ""
            else :
                L_Message.configure(text = "Le fichier a correctement été sélectionné !", text_color = "#2cc985")
                L_Upload_Path.configure(text = chemin_fichier, text_color = "#555555") 

    else :
        L_Message.configure(text = "Le fichier sélectionné n'est pas un fichier JSON ou n'existe pas.", text_color = "#e43d3d")
        chemin_fichier = ""
 
################################################################| FENETRE MENU |################################################################

def Menu():
    """
    @brief Fonction pour afficher la fenêtre du menu principal.

    Cette fonction crée les widgets nécessaires pour la fenêtre du menu principal.
    """
    ################|     [Fonction]      |################

    def B_Start_Menu_fonction():
        """
        @brief Fonction appelée lorsqu'on clique sur le bouton 'Nouvelle Partie' du menu.

        Cette fonction change la fenêtre pour afficher la création d'une nouvelle partie.
        """
        Changement_Fenetre(Creation_Partie)
        """
        @brief Fonction appelée lorsqu'on clique sur le bouton 'Charger Partie' du menu.

        Cette fonction vérifie la validité d'un fichier JSON pour charger une partie existante.
        """
    def B_Charger_Partie_fonction():
        Verification_fichier()
        if chemin_fichier != "" :
            Changement_Fenetre(Partie)

    ################|     [Affichage]     |################

    B_Start_Menu = customtkinter.CTkButton(
        master = root, width = 450, height = 120,
        text = "Nouvelle Partie", font = customtkinter.CTkFont(size = 35),
        corner_radius = 8, command = B_Start_Menu_fonction)
    B_Start_Menu.place(x = 415, y = 225)

    B_Charger_Partie = customtkinter.CTkButton(
        master = root, width = 450, height = 120,
        text = "Charger Partie", font = customtkinter.CTkFont(size = 35),
        corner_radius = 8, command = B_Charger_Partie_fonction)
    B_Charger_Partie.place(x = 415, y = 375)

    global L_Upload_Path
    L_Upload_Path = customtkinter.CTkLabel(
        master = root, width = 450,
        text_color = "#ebebeb", font = customtkinter.CTkFont(size = 10),
        fg_color = "transparent")
    L_Upload_Path.place(x = 415, y = 500)

    global L_Message
    L_Message = customtkinter.CTkLabel(
        master = root, width = 450, height = 30,
        text = "Bonjour !", text_color = "#ebebeb", font = customtkinter.CTkFont(size = 12)) 
    L_Message.place(x = 415, y = 600)

################################################################| FENETRE CREATION PARTIE |################################################################

def Creation_Partie():
    """
    @brief Fonction pour afficher la fenêtre de création d'une nouvelle partie.

    Cette fonction crée les widgets nécessaires pour la fenêtre de création d'une nouvelle partie.
    """

    ################|     [Fonction]      |################

    

    ################################

    def R_Mode1_fonction():
        """
        @brief Fonction appelée lorsqu'on sélectionne le mode strict.

        Cette fonction met à jour l'affichage pour le mode strict.
        """
        global Mode_jeu

        TB_Preview.delete("0.0","end")
        TB_Preview.insert("0.0","\n" *4 + "Dans ce mode, les membres de l'équipe discutent de la tâche à estimer.\n\n" +
                            "Ensuite chacun donne sa propre estimation pour représenter l'effort requis.\n\n" +
                            "Si les estimations diffèrent, les membres discutent des raisons de leurs choix .\n\n" +
                            "L'objectif est d'atteindre un consensus où tous les membres de l'équipe sont d'accord.\n\n" +
                            "Cela encourage la communication et la compréhension collective de la complexité de la tâche.")
        L_Preview.configure(text = "Mode Strict")
        Mode_jeu = "Strict"


    def R_Mode2_fonction():
        """
        @brief Fonction appelée lorsqu'on sélectionne le mode non strict.

        Cette fonction met à jour l'affichage pour le mode non strict.
        """
        global Mode_jeu

        TB_Preview.delete("0.0","end")
        TB_Preview.insert("0.0","\n" *4 + "Dans ce mode, les membres de l'équipe donne leur estimation individuelle de l'effort requis pour la tâche.\n\n" +
                            "Ensuite, les estimations sont moyennées pour obtenir une estimation finale.\n\n" +
                            "Cette méthode est utile lorsque les estimations varient et que la discussion ne parvient pas à un consensus unanime.\n\n" +
                            "Elle permet de prendre en compte les différents points de vue de l'équipe sans forcément parvenir à un accord.\n\n")
        L_Preview.configure(text = "Mode Moyenne")
        Mode_jeu = "Moyenne"

    ################################

    def B_Supprimer_Player_fonction(id):
        """
        @brief Supprime un joueur de la liste des joueurs.

        Supprime un joueur de la liste des joueurs, détruit les éléments graphiques associés,
        et met à jour l'affichage.

        @param id: L'index du joueur à supprimer.
        """
        Player.pop(id)
        label_id[id].destroy(), boutton_id[id].destroy()
        label_id.pop(id), boutton_id.pop(id)
        Update_Player_Frame()

    def Update_Player_Frame():
        """
        @brief Met à jour l'affichage des joueurs.

        Détruit tous les widgets enfants du cadre F_Player, puis recrée les étiquettes et
        les boutons pour chaque joueur dans la liste Player. Met à jour l'état de l'interface
        en fonction du nombre de joueurs.

        """            
        for widget in F_Player.winfo_children():
            widget.destroy()

        global nbr_Player
        nbr_Player = len(Player)

        for i in range(nbr_Player):

            L_Player_Creation = customtkinter.CTkLabel(master = F_Player,text = Player[i], font = customtkinter.CTkFont(size = 18))
            L_Player_Creation.grid(row = i, column=0, padx = 10, pady=(0, 5))

            label_id.append(L_Player_Creation)

            B_Player_Frame = customtkinter.CTkButton(master = F_Player, width = 10, height = 10, text = "X", fg_color = "#f05050", hover_color = "#ec3e3e",
                font = customtkinter.CTkFont(size = 18, weight = "bold"),
                command = lambda id = i: B_Supprimer_Player_fonction(id))
            B_Player_Frame.grid(row = i, column = 1)
            B_Player_Frame.place(x = 310, y = 3 + 33 * (i))

            boutton_id.append(B_Player_Frame)

        E_Player.delete(0, tk.END)

        if nbr_Player >= 8: # METTRE A 8
            E_Player.configure(state = "disabled", fg_color = "#b6b6b6")
            B_Player.configure(state = "disabled")
        else :
            E_Player.configure(state = "normal", fg_color = "#f9f9fa")
            B_Player.configure(state = "normal")

    def B_Player_fonction():
        """
        @brief Fonction associée au bouton d'ajout de joueur.

        Récupère le nom du joueur à partir de l'entrée E_Player, ajoute le joueur à la liste Player,
        et met à jour l'affichage des joueurs.
        """
        player_name = E_Player.get() 

        if player_name: 
            Player.append(player_name)     
            Update_Player_Frame()

    ################################

    def B_Start_fonction():
        """
        @brief Fonction associée au bouton de démarrage de la partie.

        Vérifie les conditions nécessaires pour démarrer la partie (nom de la partie, fichier de tâches, nombre de joueurs),
        affiche un message approprié, puis démarre la partie en changeant de fenêtre.
        """
        global nom_partie

        if (E_NomPartie.get() != ""):
            if ("chemin_fichier" in globals()) and (chemin_fichier != ""):
                if ("nbr_Player" in globals()) and (nbr_Player > 1):

                    nom_partie = E_NomPartie.get()

                    L_Message.configure(text = "La partie va commencer dans 5...", text_color = "#2cc985")
                    for i in range (4,0,-1):
                        root.update()
                        root.after(1000, L_Message.configure(text = f"La partie va commencer dans {i}...", text_color = "#2cc985"))
                    root.update()
                    root.after(1000, Changement_Fenetre(Partie))

                else:
                    L_Message.configure(text = "Il faut au minimum deux Player !", text_color = "#e43d3d")
            else:
                L_Message.configure(text = "Aucun fichier de tâche selectioné !", text_color = "#e43d3d")
                print('oui' + chemin_fichier)
        else:
            L_Message.configure(text = "Il manque un nom à votre partie !", text_color = "#e43d3d")

    ################################

    def B_Retour_fonction():
        """
        @brief Fonction appelée lors du clic sur le bouton de retour.
        
        La fonction appelle la fonction Changement_Fenetre(Menu).
        """
        Changement_Fenetre(Menu)

    ################|     [Affichage]     |################

    # E -> Zone d'édition   
    # B -> Boutton           
    # R -> Radio Boutton    
    # L -> Label
    # TB -> TextBox

    ################################

    E_NomPartie = customtkinter.CTkEntry(
        master = root, width = 370, height = 50,
        placeholder_text = "Nom partie...", placeholder_text_color = "#b6b6b6", text_color = "#555555",
        border_width = 2, font = customtkinter.CTkFont(size = 25))
    E_NomPartie.place(x = 90, y = 150)

    ################################

    L_Upload = customtkinter.CTkLabel(
        master = root, width = 310, height = 50,
        text = "Tâches", text_color = "#555555", font = customtkinter.CTkFont(size = 25),
        fg_color = "#f9f9fa", corner_radius = 8)
    L_Upload.place(x = 90, y = 240)

    global L_Upload_Path
    L_Upload_Path = customtkinter.CTkLabel(
        master = root, width = 310,
        text_color = "#ebebeb", font = customtkinter.CTkFont(size = 10),
        fg_color = "transparent")
    L_Upload_Path.place(x = 90, y = 295)

    B_Upload = customtkinter.CTkButton(
        master = root, width = 50, height = 50,
        text = "+", font = customtkinter.CTkFont(size = 35),
        corner_radius = 8, command = Verification_fichier)
    B_Upload.place(x = 410, y = 240)

    ################################

    L_Radio = customtkinter.CTkLabel(
        master = root, width = 30, height = 30,
        text = "⚙", text_color = "#555555", font = customtkinter.CTkFont(size = 20),
        fg_color = "#f9f9fa", corner_radius = 8)
    L_Radio.place(x = 90, y = 330)

    radio_var = tk.IntVar(value=0)

    R_Mode1 = customtkinter.CTkRadioButton(
        master = root, variable = radio_var, value = 1, width = 150, height = 30,
        text = "Strict", text_color = "#555555", font = customtkinter.CTkFont(size = 20),
        command = R_Mode1_fonction)
    R_Mode1.place(x = 150, y = 330)
    R_Mode1.select()

    R_Mode2 = customtkinter.CTkRadioButton(
        master = root, variable = radio_var, value = 2, width = 150, height = 30,
        text = "Moyenne", text_color = "#555555", font = customtkinter.CTkFont(size = 20),
        command = R_Mode2_fonction)
    R_Mode2.place(x = 310, y = 330)

    global Mode_jeu
    Mode_jeu = "Strict"

    ################################

    E_Player = customtkinter.CTkEntry(
        master = root, width = 310, height = 50,
        placeholder_text = "Player...", placeholder_text_color = "#b6b6b6", text_color = "#555555",
        border_width = 2, font = customtkinter.CTkFont(size = 25))
    E_Player.place(x = 90, y = 400)

    B_Player = customtkinter.CTkButton(
        master = root, width = 50, height = 50,
        text = "+", font = customtkinter.CTkFont(size = 35),
        corner_radius = 8, command = B_Player_fonction)
    B_Player.place(x = 410, y = 400)

    label_id = []
    boutton_id = []
    global Player
    Player = []
    F_Player = customtkinter.CTkScrollableFrame(
        master = root, width = 345, height = 200,
        corner_radius = 8, fg_color = "#f9f9fa")
    F_Player.place(x = 90, y = 480)

    ################################

    TB_Preview = customtkinter.CTkTextbox(
        master = root, width = 500, height = 300,
        text_color = "#555555", font = customtkinter.CTkFont(size = 14),
        fg_color = "#f9f9fa", wrap = "word", corner_radius = 8)
    TB_Preview.place(x = 600, y = 150)

    L_Preview = customtkinter.CTkLabel(
        master = TB_Preview, width = 310, height = 50,
        text = "Mode Unanime", text_color = "#555555", font = customtkinter.CTkFont(size = 25, weight = "bold"),
        fg_color = "#ebebeb", corner_radius = 8)
    L_Preview.place(x = 90, y = 10)
    R_Mode1_fonction()

    ################################

    B_Start = customtkinter.CTkButton(
        master = root, width = 300, height = 80, 
        text = "🃏 Start 🃏", font = customtkinter.CTkFont(size = 25), 
        corner_radius = 8, command = B_Start_fonction)
    B_Start.place(x = 700, y = 530)

    ################################

    global L_Message
    L_Message = customtkinter.CTkLabel(
        master = root, width = 500, height = 30,
        text = "Bonjour !", text_color = "#ebebeb", font = customtkinter.CTkFont(size = 12)) 
    L_Message.place(x = 600, y = 640)

    ################################

    B_Retour = customtkinter.CTkButton(
        master = root, width = 70, height = 30,
        text = "Retour",font = customtkinter.CTkFont(size = 15),
        corner_radius = 8, command = B_Retour_fonction)
    B_Retour.place(x = 1180, y = 670)

################################################################| FENETRE PARTIE |################################################################


def Partie():
    """
    @brief Fonction pour afficher la fenêtre d'une partie en cours.

    Cette fonction crée les widgets nécessaires pour la fenêtre d'une partie en cours.
    """
    
    ################|     [Fonction]      |################

    global Mode_jeu
    global tour_joueur
    global num_tache
    global Note
    global accord
    global Note_moyenne
    global Player
    global nom_partie

    ################################

    with open(chemin_fichier, 'r') as file:
        fichier_tache = json.load(file)

    if fichier_tache["parametre"][0]["en_cours"] == True:
        num_tache = int(fichier_tache["parametre"][0]["numero_tache"])
        Mode_jeu = fichier_tache["parametre"][0]["mode"]
        Player = fichier_tache["parametre"][0]["joueur"]
    else:
        num_tache = 0
        fichier_tache["parametre"][0]["en_cours"] = True
        fichier_tache["parametre"][0]["numero_tache"] = num_tache
        fichier_tache["parametre"][0]["mode"] = Mode_jeu
        fichier_tache["parametre"][0]["joueur"] = Player
        fichier_tache["parametre"][0]["nom_partie"] = nom_partie
        with open(chemin_fichier, "w") as fichier:
            json.dump(fichier_tache, fichier, indent=2)

    nbr_Player = len(Player)
    tour_joueur = 0
    Note = []
    Note_moyenne = 0
    accord = False

    ################################

    def B_Carte_fonction(id):
        """
        @brief Fonction appelée lors du clic sur une carte.
        
        @param id: Identifiant de la carte cliquée.
        @type id: int
        
        La fonction gère le déroulement du jeu en fonction du mode de jeu (Strict ou Moyenne).
        Elle met à jour les notes, le tour des joueurs, et affiche les informations en conséquence.
        """
        
        global Mode_jeu
        global tour_joueur
        global num_tache
        global Note
        global accord
        global Note_moyenne
        global Player
        global nom_partie

    ################################

        Note.append(cartes[id])
        print(Note)

        tour_joueur += 1
    
        if tour_joueur == nbr_Player:
            tour_joueur = 0

        L_Tour_Player.configure(text = Player[tour_joueur])

        if tour_joueur == 0:

        ################################        

            if Mode_jeu == "Strict":

                accord = True
                for element in Note:
                    if element == Note[0]:
                        continue
                    else :
                        accord = False

                if accord == True:
                    Note_moyenne = Note[0] 
                else :
                    L_Message_Partie.configure(text = f"La priorité de la tâche '{fichier_tache['taches'][num_tache]['nom']}' n'a pas été définie.", text_color = "#e43d3d")

        ################################    

            if Mode_jeu == "Moyenne":

                accord = True
                for element in Note:
                    Note_moyenne = Note_moyenne + int(element)
                Note_moyenne = Note_moyenne / len(Note)

        ################################

            if accord == True:
                fichier_tache['taches'][num_tache]['note'] = str(Note_moyenne)
                fichier_tache['taches'][num_tache]['terminer'] = True
                fichier_tache['parametre'][0]['numero_tache'] = num_tache + 1
                with open(chemin_fichier, "w") as fichier:
                    json.dump(fichier_tache, fichier, indent=2)

                L_Message_Partie.configure(text = f"La priorité de la tâche '{fichier_tache['taches'][num_tache]['nom']}' est de {Note_moyenne}.", text_color = "#2cc985")

                num_tache += 1

        ################################

            Note_moyenne = 0
            Note = []

        ################################

            if num_tache < len(fichier_tache['taches']):
                L_Titre_Tache.configure(text = fichier_tache['taches'][num_tache]['nom'])
                L_Tache.configure(text = fichier_tache['taches'][num_tache]['description'])

            else :
                L_Tour.destroy()
                L_Tour_Player.destroy()
                L_Titre_Tache.destroy()
                for i in range(10):
                    boutons_partie[i].destroy()

                B_Fin = customtkinter.CTkButton(
                    master = root, width = 300, height = 110,
                    text = "Quitter", font = customtkinter.CTkFont(size = 25, weight = "bold"),
                    corner_radius = 8,
                    command = root.destroy)
                B_Fin.place(x = 490, y = 550)

                L_Tache.configure(text = "Fin de la partie", anchor = "center", font = customtkinter.CTkFont(size = 40, weight = "bold"))

    ################|    [Affichage]     |################

    L_Tache = customtkinter.CTkLabel(
        master = root, width = 650, height = 100,
        text = fichier_tache['taches'][num_tache]['description'], text_color = "#555555", font = customtkinter.CTkFont(size = 20),
        justify = "center", anchor = "s", pady = 20, fg_color = "#f9f9fa", corner_radius = 8)
    L_Tache.place(x = 315, y = 30)

    L_Titre_Tache = customtkinter.CTkLabel(
        master = L_Tache, width = 150, height = 30,
        text = fichier_tache['taches'][num_tache]['nom'], text_color = "#555555", font = customtkinter.CTkFont(size = 30, weight = "bold"), )
    L_Titre_Tache.place(x = 250, y = 10)

    L_Tour = customtkinter.CTkLabel(
        master = root, width = 450, height = 0,
        text = "À toi de choisir ta note", text_color = "#555555", font = customtkinter.CTkFont(size = 30, weight = "bold"),
        fg_color = "transparent")
    L_Tour.place(x = 415, y = 200)

    L_Tour_Player = customtkinter.CTkLabel(
        master = root, width = 350, height = 70,
        text = Player[tour_joueur], text_color = "#555555", font = customtkinter.CTkFont(size = 30, weight = "bold"),
        fg_color = "#f9f9fa", corner_radius = 8)
    L_Tour_Player.place(x = 465, y = 250)

    L_Message_Partie = customtkinter.CTkLabel(
        master = root, width = 650, height = 0,
        text = "Bonjour !", text_color = "#ebebeb", font = customtkinter.CTkFont(size = 15))
    L_Message_Partie.place(x = 315, y = 450)

    cartes = ["0","1","2","3","5","8","13","20","40","100"]
    boutons_partie = []

    for i in range(10): 
        B_Carte = customtkinter.CTkButton(
            master = root, width = 90, height = 135,
            text = cartes[i], font = customtkinter.CTkFont(size = 25, weight = "bold"),
            corner_radius = 8,
            command = lambda id = i: B_Carte_fonction(id))
        B_Carte.place(x = 50 + i * 118, y = 550)

        boutons_partie.append(B_Carte)

################################################################| MAINLOOP |################################################################

Changement_Fenetre(Creation_Partie)
Changement_Fenetre(Menu)
root.mainloop()
