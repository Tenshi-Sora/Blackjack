deck_of_cards = ('A', '2', '3', '4', '5',
                 '6', '7', '8', '9', 'J', 'Q', 'K')
dealers_deck = []
dealers_hand = []
player1s_hand = []
player1s_split_hand = []
player2s_hand = []
player2s_split_hand = []
player3s_hand = []
player3s_split_hand = []
player4s_hand = []
player4s_split_hand = []
player5s_hand = []
player5s_split_hand = []
player6s_hand = []
player6s_split_hand = []
player7s_hand = []
player7s_split_hand = []

print('\n \n ----------Start---------- \n \n')

# rules: https://www.beatblackjack.org/rules/#:~:text=Blackjack%20is%20played%20with%201,11%2C%20as%20the%20holders%20desires.&text=A%20Blackjack%20(Ace%20and%20a,all%20other%20combination%20of%20cards.

ready = False
game_round = 0


def toggle_amount_of_players():  # Option 2
    '''
    Prompts how many players are playing
    '''
    while True:
        player_input = input('''
        How many players are playing? [1-7]

        Players: ''')
        if (player_input := int(player_input)) in (1, 2, 3, 4, 5, 6, 7):
            return player_input
        print('That was not a valid input, please try again.')


players = 1


def toggle_amount_of_decks():  # Option 3
    '''
    Prompts how many decks the player would like to play with
    '''
    while True:
        player_input = input('''
        With how many decks would you like to play with?
        ----------------------------
        1 = 52 cards (clasic mode)
        2 = 104 cards
        3 = 156 cards
        4 = 208 cards
        5 = 260 cards
        6 = 312 cards
        7 = 364 cards
        8 = 416 cards
        9 = 468 cards (casino mode)
        ----------------------------

        Amount of decks: ''')
        if (player_input := int(player_input)) in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            return player_input
        print('That was not a valid input, please try again.')


decks = 1


def toggle_amount_of_rounds():  # Option 4
    '''
    Prompts how many rounds the player would like to play
    '''
    while True:
        player_input = input('''
        How many rounds would you like to play?
        Type 0 for endless mode or any number for
        that amount of rounds.

        Rounds: ''')
        if (player_input := int(player_input)) > 0:
            return player_input
        elif player_input == 0:
            return player_input
        print('That was not a valid input, please try again.')


targeted_round = 1
current_round = 0


def toggle_gamble_mode():  # Option 5
    '''
    Prompts if the player would like to turn gamble mode on or off and returns True or False
    '''
    while True:
        player_input = input('''
        Would you like to turn gamble mode on or off?
        
        [On/Off]: ''')
        if player_input.casefold().strip() == 'on':
            return True
        elif player_input.casefold().strip() == 'off':
            return False
        else:
            print('That was not a valid input, please try again.')


gamble_mode = False


def toggle_assist_mode():  # Option 6
    '''
    Prompts if the player would like to turn assist mode on or off and returns True or False
    '''
    while True:
        player_input = input('''
        Would you like to turn assist mode off?
        
        [On/Off]: ''')
        if player_input.casefold().strip() == 'on':
            return True
        elif player_input.casefold().strip() == 'off':
            return False
        else:
            print('That was not a valid input, please try again.')


assist_mode = False


def toggle_gamble_start_value():  # Toggles after the game starts
    while True:
        print(
            f'Curent starting cash is ${gamble_start_value}, would you like to change it?')
        player_input = input('[Y/N]')
        if (player_input.casefold().strip()) == 'y':
            print('How much would you like to start with?')
            player_input = input('Start value: ')
            if str.isdecimal(player_input) and (player_input := int(player_input)):
                print(f'Starting value set to {player_input}.')
                return player_input
        elif player_input == 'n':
            return 100
        else:
            print('That was not a valid input, please try again.')


gamble_start_value = 100


def check_player_input():
    while True:
        if (player_input := player_input.casefold().strip()) in ('a', '2', '3', '4', '5', '6', '7', '8', '9', 'j', 'q', 'k', 'h', 'q'):
            if player_input == 'a':
                return 'a'
            elif player_input == '2':
                return '2'
            elif player_input == '3':
                return '3'
            elif player_input == '4':
                return '4'
            elif player_input == '5':
                return '5'
            elif player_input == '6':
                return '6'
            elif player_input == '7':
                return '7'
            elif player_input == '8':
                return '8'
            elif player_input == '9':
                return '9'
            elif player_input == 'j':
                return 'j'
            elif player_input == 'q':
                return 'q'
            elif player_input == 'k':
                return 'k'
            elif player_input == 'h':
                pass  # returns help
            else:
                quit()
        else:
            print('That was not a valid input, please try again.')
            player_input = input('')


