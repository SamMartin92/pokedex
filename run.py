import requests
import time
import pokebase as pb
import os
import random
import gspread
from google.oauth2.service_account import Credentials

#Constant variables
GENERATION = 1
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pokedex_sheet')

gen_resource = None
trainer_name = None


def clear_console():
    """
    Clears all data from terminal when called
    """
    os.system('clear')


def enter_trainer_name():
    """
    Takes users trainer name to link to any data from previous uses of the app.
    Adds it to linked google sheet if it has not been addded previously.
    """ 
    trainer_sheet = SHEET.worksheet('trainer_data')
    trainers_list = trainer_sheet.row_values(1)
    sprites_sheet = SHEET.worksheet("sprites_data")
    print("Hello trainer. Please enter your name:\n")
    trainer_name = input("")
    if trainer_name.lower() in trainers_list:
        print(f"Welcome back {trainer_name}")
    else:
        print(f"Welcome {trainer_name}")
        for n in range(1,200):
            if trainer_sheet.cell(1,n).value == None:
                trainer_sheet.update_cell(1, n, trainer_name.lower())
                sprites_sheet.update_cell(1, n, trainer_name.lower())
                break        
    time.sleep(1.5)
    return trainer_name
    


def run_landing_page():
    clear_console()
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
    print("Initiating Pokadex...")
    time.sleep(1)
    clear_console()
    open_menu()


def open_menu():
    """
    Opens the menu after landing page
    """
    print("\n")
    print("Welcome to your Pokedex:")
    print("- (1) About Pokedex")
    print("- (2) Search Pokemon")
    print("- (3) Catch a pokemon")
    print("- (4) View your pokemon")
    print("Please input '1', '2', '3' or '4' below to select from the menu")
    make_menu_choice()


def make_menu_choice():
    """
    Allows user to choose from menu and handles errors
    """

    try:
        menu_selection = int(input(""))
        if menu_selection == 1:
            # open_description()
            time.sleep(2)
            clear_console()

        elif menu_selection == 2:
            time.sleep(2)
            clear_console()
            find_pokemon()

        elif menu_selection == 3:
            time.sleep(2)
            clear_console()
            encounter_wild_pokemon()
        
        elif menu_selection == 4:
            view_caught_pokemon()

        else:
            raise ValueError
    except ValueError:
        print("Not a valid input. Please type '1', '2', '3' or '4' to make your selection")
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
    display_flavour_text(pb_pokemon_data)
    get_more_pokemon_data(pb_pokemon_data)


def display_flavour_text(pb_pokemon_data):
    """
    Prints out two short descriptions about selected pokemon
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pb_pokemon_data.id}/")
    pokemon_api_response = response.json()
    name = pokemon_api_response["name"]
    description = pokemon_api_response["flavor_text_entries"]
    print(f"Pokemon number {pb_pokemon_data.id}: {name.capitalize()}")
    print("\n")
    print(f"Some information about {name.capitalize()}:")
    print("\n")
    print(f"{description[1]['flavor_text'].replace('', ' ')}")
    print("\n")
    if description[1]['flavor_text'] == description[2]['flavor_text']:
        print(f"{description[5]['flavor_text'].replace('', '')}")
    else:
        print(f"{description[2]['flavor_text'].replace('', '')}")
    print("\n")


def get_more_pokemon_data(pb_pokemon_data):
    """
    Allows user to select the data they wish to see about chosen pokemon
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pb_pokemon_data.id}/")
    pokemon_api_response = response.json()
    name = pokemon_api_response["name"]
    print(f"What else do you want to know about {name.capitalize()}?")
    print("\n\n")
    print("Input 1 for type")
    print("Input 2 for height")
    print("Input 3 for weight")
    print("Input 4 for locations")
    print("Input 5 for moves info")
    print("Input 6 for evolution chain")
    print("Input 7 to return to main menu")

    try:
        data_select = input("")
        if data_select == "1":
            print(f"\n{name.capitalize()} has the following type(s):")
            for type_slot in pb_pokemon_data.types:                
                print('{}: {}'.format(type_slot.slot, type_slot.type.name.title()))
                print("\n")
            get_more_pokemon_data(pb_pokemon_data)
        elif data_select == "2":
            print(f"\n{name.capitalize()} is {pb_pokemon_data.height} decimetres in height.\n")
            get_more_pokemon_data(pb_pokemon_data)
        elif data_select =="3":
            print(f"\n{name.capitalize()} is {pb_pokemon_data.weight} hectograms in weight.\n")
            get_more_pokemon_data(pb_pokemon_data)
        elif data_select == "4":
            get_location_data(pb_pokemon_data)
            get_more_pokemon_data(pb_pokemon_data)
        elif data_select == "5":
            get_moves_info(pb_pokemon_data)
            get_more_pokemon_data(pb_pokemon_data)
        elif data_select == "6":
            get_evolution_chain(pb_pokemon_data)
            get_more_pokemon_data(pb_pokemon_data)
        elif data_select =="7":
            clear_console()
            open_menu()
        else:
            raise ValueError
    except ValueError:
        print("That is not a valid input")
        get_more_pokemon_data(pb_pokemon_data)


