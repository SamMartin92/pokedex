import requests
import time
import pokebase as pb
import os


GENERATION = 1
gen_resource = pb.generation(GENERATION)


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
            open_description()
            time.sleep(2)
            clear_console()

        elif menu_selection == 2:
            time.sleep(2)
            clear_console()
            find_pokemon()       
        
        elif menu_selection == 3:
            print("ok")
            time.sleep(2)
            clear_console()
            catch_pokemon()
                    
        else:
            print("Not a valid input. Please type '1', '2' or '3' to make your selection")
            make_menu_choice()
    except ValueError:
        print("Not a valid input. Please type '1', '2' or '3' to make your selection")
        make_menu_choice()


def find_pokemon():
    """
    Allows user to key in name or id of pokemon and 
    seek out information about it
    """
    print("""Please enter the name or id (1-150) of the pokemon you wish to search for\n""")

    try:
        select_pokemon = input("")
        gen_1_pokemon = [pokemon.name.title() for pokemon in gen_resource.pokemon_species]
         
        if select_pokemon.capitalize() in gen_1_pokemon:
            pokemon_name = pb.pokemon(select_pokemon.lower())
            get_pokemon_data(pokemon_name)
       
        elif int(select_pokemon) in range(1,151):
            pokemon_name = pb.pokemon(int(select_pokemon))
            get_pokemon_data(pokemon_name)           
        else:
            print("Not a valid entry.")
            find_pokemon()

    except ValueError:
            print("Not a valid entry.")
            find_pokemon()
    

def get_pokemon_data(pokemon):
    """
    Allows user to select the data they wish to see about chosen pokemon
    """
    #clear_console()
    print(f"You have chosen pokemon number {pokemon.id}: {pokemon}")
    print(f"What do you want to know about {pokemon}?")
    print("\n\n")
    print("Input 1 for type")
    print("Input 2 for height")
    print("Input 3 for weight")
    print("Input 4 for locations")
    print("Input 6 for evolution chain")
    print("Input 7 to find a new pokemon")

    data_select = input("")
    if data_select == "1":
        for type_slot in pokemon.types:
            print(f"{pokemon} has the following type(s):")
            print('{}: {}'.format(type_slot.slot, type_slot.type.name.title()))
            get_pokemon_data(pokemon)
    elif data_select =="2":
        print(f"{pokemon} is {pokemon.height} decimetres in height.")
        get_pokemon_data(pokemon)
    elif data_select =="3":
        print(f"{pokemon} is {pokemon.weight} hectograms in weight.")
        get_pokemon_data(pokemon)
    elif data_select == "6":
        get_evolution_chain(pokemon)
    elif data_select =="7":
        make_menu_choice()
    else:
        print("That is not a valid input")
        get_pokemon_data(pokemon)

def get_evolution_chain(pokemon):
    """
    Retrieves evoluton data for selected pokemon
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon.id}/")
    pokemon_species = response.json()
    evolution_data = pokemon_species['evolution_chain']['url']
    response_2 = requests.get(evolution_data)
    evolution_tree = response_2.json()["chain"]
    evolves_to = evolution_tree["evolves_to"]

    if evolves_to == []:
        print(f"{pokemon} has no evolutionary chain.")
    elif evolves_to[0]["evolves_to"] ==[]:
        print(f"{evolution_tree['species']['name']} evolves into {evolves_to[0]['species']['name']}")
    elif len(evolves_to) == 1:
        print(f"{evolution_tree['species']['name']} evolves into {evolves_to[0]['species']['name']}")
        print(f"{evolves_to[0]['species']['name']} evolves into {evolves_to[0]['evolves_to'][0]['species']['name']} ")



run_landing_page()
open_menu()
make_menu_choice()

