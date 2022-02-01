"""
First Set Up Pawnchess and smol UI
"""

import sys
from chessgame.main.game import pvp_game, pve_game, get_save_game

#"Startscreen" of the Game
if __name__ == "__main__":

    #Input to divide into different cases
    CASE_ABFRAGE = input("""\nWillkommen beim Bauernschach der glorreichen Gruppe 3!\nWie wollen sie spielen?
    \tPvP\t[1]\n\t\tPvE\t[2]\n\t\tSpiel fortsetzen [3]\n""")

    #Cases
    if CASE_ABFRAGE == "1":
        pvp_game()

    elif CASE_ABFRAGE == "2":
        pve_game()

    elif CASE_ABFRAGE == "3":
        get_save_game()

    #Exception [Consider: loop to get back ti input instead of sys.exit]
    else:
        print("Bitte halten sie sich an die möglichen Eingaben!")
        sys.exit(404)
