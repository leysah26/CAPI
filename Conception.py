import tkinter as tk
import tkinter.font as tkFont
import customtkinter

def B_Upload_fonction():
    fichier = tk.filedialog.askopenfilename()
    if fichier[-5:] == ".json" :
        print("Chemin du fichier sélectionné :", fichier)
        L_Erreur.configure(
            text = "Le fichier a correctement été sélectionné !",
            text_color = "#2cc985")
    else :
        L_Erreur.configure(
            text = "Le fichier sélectionné n'est pas un fichier JSON ou n'existe pas.",
            text_color = "#e43d3d")

def R_Mode2_fonction():
    print("command")


def R_Mode1_fonction():
    print("command")


def B_Player_fonction():
    player_name = E_Player.get() # Obtenir le texte de l'entrée E_Player
    if player_name:  # S'assurer qu'il y a du texte à ajouter
        TB_Player.configure(state = tk.NORMAL)
        TB_Player.insert(tk.END, player_name + "\n")
        aaa = customtkinter.CTkRadioButton(master = TB_Player)
        #TB_Player.insert(tk.END, aaa)  # Ajouter le texte à la ListBox TB_Player
        TB_Player.configure(state = tk.DISABLED)
        E_Player.delete(0, tk.END)  # Effacer le champ d'entrée après l'ajout

def B_Start_fonction():
    print("command")


def B_Retour_fonction():
    print("command")


def B_Supprimer_fonction():
    print("command")


def B_Remonter_fonction():
    print("command")


def B_Descendre_fonction():
    print("command")

################# 

customtkinter.set_appearance_mode("Light") 
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Planning Poker")
root.geometry("1280x720")

# E -> Zone d'édition
# B -> Boutton
# R -> Radio Boutton
# I -> Image
# L -> Label
# TB -> TextBox

L_Titre = customtkinter.CTkLabel(
    master = root,
    width = 500,
    height = 80,
    text = "PLANNING POKER",
    text_color = "#555555",
    font = customtkinter.CTkFont(size = 60, weight = "bold"),
    fg_color = "#f9f9fa",
    corner_radius = 25) 
L_Titre.place(x = 390, y = 30)

E_NomPartie = customtkinter.CTkEntry(
    master = root,
    width = 360,
    height = 50,
    placeholder_text = "Nom partie...",
    placeholder_text_color = "#b6b6b6", # Couleur non-ecrit
    text_color = "#555555", # Couleur ecriture
    border_width = 2,
    font = customtkinter.CTkFont(size = 25))
E_NomPartie.place(x = 90, y = 150)

L_Upload = customtkinter.CTkLabel(
    master = root,
    width = 310,
    height = 50,
    text = "Tâches",
    text_color = "#555555",
    font = customtkinter.CTkFont(size = 25),
    fg_color = "#f9f9fa",
    corner_radius = 8)
L_Upload.place(x = 90, y = 240)

B_Upload = customtkinter.CTkButton(
    master = root,
    width = 50,
    height = 50,
    corner_radius = 8,
    text = "+",
    font = customtkinter.CTkFont(size = 35),
    command = B_Upload_fonction)
B_Upload.place(x = 410, y = 240)

L_Radio = customtkinter.CTkLabel(
    master = root,
    width = 30,
    height = 30,
    corner_radius = 8,
    text = "⚙",
    text_color = "#555555",
    fg_color = "#f9f9fa",
    font = customtkinter.CTkFont(size = 20))
L_Radio.place(x = 90, y = 330)

radio_var = tk.IntVar(value=0)

R_Mode1 = customtkinter.CTkRadioButton(
    master = root,
    variable = radio_var,
    value = 1,
    width = 150,
    height = 30,
    text = "Unanimité",
    text_color = "#555555",
    font = customtkinter.CTkFont(size = 20),
    command = R_Mode1_fonction)
R_Mode1.place(x = 150, y = 330)
R_Mode1.select()

R_Mode2 = customtkinter.CTkRadioButton(
    master = root,
    variable = radio_var,
    value = 2,
    width = 150,
    height = 30,
    text = "Moyenne",
    text_color = "#555555",
    font = customtkinter.CTkFont(size = 20),
    command = R_Mode2_fonction)
R_Mode2.place(x = 310, y = 330)

E_Player = customtkinter.CTkEntry(
    master = root,
    width = 310,
    height = 50,
    placeholder_text = "Player...",
    placeholder_text_color = "#b6b6b6", # Couleur non-ecrit
    text_color = "#555555", # Couleur ecriture
    border_width = 2,
    font = customtkinter.CTkFont(size = 25))
E_Player.place(x = 90, y = 400)

B_Player = customtkinter.CTkButton(
    master = root,
    width = 50,
    height = 50,
    corner_radius = 8,
    text = "+",
    font = customtkinter.CTkFont(size = 35),
    command = B_Player_fonction)
B_Player.place(x = 410, y = 400)

TB_Player = customtkinter.CTkTextbox(
    master = root,
    width = 260,
    height = 200,
    corner_radius = 8,
    fg_color = "#f9f9fa")
TB_Player.configure(state = tk.DISABLED)
TB_Player.place(x = 90, y = 480)

B_Remonter = customtkinter.CTkButton(
    master = root,
    width = 70,
    height = 30,
    corner_radius = 8,
    text = "↑",
    font = customtkinter.CTkFont(size = 20),
    command = B_Remonter_fonction)
B_Remonter.place(x = 380, y = 500)

B_Descendre = customtkinter.CTkButton(
    master = root,
    width = 70,
    height = 30,
    corner_radius = 8,
    text = "↓",
    font = customtkinter.CTkFont(size = 20),
    command = B_Descendre_fonction)
B_Descendre.place(x = 380, y = 540)

B_Supprimer = customtkinter.CTkButton(
    master = root,
    width = 70,
    height = 30,
    corner_radius = 8,
    text = "X",
    font = customtkinter.CTkFont(size = 20),
    command = B_Supprimer_fonction)
B_Supprimer.place(x = 380, y = 630)

I_Preview = tk.Button(root) ### /!\ ###
I_Preview["bg"] = "#f0f0f0" 
I_Preview["font"] = tkFont.Font(family = 'Helvetica', size = 10)
I_Preview["fg"] = "#000000"
I_Preview["justify"] = "center"
I_Preview["text"] = "image"
I_Preview.place(x = 600, y = 150, width = 500, height = 300)

B_Start = customtkinter.CTkButton(
    master = root,
    width = 300,
    height = 80,
    corner_radius = 8,
    text = "🃏 Start 🃏",
    font = customtkinter.CTkFont(size = 25),
    command = B_Start_fonction)
B_Start.place(x = 700, y = 530)

L_Erreur = customtkinter.CTkLabel(
    master = root,
    width = 500,
    height = 30,
    text = "gnagnagna",
    text_color = "#ebebeb",
    font = customtkinter.CTkFont(size = 12)) 
L_Erreur.place(x = 600, y = 640)

B_Retour = customtkinter.CTkButton(
    master = root,
    width = 70,
    height = 30,
    corner_radius = 8,
    text = "Retour",
    font = customtkinter.CTkFont(size = 15),
    command = B_Retour_fonction)
B_Retour.place(x = 1180, y = 670)

root.mainloop()