def get_location_data(pb_pokemon_data):
    """
    Retrieves location data for selected pokemon
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pb_pokemon_data.id}/encounters")
    location_info = response.json()
    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    #Print location data here and call
    gen_1_versions = ["red", "blue", "yellow" ]
    chars_to_replace = {"-":" ", "area": "", "b1f":"underground", "b2f": "2nd level underground", 
    "b3f": "3rd level undergound", "b4f": "4th level undergound", "1f":"1st level",
     "2f": "2nd level", "3f": "3rd level", "4f": "4th level"}
    print(f"Known locations of {capitalized_pokemon} listed below:\n")
    for x in location_info:        
        location_name = x["location_area"]["name"]
        version_details = x["version_details"]        
        for y in version_details:            
            if y["version"]["name"] in gen_1_versions:             
                for key, value in chars_to_replace.items():
                    location_name = location_name.replace(key, value)
                print(location_name.capitalize())
                break
    print("\n")
    get_more_pokemon_data(pb_pokemon_data)


def get_moves_info(pb_pokemon_data):
    """
    Retrieves the first generation moves the selected pokemon can learn and
    prints them to the console for the user
    """
    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pb_pokemon_data.id}/")
    selected_pokemon_moves = response.json()["moves"]
    print(f"{capitalized_pokemon} can learn the following moves:")
    for x in selected_pokemon_moves:
        move_url = x["move"]["url"]
        move_info = requests.get(move_url).json()
        if move_info["generation"]["name"] == "generation-i":
            version_details = x["version_group_details"]
            for y in version_details:
                print(x["move"]["name"].capitalize())
                break


def get_evolution_chain(pokemon):
    """
    Retrieves evoluton data for selected pokemon
    """
    capitalized_pokemon = str(pokemon).capitalize()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon.id}/")
    pokemon_species = response.json()
    evolution_data = pokemon_species['evolution_chain']['url']
    response_2 = requests.get(evolution_data)
    evolution_tree = response_2.json()["chain"]
    evolves_to = evolution_tree["evolves_to"]

    if evolves_to == []:
        print(f"\n{capitalized_pokemon} has no evolutionary chain.\n")
    elif evolves_to[0]["evolves_to"] ==[]:
        print(f"\n{evolution_tree['species']['name'].capitalize()} evolves into {evolves_to[0]['species']['name'].capitalize()}\n")
    elif len(evolves_to) == 1:
        print(f"\n{evolution_tree['species']['name'].capitalize()} evolves into {evolves_to[0]['species']['name'].capitalize()}")
        print(f"\n{evolves_to[0]['species']['name'].capitalize()} evolves into {evolves_to[0]['evolves_to'][0]['species']['name'].capitalize()}\n")



def show_and_return_pokemon_habitats():
    """
    Prints the searchable habitats for the user to select.
    """
    habitats = requests.get("https://pokeapi.co/api/v2/pokemon-habitat/")
    available_habitats = habitats.json()['results']
    print("In which habitat would you like to search for pokemon?")
    print("\n")
    for x in available_habitats:
        if available_habitats.index(x) == 4:
            print(('{}:{}'.format(available_habitats.index(x)+ 1, "Legendary Locations")))
            continue
        print('{}:{}'.format(available_habitats.index(x)+ 1, x['name'].capitalize()))
    print("\n")
    return available_habitats


def encounter_wild_pokemon():
    """
    Randomly generates pokemon from the habitat the user selects
    """
    available_habitats = show_and_return_pokemon_habitats()
    gen_1_habitat_pokemon = []
    try:
        habitat_id_selected = int(input(""))
        selected_habitat = available_habitats[habitat_id_selected - 1]
    except ValueError:
        print("Not a valid input")
        time.sleep(0.5)
        clear_console()
        encounter_wild_pokemon()
    print("Searching for pokemon...")
    url_for_habitat_species = selected_habitat['url']
    response = requests.get(url_for_habitat_species)
    response_json = response.json()
    pokemon_for_selected_habitat = response_json["pokemon_species"]
    for x in pokemon_for_selected_habitat:
        response_2 = requests.get(x["url"])
        pokemon_within_habitat = response_2.json()
        if pokemon_within_habitat["id"] < 151:
            gen_1_habitat_pokemon.append(pokemon_within_habitat["name"])
    random_habitat_pokemon = random.choice(gen_1_habitat_pokemon)
    pb_pokemon_data = pb.pokemon(random_habitat_pokemon)
    print(f"A wild {random_habitat_pokemon.capitalize()} appeared!")
    print("Checking pokadex...")
    time.sleep(1)
    display_flavour_text(pb_pokemon_data)
    make_wild_pokemon_choice(pb_pokemon_data)


def make_wild_pokemon_choice(pb_pokemon_data):
    """
    User makes the choice to learn more about pokemon, catch pokemon or return to menu
    """
    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    print("What would you like to do next?\n")
    print(f"1. Learn more about {capitalized_pokemon}\n")
    print("2. Throw a pokeball.\n")
    print("3. Run\n")
    try:
        wild_pokemon_choice = input("1, 2 or 3?")
        if wild_pokemon_choice == "1":
            print(f"{capitalized_pokemon} ran while you were checking your pokedex!")
            print("...")
            time.sleep(0.5)
            get_more_pokemon_data(pb_pokemon_data)            
        elif wild_pokemon_choice == "2":
            throw_pokeball(pb_pokemon_data)
            open_menu()
        elif wild_pokemon_choice == "3":
            print(f"Ran from {capitalized_pokemon}")
            time.sleep(0.5)
            open_menu()
        else:
            raise ValueError
    except ValueError:
        print("Not a valid input")


def throw_pokeball(pb_pokemon_data):
    """
    Attempts to 'catch' the encountered pokemon and store
    their name in list of caught pokemon for user
    """
    
    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    print(f"{trainer_name} threw a pokeball!")
    print(".\n..\n...")
    print(f"{capitalized_pokemon} was caught!")
    print(f"Congratulations {trainer_name}. You caught a {capitalized_pokemon}.")
    print(f"{capitalized_pokemon} will be stored with the rest of your pokemon.")
    store_caught_pokemon(pb_pokemon_data)
    


def store_caught_pokemon(pb_pokemon_data):
    """
    Stores 'caught' pokemon in column under trainer_name
    in trainer_data sheet. Also stores associated sprite
    url in sprites_data sheet
    """
    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pb_pokemon_data.id}/")
    sprite_url = response.json()["sprites"]["other"]["official-artwork"]["front_default"]
    trainer_sheet = SHEET.worksheet('trainer_data')
    sprites_sheet = SHEET.worksheet("sprites_data")
    trainers_list = trainer_sheet.row_values(1)
    i = trainers_list.index(trainer_name)
    for j in range(2,200):
        if trainer_sheet.cell(j, i+1).value == None:
            trainer_sheet.update_cell(j, i+1, capitalized_pokemon)
            sprites_sheet.update_cell(j, i+1, sprite_url)
            break
    

def return_trainer_col():
    """
    Returns dedicated column of user in trainer_data worksheet
    """
    trainer_sheet = SHEET.worksheet('trainer_data')
    trainers_list = trainer_sheet.row_values(1)
    trainer_col = trainers_list.index(trainer_name.lower())
    return trainer_col


def return_caught_pokemon():
    """
    Returns list of pokemon 'caught' by the user
    """
    trainer_sheet = SHEET.worksheet('trainer_data')
    i = return_trainer_col()
    caught_pokemon = trainer_sheet.col_values(i+1)
    return caught_pokemon


def view_caught_pokemon():
    """
    Prints out the pokemon the user has 'caught' previously
    """
    caught_pokemon = return_caught_pokemon()
    if len(caught_pokemon) == 1:
        print("You have not caught any pokemon yet.\n")
        print("Returning to menu. Select (3) to catch a pokemon")
        open_menu()
    else:
        print("Please see your pokemon below:")
        for x in range(len(caught_pokemon)):
            if x == 0:
                continue
            print(f"{x}: {caught_pokemon[x]}")
    print("\n")
    print("If you would like to view any of your pokemon, please enter the number next to their name.")
    print("Otherwise, enter '0' to return to the main menu")
    return_or_get_sprite_url()
    

def return_or_get_sprite_url():
    """
    Prints out a url for user to paste into browser to
    view an image of selected 'caught' pokemon
    """
    trainer_sheet = SHEET.worksheet('trainer_data')
    sprites_sheet = SHEET.worksheet("sprites_data")
    i = return_trainer_col()
    caught_pokemon = trainer_sheet.col_values(i+1)
    view_pokemon_choice = input("")
    try:        
        if int(view_pokemon_choice) == 0:
            open_menu()
        elif int(view_pokemon_choice) in range(1,len(caught_pokemon)):
            print("Paste the below url into your browswer to see you pokemon:\n")
            print(sprites_sheet.cell(int(view_pokemon_choice)+1,i+1).value)
            print("\n")
            print("If you would like to another one of your pokemon, please enter the number next to their name.")
            print("Otherwise, enter '0' to return to the main menu")
            print("\n")
            return_or_get_sprite_url()
        else:
            raise ValueError
    except ValueError:
        print("Invalid input")
        print("If you would like to view any of your pokemon, please enter the number next to their name.")
        print("Otherwise, enter '0' to return to the main menu")
        return_or_get_sprite_url()





def main():
    """
    Main function initiates app.
    """
    global gen_resource
    global trainer_name
    gen_resource = pb.generation(GENERATION)
    trainer_name = enter_trainer_name()
    run_landing_page()
    
    
    
main()