print('''
 /$$      /$$           /$$                                           /$$                                 
| $$  /$ | $$          | $$                                          | $$                                 
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$        /$$$$$$    /$$$$$$                    
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$      |_  $$_/   /$$__  $$                   
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$        | $$    | $$  \ $$                   
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$        | $$ /$$| $$  | $$                   
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$        |  $$$$/|  $$$$$$/                   
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/         \___/   \______/                    
                                                                                                          
                                                                                                          
                                                                                                          
 /$$$$$$$$                            /$$       /$$        /$$$$$$                              /$$       
|__  $$__/                           | $$      |__/       /$$__  $$                            | $/       
   | $$  /$$$$$$  /$$$$$$$   /$$$$$$$| $$$$$$$  /$$      | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$|_//$$$$$$$
   | $$ /$$__  $$| $$__  $$ /$$_____/| $$__  $$| $$      |  $$$$$$  /$$__  $$ /$$__  $$|____  $$ /$$_____/
   | $$| $$$$$$$$| $$  \ $$|  $$$$$$ | $$  \ $$| $$       \____  $$| $$  \ $$| $$  \__/ /$$$$$$$|  $$$$$$ 
   | $$| $$_____/| $$  | $$ \____  $$| $$  | $$| $$       /$$  \ $$| $$  | $$| $$      /$$__  $$ \____  $$
   | $$|  $$$$$$$| $$  | $$ /$$$$$$$/| $$  | $$| $$      |  $$$$$$/|  $$$$$$/| $$     |  $$$$$$$ /$$$$$$$/
   |__/ \_______/|__/  |__/|_______/ |__/  |__/|__/       \______/  \______/ |__/      \_______/|_______/ 
                                                                                                          
                                                                                                          
                                                                                                          
 /$$$$$$$  /$$                     /$$                               /$$                                  
| $$__  $$| $$                    | $$                              | $$                                  
| $$  \ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$  /$$$$$$   /$$$$$$$| $$   /$$                            
| $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/|__/ |____  $$ /$$_____/| $$  /$$/                            
| $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  /$$$$$$$| $$      | $$$$$$/                             
| $$  \ $$| $$ /$$__  $$| $$      | $$_  $$ | $$ /$$__  $$| $$      | $$_  $$                             
| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$|  $$$$$$$|  $$$$$$$| $$ \  $$                            
|_______/ |__/ \_______/ \_______/|__/  \__/| $$ \_______/ \_______/|__/  \__/                            
                                       /$$  | $$                                                          
                                      |  $$$$$$/                                                          
                                       \______/                                                           
''')

while not ready:
    print(f'''
         __________________________________
        |                                  |
        |  Type 'q' at any moment to quit  |
        |   Type 1-8 to select an option   |
        |__________________________________|

        1) Start
        2) Players: {players}
        3) Decks: {decks} deck(s)
        4) Rounds: {targeted_round} (Select 0 rounds for endless mode)
        5) Gamble mode: {'On' if gamble_mode else 'Off'}
        6) Assist mode: {assist_mode}
        7) Help
        8) Quit
    ''')
    player_input = input('        Select your option: ')
    if (player_input.casefold().strip()) == '1':
        ready == True
        player_input = ''
        break
    elif player_input == '2':
        players = toggle_amount_of_players()
        player_input = ''
    elif player_input == '3':
        decks = toggle_amount_of_decks()
        player_input = ''
    elif player_input == '4':
        targeted_round = toggle_amount_of_rounds()
        player_input = ''
    elif player_input == '5':
        gamble_mode = toggle_gamble_mode()
        player_input = ''
    elif player_input == '6':
        assist_mode = toggle_assist_mode()
        player_input = ''
    elif player_input == '7':
        print('''
        Objective:
          Get the highest value withought passing 21
        
        Controls:
          Help: [h] pulls up this help menu
          Draw: [d] draws 1 more card
          Doubling down: [dd] if you get a score of 9, 10, or 11 on the first two cards, you can doubling down. This will allow you to draw only 1 more card but duble your bet
          Split: [s] if the first two cards are the same value, you can split them into two hands (an additional bet equal to the first is required). There is one exception: If the player splits two Aces, he receives only one more card and in such a case a score of 21 is not considered as Blackjack
        ''')
        input('Press enter to return')
    elif player_input == '8' or player_input == 'q':
        quit()

if gamble_mode:
    gamble_start_value = toggle_gamble_start_value()

while True:
    while current_round < targeted_round:
        pass


print('Thanks for playing. See you soon.')

print('\n \n ----------End---------- \n \n')
