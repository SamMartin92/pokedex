import requests
import time
import pokebase as pb
import os
import random


GENERATION = 1
gen_resource = None


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
    Allows user to choose from menu and handles errors
    """

    try:
        menu_selection = int(input(""))
        if menu_selection == 1:
            print("choice 1")
            # open_description()
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
            raise ValueError
    except ValueError:
        print("Not a valid input. Please type '1', '2' or '3' to make your selection")
        make_menu_choice()


def find_pokemon():
    """
    Allows user to key in name or id of pokemon and
    seek out information about it
    """
    try:
        selected_pokemon_id_or_name = input("Please enter the name or id (1-150) of the pokemon you wish to search for\n")
        gen_1_pokemon = [pokemon.name.title() for pokemon in gen_resource.pokemon_species]

        #Name search
        if selected_pokemon_id_or_name.capitalize() in gen_1_pokemon:
            pb_pokemon_data = pb.pokemon(selected_pokemon_id_or_name.lower())
            display_pokemon(pb_pokemon_data)
        #Id search
        elif int(selected_pokemon_id_or_name) in range(1,151):
            pb_pokemon_data = pb.pokemon(int(selected_pokemon_id_or_name))
            display_pokemon(pb_pokemon_data)
        else:
            raise ValueError
    except ValueError:
            print("Not a valid entry.")
            find_pokemon()

def display_pokemon(pb_pokemon_data):
    """
    Displays info about pokemon and launches get_pokemon_data
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon.id}/")
    pokemon_api_response = response.json()
    name = pokemon_api_response["name"]
    description = pokemon_api_response["flavor_text_entries"]
    print(f"You have chosen pokemon number {pb_pokemon_data.id}: {name}")
    print("\n")
    print(f"Some information about {name}:")
    print("\n")
    print(f"{description[0]['flavor_text'].replace('/n', '')}")
    print("\n")
    print(f"{description[2]['flavor_text'].replace('/n', '')}")
    print("\n")
    print(f"What else do you want to know about {name}?")
    get_more_pokemon_data(pb_pokemon_data)



def get_more_pokemon_data(pb_pokemon_data):
    """
    Allows user to select the data they wish to see about chosen pokemon
    """

    print("\n\n")
    print("Input 1 for type")
    print("Input 2 for height")
    print("Input 3 for weight")
    print("Input 4 for locations")
    print("Input 6 for evolution chain")
    print("Input 7 to return to main menu")

    try:
        data_select = input("")
        if data_select == "1":
            clear_console()
            for type_slot in pb_pokemon_data.types:
                print(f"{pb_pokemon_data} has the following type(s):")
                print('{}: {}'.format(type_slot.slot, type_slot.type.name.title()))
                get_more_pokemon_data(pb_pokemon_data)
        elif data_select == "2":
            clear_console()
            print(f"{pb_pokemon_data} is {pb_pokemon_data.height} decimetres in height.")
            get_more_pokemon_data(pb_pokemon_data)
        elif data_select =="3":
            clear_console()
            print(f"{pb_pokemon_data} is {pb_pokemon_data.weight} hectograms in weight.")
            get_more_pokemon_data(pb_pokemon_data)
        elif data_select == "5":
            get_location_data(pb_pokemon_data)
        elif data_select == "6":
            clear_console()
            get_evolution_chain(pb_pokemon_data)
        elif data_select =="7":
            open_menu()
        else:
            raise ValueError
    except ValueError:
        print("That is not a valid input")
        get_more_pokemon_data(pb_pokemon_data)


def get_location_data(pokemon):
    """
    Retrieves location data for selected pokemon
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.id}/encounters")
    location_info = response.json()
    #Print location data here and call



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


def show_and_return_pokemon_habitats():
    habitats = requests.get("https://pokeapi.co/api/v2/pokemon-habitat/")
    available_habitats = habitats.json()['results']
    print("Where would you like to search for pokemon?")
    print("\n")
    for x in available_habitats:
        print('{}:{}'.format(available_habitats.index(x)+ 1, x['name']))
    print("\n")
    return available_habitats



def catch_pokemon():
    """
    Opens catch pokemon feature. Randomly generates pokemon from habitat and user can 'catch' or get info on pokemon
    """
    available_habitats = show_and_return_pokemon_habitats()

    habitat_id_selected = int(input(""))

    #Assuming here that habitat_select is a integer
    selected_habitat = available_habitats[habitat_id_selected - 1]
    url_for_habitat_species = selected_habitat['url']
    response = requests.get(url_for_habitat_species)
    response_json = response.json()
    pokemon_for_selected_habitat = response_json["pokemon_species"]
    random_habitat_pokemon = random.choice(pokemon_for_selected_habitat)
    print(f"A wild {random_habitat_pokemon['name']} appeared!"



def main():
    global gen_resource
    run_landing_page()
    gen_resource = pb.generation(GENERATION)
    open_menu()
    make_menu_choice()

main()