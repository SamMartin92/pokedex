google sheet which shows what pokemon have been caught. enter your trainer name, and then saves in a row on a google sheet

text art pokeball:
https://www.ascii-art-generator.org/

pokedex:
https://patorjk.com/software/taag/#p=testall&h=3&f=Doh&t=P%20O%20K%20E%20D%20E%20X

where i got clear console:
https://appdividend.com/2022/01/29/how-to-clear-console-in-python/#:~:text=To%20clear%20the%20console%20in,system()%20method.



def find_pokemon():
    """
    Allows user to key in name or id of pokemon and 
    seek out information about it
    """
    print("""Please enter the name or id (1-150) of the pokemon you wish to search for\n""")

    try:
        select_pokemon = input("")
        possible_ids = [poke.id for poke in gen_resource.pokemon_species]
        gen_1_pokemon = [pokemon.name.title() for pokemon in gen_resource.pokemon_species]
         
        if select_pokemon.capitalize() in gen_1_pokemon:
            pokemon_name = pb.pokemon(select_pokemon.lower())
            print(f"You have chosen {pokemon_name}")
            print("\n")
            print(f"{pokemon_name} is number {pokemon_name.id}")
        
        elif int(select_pokemon) in possible_ids:
            pokemon_name = pb.pokemon(int(select_pokemon)).name.title()
            print(f"Pokemon number {select_pokemon} is {pokemon_name}")
            
        else:
            print("Not a valid entry.")
            find_pokemon()

    except ValueError:
            print("Not a valid entry.")
            find_pokemon()

    return pokemon_name





    if 
        pokemon_name = pb.pokemon(int(select_pokemon)).name.title()
        print(f"Pokemon number {select_pokemon} is {pokemon_name}")




>>> for x in eevee_moves:
...     move_url = x["move"]["url"]
...     move_info = requests.get(move_url).json()
...     if move_info["generation"]["name"] == "generation-i":
...             version_details = x["version_group_details"]
...             for y in version_details:
...                     print('{}: {}'.format(y["level_learned_at"],x["move"]["name"]))
... 