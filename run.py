"""
Imported libraries
"""

import time
import random
from os import system, name
import pokebase as pb
import requests
import gspread
from google.oauth2.service_account import Credentials
from models import Trainer, Pokemon, session

# Constant variables
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

pokemon_generation_data = None
trainer_name = None


# https://www.geeksforgeeks.org/clear-screen-python/
def clear_console():
    """
    Clears all data from terminal when called
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def delay_clear():
    """
    Shows user screen for .75 seconds before clearing console
    """
    time.sleep(.75)
    clear_console()


def enter_trainer_name():
    """
    Takes users trainer name to link to any data from previous uses of the app.
    Adds it to linked google sheet if it has not been addded previously.
    """
    i=0
    trainer_sheet = SHEET.worksheet('trainer_data')
    trainers_list = trainer_sheet.row_values(1)
    sprites_sheet = SHEET.worksheet("sprites_data")
    existing_trainers = session.query(Trainer.name).all()
    existing_trainer_names = [trainer[i] for trainer in existing_trainers]
    print("Hello trainer. Please enter your name:\n")
    try:
        trainer_name = input("")

        if len(trainer_name) == 0:
            raise ValueError("Name cannot be empty")
        # if trainer_name.lower() in trainers_list:
        if trainer_name in existing_trainer_names:
            print(f"Welcome back {trainer_name}")
        
        else:
            print(f"Welcome {trainer_name}")
            new_trainer = Trainer(name=trainer_name)
            session.add(new_trainer)
            session.commit()
            index_to_update = len(trainers_list) + 1
            trainer_sheet.update_cell(1, index_to_update, trainer_name.lower())
            sprites_sheet.update_cell(1, index_to_update, trainer_name.lower())
        time.sleep(1)
        return trainer_name
    except ValueError as e:
        print(e)
        return enter_trainer_name()


def run_landing_page():
    clear_console()

    print("""
         _____     ____    _  __  ______   _____    ______  __   __
        |  __ \\   / __ \\  | |/ / |  ____| |  __ \\  |  ____| \\ \\ / /
        | |__) | | |  | | | ' /  | |__    | |  | | | |__     \\ V /
        |  ___/  | |  | | |  <   |  __|   | |  | | |  __|     > <
        | |      | |__| | | . \\  | |____  | |__| | | |____   / . \\
        |_|       \\____/  |_|\\_\\ |______| |_____/  |______| /_/ \\_\\
        """.center(80))

    print('''
                         ...'',,,,,,,,,'...
                     ..',;;;;;;;;;;;;;;;;;;,'..
                   .';;;;;;;;;;;;;;;;;;;;;;;;;,'.
                 .,;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,'.
               .';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,'.
              .,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,.
             .,;;;;;;;;;;;;;;,'......',;;;;;;;;;;;,,,,.
            .';;;;;;;;;;;;;'.          .';;;;;;;;;,,,,'.
            .;;;;;;;;;;;;,.   ,ldxxdl,   .,;;;;;;;;,,,,.
            .;;;;;;;;;;;;.  .dNMMMMMMNd.  .;;;;;;;;.....
                            :NMMMMMMMMN:
           .;::::::::::::.  ,KMMMMMMMMK,  .;:::::::;;;;'
           '0MMMMMMMMMMMWk.  ,xKNWWNKx,  .kWMMMMMMNXXXXd.
           .dWMMMMMMMMMMMWO;.  .',,'.  .;OWMMMMMMMNXXX0;
            'OMMMMMMMMMMMMMNOo;'....';oONMMMMMMMMWNXXKo.
             ,0MMMMMMMMMMMMMMMWNXXXXNWMMMMMMMMMMWNXXXd.
              ,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXKo.
               .oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXk;
                 'dXWMMMMMMMMMMMMMMMMMMMMMMMMWNXkc.
                   .lOXWMMMMMMMMMMMMMMMMMMMWN0o;.
                      ':dOKNWMMMMMMMMMMWX0xl,.
                          .';cllooooll:;..



        '''.center(80))
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
        selected_menu_choice = int(input(""))
        if selected_menu_choice == 1:
            delay_clear()
            open_description()

        elif selected_menu_choice == 2:
            delay_clear()
            find_pokemon()

        elif selected_menu_choice == 3:
            delay_clear()
            encounter_wild_pokemon()

        elif selected_menu_choice == 4:
            delay_clear()
            view_caught_pokemon()
        else:
            raise ValueError
    except ValueError:
        print("Not a valid input. Please type '1', '2', '3' or '4' to make",
              "your selection")
        make_menu_choice()


def open_description():
    """
    Gives the user a description of the application
    """
    clear_console()
    print("""
    Welcome to your Pokedex.

    The Pokedex is a tool based around the first generation of Pokemon. ie
    the first 150 pokemon.
    Connecting to 'PokeAPI', your Pokedex will give you all the information
    you need to find the first generation of pokemon.

    Search for pokemon by name or ID with menu option (2).
    Retrieve information such as known locations, evolutionary chains,
    what moves they can learn and more.

    With your pokedex, you can also encounter and catch wild pokemon with
    menu option (3). Choose a habitat to search and come across a random
    pokemon which can be found there.If you like the pokemon you encounter,
    throw a pokeball and add them to your collection.

    Once you have caught some pokemon, you can view your collection with menu
    option (4). Check out what pokemon you've caught so far and generate a
    url to check them out in your browser.

    With your pokedex in hand, there is nothing stopping you on your journey
    to becoming a pokemon master. Gotta catch 'em all!
        """)
    menu_return = input("Press enter to return to the main menu")
    if menu_return is None:
        clear_console()
        open_menu()
    else:
        clear_console()
        open_menu()


def find_pokemon():
    """
    Allows user to key in name or id of pokemon and
    seek out information about it
    """
    i=0
    print("Please enter the name or id (1-150) of the pokemon you wish to",
          "search for:")
    try:
        selected_pokemon_id_or_name = input("")
        pokemon_names = [pokemon[i] for pokemon in session.query(Pokemon.name).all()]
        # Name search
        if selected_pokemon_id_or_name.lower() in pokemon_names:
            pb_pokemon_data = session.query(Pokemon).filter_by(name=selected_pokemon_id_or_name.lower()).first()
            delay_clear()
            display_pokemon(pb_pokemon_data)
        # Id search
        elif int(selected_pokemon_id_or_name) in range(1, 151):
            pb_pokemon_data = session.query(Pokemon).filter_by(id=int(selected_pokemon_id_or_name)).first()
            delay_clear()
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
    name = pb_pokemon_data.name
    print(f"Pokemon number {pb_pokemon_data.id}: {name.capitalize()}")
    print(f"Some information about {name.capitalize()}:\n")
    print(pb_pokemon_data.description1)
    print("\n")
    print(pb_pokemon_data.description2)
    print("\n")


def get_more_pokemon_data(pb_pokemon_data):
    """
    Allows user to select the data they wish to see about chosen pokemon
    """
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{pb_pokemon_data.id}/")
    pokemon_api_response = response.json()
    name = pb_pokemon_data.name
    print(f"What do you want to know about {name.capitalize()}?")
    print("Input 1 for type")
    print("Input 2 for height")
    print("Input 3 for weight")
    print("In put 4 for locations")
    print("Input 5 for moves info")
    print("Input 6 for evolution chain")
    try:
        data_select = input("Input 7 to return to main menu     ")
        if data_select == "1":
            delay_clear()
            print(f"\n{name.capitalize()} has the following type(s):")
            print(f"1. {pb_pokemon_data.type1.capitalize()}")
            if pb_pokemon_data.type2 is not None:
                print(f"2. {pb_pokemon_data.type2.capitalize()}")
                print("\n")
        elif data_select == "2":
            delay_clear()
            print(f"\n{name.capitalize()} is {pb_pokemon_data.height}",
                  "decimetres in height.\n")
        elif data_select == "3":
            delay_clear()
            print(f"\n{name.capitalize()} is {pb_pokemon_data.weight}",
                  "hectograms in weight.\n")
        elif data_select == "4":
            delay_clear()
            get_location_data(pb_pokemon_data)
        elif data_select == "5":
            delay_clear()
            get_moves_info(pb_pokemon_data)
        elif data_select == "6":
            delay_clear()
            get_evolution_chain(pb_pokemon_data)
        elif data_select == "7":
            clear_console()
            open_menu()
        else:
            raise ValueError

        if data_select != '7':
            get_more_pokemon_data(pb_pokemon_data)

    except ValueError:
        delay_clear()
        print("That is not a valid input")
        get_more_pokemon_data(pb_pokemon_data)


def get_location_data(pb_pokemon_data):
    """
    Retrieves location data for selected pokemon
    """
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pb_pokemon_data.id}/encounters")
    location_info = response.json()
    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    # Print location data here and call
    gen_1_versions = ["red", "blue", "yellow"]
    chars_to_replace = {"-": " ", "area": "",
                        "b1f": "underground",
                        "b2f": "2nd level underground",
                        "b3f": "3rd level undergound",
                        "b4f": "4th level undergound",
                        "1f": "1st level",
                        "2f": "2nd level",
                        "3f": "3rd level",
                        "4f": "4th level",
                        "5f": "5th level",
                        "6f": "6th level",
                        "7f": "7th level"}
    if len(location_info) == 0:
        print("No locations found")
    else:
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
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pb_pokemon_data.id}/")
    selected_pokemon_moves = response.json()["moves"]
    print(f"Retrieving moves for {capitalized_pokemon}...")
    moves_learned = []
    for x in selected_pokemon_moves:
        move_url = x["move"]["url"]
        move_info = requests.get(move_url).json()
        if move_info["generation"]["name"] == "generation-i":
            version_details = x["version_group_details"]
            for y in version_details:
                if y["move_learn_method"]["name"] != "level-up":
                    moves_learned.append(x["move"]["name"].capitalize())
                    break
    print(f"{capitalized_pokemon} can learn the following moves:\n")
    print(', '.join(moves_learned))
    print("\n")


def get_evolution_chain(pb_pokemon_data):
    """
    Retrieves evoluton data for selected pokemon
    """
    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{pb_pokemon_data.id}/")
    pokemon_species = response.json()
    evolution_data = pokemon_species['evolution_chain']['url']
    response_2 = requests.get(evolution_data)
    evolution_tree = response_2.json()["chain"]
    evol_to = evolution_tree["evolves_to"]

    if evol_to == []:
        print(f"\n{capitalized_pokemon} has no evolutionary chain.\n")
    elif evol_to[0]["evolves_to"] == []:
        print(f"\n{evolution_tree['species']['name'].capitalize()} evolves",
              f"into {evol_to[0]['species']['name'].capitalize()}\n")
    elif len(evol_to) == 1:
        print(f"\n{evolution_tree['species']['name'].capitalize()} evolves "
              f"into {evol_to[0]['species']['name'].capitalize()}\n")
        print(
            f"{evol_to[0]['species']['name'].capitalize()} evolves into "
            f"{evol_to[0]['evolves_to'][0]['species']['name'].capitalize()}\n")


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
            print(('{}:{}'.format(available_habitats.index(x) + 1,
                  "Legendary Locations")))
            continue
        print('{}:{}'.format(available_habitats.index(x) + 1,
                             x['name'].capitalize()))
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
        if habitat_id_selected in range(1, 10):
            selected_habitat = available_habitats[habitat_id_selected - 1]
        else:
            raise ValueError
    except ValueError:
        print("Not a valid input")
        time.sleep(0.5)
        clear_console()
        encounter_wild_pokemon()
    delay_clear()
    print("Searching for pokemon...")
    url_for_habitat_species = selected_habitat['url']
    response = requests.get(url_for_habitat_species)
    response_json = response.json()
    pokemon_for_selected_habitat = response_json["pokemon_species"]
    for x in pokemon_for_selected_habitat:
        response_2 = requests.get(x["url"])
        pokemon_within_habitat = response_2.json()
        # Show only first generation pokemon
        if pokemon_within_habitat["id"] < 151:
            gen_1_habitat_pokemon.append(pokemon_within_habitat["name"])
    random_habitat_pokemon = random.choice(gen_1_habitat_pokemon)
    pb_pokemon_data = pb.pokemon(random_habitat_pokemon)
    clear_console()
    print(f"A wild {random_habitat_pokemon.capitalize()} appeared!")
    print("Checking pokadex...")
    time.sleep(2.5)
    clear_console()
    display_flavour_text(pb_pokemon_data)
    make_wild_pokemon_choice(pb_pokemon_data)


def make_wild_pokemon_choice(pb_pokemon_data):
    """
    User makes the choice to learn more about pokemon,
    catch pokemon or return to menu
    """
    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    print("What would you like to do next?\n")
    print(f"-(1)- Learn more about {capitalized_pokemon}")
    print("-(2)- Throw a pokeball.")
    print("-(3)- Run")
    try:
        wild_pokemon_choice = input("")
        if wild_pokemon_choice == "1":
            delay_clear()
            print(f"{capitalized_pokemon} fled while you were",
                  "checking your pokedex!")
            print("...")
            time.sleep(0.75)
            get_more_pokemon_data(pb_pokemon_data)
        elif wild_pokemon_choice == "2":
            delay_clear()
            throw_pokeball(pb_pokemon_data)
            open_menu()
        elif wild_pokemon_choice == "3":
            delay_clear()
            print(f"Got away from {capitalized_pokemon}")
            time.sleep(0.5)
            open_menu()
        else:
            raise ValueError
    except ValueError:
        print("Not a valid input")
        delay_clear()
        display_flavour_text(pb_pokemon_data)
        make_wild_pokemon_choice(pb_pokemon_data)


def throw_pokeball(pb_pokemon_data):
    """
    Attempts to 'catch' the encountered pokemon and store
    their name in list of users 'caught' pokemon.
    """

    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    print(f"{trainer_name} threw a pokeball at {capitalized_pokemon}!")
    print(".\n..\n...")
    print(f"{capitalized_pokemon} was caught!")
    print(f"Congratulations {trainer_name}.",
          f"You caught a {capitalized_pokemon}.")
    print(f"{capitalized_pokemon} will be stored with the rest",
          "of your pokemon.")
    store_caught_pokemon(pb_pokemon_data)


def store_caught_pokemon(pb_pokemon_data):
    """
    Stores 'caught' pokemon in column under trainer_name
    in trainer_data sheet. Also stores associated sprite
    url in sprites_data sheet
    """
    capitalized_pokemon = str(pb_pokemon_data).capitalize()
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pb_pokemon_data.id}/")
    sprite_url = response.json(
    )["sprites"]["other"]["official-artwork"]["front_default"]
    trainer_sheet = SHEET.worksheet('trainer_data')
    sprites_sheet = SHEET.worksheet("sprites_data")

    col_idx = return_trainer_col_index()
    caught_pokemon_list_by_trainer = return_caught_pokemon_by_trainer()
    row_idx = len(caught_pokemon_list_by_trainer) + 1
    trainer_sheet.update_cell(row_idx, col_idx + 1, capitalized_pokemon)
    sprites_sheet.update_cell(row_idx, col_idx + 1, sprite_url)


def return_trainer_col_index():
    """
    Returns dedicated column of user in trainer_data worksheet
    """
    trainer_sheet = SHEET.worksheet('trainer_data')
    trainers_list = trainer_sheet.row_values(1)
    trainer_col = trainers_list.index(trainer_name.lower())
    return trainer_col


def return_caught_pokemon_by_trainer():
    """
    Returns list of pokemon 'caught' by the user
    """
    trainer_sheet = SHEET.worksheet('trainer_data')
    i = return_trainer_col_index()
    caught_pokemon = trainer_sheet.col_values(i + 1)
    return caught_pokemon


def view_caught_pokemon():
    """
    Prints out the pokemon the user has 'caught' previously
    """
    caught_pokemon = return_caught_pokemon_by_trainer()
    if len(caught_pokemon) == 1:
        print("You have not caught any pokemon yet.\n")
        print("Returning to menu. Select (3) to catch a pokemon")
        open_menu()
    else:
        print("Please see your pokemon below:")
        for x in range(len(caught_pokemon)):
            if x > 0:
                print(f"{x}: {caught_pokemon[x]}")
    return_or_get_sprite_url()


def return_or_get_sprite_url():
    """
    Prints out a url for user to paste into browser to
    view an image of selected 'caught' pokemon
    """
    trainer_sheet = SHEET.worksheet('trainer_data')
    sprites_sheet = SHEET.worksheet("sprites_data")
    i = return_trainer_col_index()
    caught_pokemon = trainer_sheet.col_values(i + 1)
    print("\nIf you would like to view any of your pokemon,",
          "please enter the number next to  their name.")
    print("Otherwise, enter '0' to return to the main menu")
    view_pokemon_choice = input("")
    try:
        if int(view_pokemon_choice) == 0:
            delay_clear()
            open_menu()
        elif int(view_pokemon_choice) in range(1, len(caught_pokemon)):
            delay_clear()
            print("Paste the below url into your browswer to",
                  "see your pokemon:")
            print("Be careful not to use ctrl + C to copy",
                  "or you will exit the program.\n")
            print(
                sprites_sheet.cell(
                    int(view_pokemon_choice) + 1,
                    i + 1).value)
            print("\n")
            view_caught_pokemon()
            return_or_get_sprite_url()
        else:
            raise ValueError
    except ValueError:
        print("\nInvalid input")
        delay_clear()
        view_caught_pokemon()
        print("\n")
        return_or_get_sprite_url()


def main():
    """
    Main function initiates app.
    """
    global pokemon_generation_data
    global trainer_name
    pokemon_generation_data = pb.generation(GENERATION)
    trainer_name = enter_trainer_name()
    run_landing_page()


main()
