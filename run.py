import requests
import time
import pokebase as pb
import os
""""
value = 'bulbasaur'
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{value}")
pokedex_data = response.json()
print(pokedex_data)"""


def clear_console():
    """
    Clears all data from terminal when called
    """
    os.system('clear')



def run_landing_page():
    print(" _____     ____    _  __  ______   _____    ______  __   __")
    print("|  __ \   / __ \  | |/ / |  ____| |  __ \  |  ____| \ \ / /")
    print("| |__) | | |  | | | ' /  | |__    | |  | | | |__     \ V / ")
    print("|  ___/  | |  | | |  <   |  __|   | |  | | |  __|     > <  ")
    print("| |      | |__| | | . \  | |____  | |__| | | |____   / . \ ")
    print("|_|       \____/  |_|\_\ |______| |_____/  |______| /_/ \_\ ")                                                   
  


    print('''


    
    
    MMMMMMMMMMMMMMMMMMMMMMMWN0xoc;'....     ....';cok0NWMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMNOo:'.                       ..:oONWMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMWNkc'          ..............         'ckXMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMW0o'       ...',;;;;;;;;;;;;;;;,'...       'o0WMMMMMMMMMMMMMM
    MMMMMMMMMMMMW0c.      ..,;;;;;;;;;;;;;;;;;;;;;;;;,'..      .c0WMMMMMMMMMMMM
    MMMMMMMMMMMXl.     ..,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,..     .lKMMMMMMMMMMM
    MMMMMMMMMWk,     .';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,'.     'kWMMMMMMMMM
    MMMMMMMMNo.    .';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,'.    .oNMMMMMMMM
    MMMMMMMXl     .,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,.     lXMMMMMMM
    MMMMMMNl     .;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,,.     lNMMMMMM
    MMMMMWd.    .;;;;;;;;;;;;;;;;;;;;,''''''',;;;;;;;;;;;;;;;,,,,,.    .dWMMMMM
    MMMMM0'    .,;;;;;;;;;;;;;;;;;'..         ..';;;;;;;;;;;;;,,,,,.    '0MMMMM
    MMMMWo    .';;;;;;;;;;;;;;;;'.     .....     .';;;;;;;;;;;,,,,,,.    oWMMMM
    MMMMK,    .;;;;;;;;;;;;;;;;.    'oOKXNXKOo'    .;;;;;;;;;;,,,,,,.    ,KMMMM
    MMMMO.    .''''' ''''''''     'cKMMMMMMMMWKc'     '''''''''''''''.   .OMMMM
    MMMMk.                        '0MMMMMMMMMMM0'                        .kMMMM
    MMMMk.     ...............    '0MMMMMMMMMMM0'    .... ...            .kMMMM
    MMMMO.   .x000000000000000d.   cXMMMMMMMMMKc   .d000000000Okkkkkc.   .OMMMM
    MMMMK,   .kMMMMMMMMMMMMMMMNd.   'oOKXNXKOo'   .dWMMMMMMMMWNXXXXKc    ,KMMMM
    MMMMWo    cNMMMMMMMMMMMMMMMWO;     .....    .;OWMMMMMMMMMWXXXXXk'    oWMMMM
    MMMMM0'   .xWMMMMMMMMMMMMMMMMNOl,.       .,lONMMMMMMMMMMWNXXXX0:    '0MMMMM
    MMMMMWd.   'OWMMMMMMMMMMMMMMMMMMNKOkxxxkOKWMMMMMMMMMMMMMWXXXXKl.   .dWMMMMM
    MMMMMMNl    'OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXKl.    lNMMMMMM
    MMMMMMMXl    .dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXO:     lXMMMMMMM
    MMMMMMMMNo.   .:0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXKd'    .oNMMMMMMMM
    MMMMMMMMMWk'    .l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNXKx,     'kWMMMMMMMMM
    MMMMMMMMMMMXo.    .ckNMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXOo,     .oXMMMMMMMMMMM
    MMMMMMMMMMMMW0l.     'lkXWMMMMMMMMMMMMMMMMMMMMMMWXOo;.     .c0WMMMMMMMMMMMM
    MMMMMMMMMMMMMMWKo'      .;lx0XNWMMMMMMMMMMMWNKko:'.      'oKWMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMNkc'        .';:clllolllc:,..        'ckNMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMWNOo:'.                       .':oONMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMWN0koc;,....     ....,;cok0NWMMMMMMMMMMMMMMMMMMMMMMM



        ''')

    time.sleep(2)
    clear_console()


def open_menu():
    """
    Opens the menu after landing page
    """
    print("\n")
    print("Welcome to your Pokedex:")
    print("- (1) About Pokedex")
    print("- (2) Search Pokemon")
    print("- (3) Catch a pokemon")
    print("Please input '1', '2' or '3' below to select from the menu")

def make_menu_choice():
    """
    Allows user to choose from menue and handles errors
    """
    try:
        menu_selection = int(input(""))
        if menu_selection == 1:
            print("choice 1")
            open_description():

        elif menu_selection == 2:
            print("yep")
            get_pokemon_data()
        
        elif menu_selection == 3:
            print("ok")
            catch_pokemon()
        
        else:
            print("Not a valid input. Please type '1', '2' or '3' to make your selection")
            make_menu_choice()
    except ValueError:
        print("Not a valid input. Please type '1', '2' or '3' to make your selection")
        make_menu_choice()

    
        
            



run_landing_page()
open_menu()
make_menu_choice()
