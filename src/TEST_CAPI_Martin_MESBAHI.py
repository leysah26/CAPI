# test_mon_application.py
import pytest
from CAPI_MARTIN_MESBAHI import (B_Carte_fonction, Changement_Fenetre, fichier_tache, root,
                         Mode_jeu, tour_joueur, num_tache, Note, accord, Note_moyenne,
                         Player, nom_partie)

# Mock ou simulateur de votre module customtkinter
class MockCTkButton:
    def __init__(self, master, width, height, text, font, corner_radius, command):
        self.master = master
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.corner_radius = corner_radius
        self.command = command

# Mock ou simulateur du module customtkinter
class MockCTkLabel:
    def __init__(self, master, width, height, text, text_color, font, justify, anchor, pady, fg_color, corner_radius):
        self.master = master
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        self.font = font
        self.justify = justify
        self.anchor = anchor
        self.pady = pady
        self.fg_color = fg_color
        self.corner_radius = corner_radius



@pytest.fixture


def test_B_Carte_fonction(setup):
    # mise en place les conditions initiales pour le test
    global Note, tour_joueur, Mode_jeu, accord, Note_moyenne, fichier_tache, num_tache
    Note = []
    tour_joueur = 0
    Mode_jeu = "Strict"
    accord = False
    Note_moyenne = 0
    num_tache = 0

    # Appel de la fonction a tester
    B_Carte_fonction(0)

    # utilisation des assertions pour vérifier le comportement de la fonction
    assert tour_joueur == 1
    assert Note == ["0"]


