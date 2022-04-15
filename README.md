# Pokedex

![Multi Device Mockup](lin)

[Link to live Site](https://pokedex-pp3.herokuapp.com/)

Pokedex is a pyhton based web application run in a mock terminal. Based on the popular kids television series, Pokémon, Pokedex attempts replicate  in some regards, the Pokédex, a tool used by trainers in the television and video game series. In the show, this device is used to capture and provide information to the characters about the pokemon they encounter. This python pokedex offers similar functionality, through calls to [PokeAPI](https://pokeapi.co/), an API with a comprehensive database detailing everything from the main game series. 

This python Pokedex allows the user to fund information about the first generation of the pokémon series. The first generation comprises of the first 150 pokémon introduced and information linked to the first release of Pókemon games for the Nintendo Gameboy ([Pokémon Red, Blue](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Red_and_Blue) & [Yellow](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Yellow). The reason for limiting the information provided in this pokedex is that the large number of games and generations released since the first generation back in the 1990s means the number of results returned from API calls would have made for an overwhelming user experience, but also, as a child of the 90s, it is a point of personal preference.

Beyond, finding information about the first generation of Pokémon, users can encounter 'wild' pokémon and catch them, mimicing the games the tv series, and view their collection of pokemon whenever they decide to return to the application.

## User Experience:

* ## Vision:
 The idea and aim of the pokedex is to create a fun and informative web application from which users can find some basic information about the frst generation of pokemon. Whether a user is just curious for certain fundamental information about a pokemon, or is new to pokemon and wants to see some general info, pokedex aims to act as encyclopedia of sorts which pulls out information quickly and easily for the user. There should be no prerequisate knowledge required on the user's end. Users who simply want to learn something new should be able to extract info through their inputs, even if it involves and element of randomness on their part.
 
 In addition to this, the app aims to play to the idea which drove the pokémon series and games in the first place: catching and collecting pokémon. The app should allow the user to play the role of trainer and seek out and 'catch' their favourite pokemon, to be viewed at any stage when they return to the application.
 
 * ## Target Audience:
  Centering the app around the first generation of the series, the supposed target audience would be any user who, like myself, has an affiliation with the series from childhood, or perhaps recent times. However, this app is also aimed more widely at anyone curious about pokémon or anyone familiar with the Gameboy games. This application offers a stripped back version of some of the facets of the original games without the need to spend time progressing through an entire video game.
 
 * ## User stories:
  As a user:
  1. I want to easily understand the purpose of the application and to navigate easily to all relevant sections.
  2. I want to find the desired information abdout specific pokemon quickly and simply.
  3. I want to collect my favourite pokemon and view those which I have caught.
  4. Who is a new fan of the series, I want to simulate some aspects of the life of a pokémon trainer as seen in the games and tv series.
  5. Who grew up watching Pokémon, I want to feel a sense of nostalgia recalling a pleasant childhood memory.
  
  As a returning user:
  1. I want my previous use of the app to be saved and reflected when viewing the pokemon I have caught in the past.
  2. I want to see if there are new features added to the application.
 
  As a site owner:
  1. I want to provide an easy, enjoyable and reactive experience for the user.
  2. I want a way to monitor and save past usage of users.
  3. I want to provide a real world simulation of the Pokédex tool used in the games and tv series.
 
 * ## UX Plane:
1. ### Strategy:
  * Build a python based web app which runs through a mock terminal for fans, or those curious, of Pokémon.
  * Make a simple application with straight-forward features to educate the user about the world of Pokémon.
2. ## Scope:
  * Build the application on a single page site and have it run in a mock terminal.
  * Build an application with no learning curve or prior knowledge required.
  * Design a application which intuitively allows the user to access the feature without any difficulty.
  * Design a visually pleasing application which provides feedback to the user and handles all input errors.
3. ## Structure:
  * Buld the entire app in one terminal.
  * Build an application which flows from one feature to the next and allows the user to loop back to the main menu without the need to restart the application.
  * Make menu and input options clear and consistent throughout each section of the application.
 4. ## Skeleton:
  * This application will flow from section to section based on user input.
  * Before proceeding with coding this site, I made a simple flow chart to represent the journeys users could take. This would be developed further while building the    application.
    1. Initial flow chart:
      ![Initial Chart](assets/images/readme/flow-charts/initial-flow-chart.png)
    2. Further developed during build:
5. ##Surface:
  * This application should provide basic menus with straight forward options for user input.
  * Should provide feedback to the user where API calls cause slight delays in returning information to the terminal.

* ## Features:
  * ### Existing features:
   1. #### Enter trainer name:
    On running the application, the user is first asked to input their 'trainer name'. This acts as a username for the app. The user is then welcomed to the application and if they have used it previously, is welcomed back.
    ![Enter trainer name](assets/images/readme/features/enter-trainer-name.PNG)
    The trainer's name is stored in the app-associated google sheet, in the top row of each worksheet in order to store actions of the user, so they can be accessed for future uses.
    ![Trainer sheet](assets/images/readme/features/sheet-trainer-names.PNG)
   2. #### Landing image:
    After the user has entered their trainer name, the landing image displays for 2 seconds displaying the name of the application and a stylyised image of a Pokéball from the series.
   3. #### Main menu:
    The main menu then displays which displays the various sections within the app and allows the user to input and decide which action they want to take.
    ![Main menu](assets/images/readme/features/main-menu.PNG)
   4. #### About Pokedex:
    Option (1) in the menu opens the 'About Pokedex' section. This simply gives a description of the application and can be the first port of call for a new user, to understand the purpose of the application if it is not immediately apparent to them.
    ![About Pokedex](assets/images/readme/features/description.PNG)
    5. #### Search pokemon:
    This feature allows a user to search for information on a desired pokemon by entering its name or ID. If a user does not have any prior knowledge, the prompt in the input text to input a number from 1-150 will allow them to easily bring up a pokemon and display its info depending on what random number they choose.
    ![Search pokemon input](assets/images/readme/features/search-pokemon-user-input.PNG)
    Once a name or ID has been selected, two samples of 'flavour text' are dsplayed which are bite-sized pieces of information on the selected pokemon. These are taken from the original Gameboy game. When a pokemon was caught and could be viewed in he pokédex within the game, these pieces of text were displayed along with the pokémon's stats.
    Below this, another menu displays which asks the user what information they would like to get about the selected pokemon. The user can input based on the number listed next to the option or input 7 to return to the main menu.
    ![Search pokemon output](assets/images/readme/features/search-pokemon-output.PNG)
    6. #### Catch pokemon:
      This feature allows the user to 'encounter' a 'wild' pokemon, randomly generated from the selected habitat. 
      ![Catch pokemon input](assets/images/readme/features/catch-pokemon-input.PNG)
      Users can look up information about the randomly encountered pokemon or choose to 'catch' it. If the pokemon is caught, it is stored in the associated google sheet under their trainer name so that it can be accessed for future reference. This is how a user can collect a roster of their own pókemon within the app.
      ![Select habitat output](assets/images/readme/features/selected-habitat-output.PNG)
      A menu gives the user three options:
      1. They can learn more about the pokemon. This runs the same function and generates the same menu as if the pokémon had been searched for with option (2) in the main menu. The user will see that the pokemon is no longer available to catch through a message advising them the pokemon fled.
      ![Learn more](assets/images/readme/features/catch-pokemon-learn-more.PNG)
      2. Describing the 3rd option next, users can simply 'Run' from the pokémon. This is a similar option as to one which is offered to users of the game series if they encounter a wild pokémon. This simply displays a message to the user and brings them back to the main menu.
      ![Run from pokemon](assets/images/readme/features/run-from-pokemon.PNG)
      3. The second option for users is to 'throw a pokéball' and 'catch' the encountered pokémon. This again mimics the game series in how it displays a message to the user congratulating them on catching the wild pokemon.
      ![Throw pokéball](assets/images/readme/features/throw-pokeball.PNG)
      As mentioned above, if the user decides to catch the pokémon, it is stored below their trainer name in the associated google sheet so that it can be viewed and accessed in the future.
      ![Caught pokémon in Google sheet](assets/images/readme/features/google-sheet-caught-pokemon.PNG)
    7. ####  View caught pokémon:
    Lastly, with this feature, users can see their roster of previously caught pokemon, taken fromt he data stored in the associated google sheet. The caught pokemon displays as a numbered list, this will act as a guide for the user input option which follows this display.
    ![View caught pokemon](assets/images/readme/features/view-caught-pokemon.PNG)
    The final option open to users of the app is to generate a url to see what their pokemon looks like. Within the PokéAPI, there are what is known as 'sprite images' that can be accessed. These are images from various verisons of the games and official artwork of the pokémon. Upon inputting the number next to the desired pokémon, a url is provided to paste into browser along with a warning not to use the Ctrl + C shortcut to copy as this will exit out of the program.
    ![Generate sprite url](assets/images/readme/features/get-sprite-info.PNG)
    This url is generated from a seperate worksheet named sprite-data, which updates the coinciding cell, which is updated with the pokémon name when it is caught.
    ![Sprite data sheet](assets/images/readme/features/sheet-sprite-data.PNG)
    
    
   
    
 
























google sheet which shows what pokemon have been caught. enter your trainer name, and then saves in a row on a google sheet

text art pokeball:
https://www.ascii-art-generator.org/

pokedex:
https://patorjk.com/software/taag/#p=testall&h=3&f=Doh&t=P%20O%20K%20E%20D%20E%20X

where i got clear console:
https://appdividend.com/2022/01/29/how-to-clear-console-in-python/#:~:text=To%20clear%20the%20console%20in,system()%20method.

https://pokebase.readthedocs.io/en/latest/examples/index.html

favicon: https://www.favicon.cc/?action=icon&file_id=875676
