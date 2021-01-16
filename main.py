dealers_hand = []


def check_player_action(check_action):
    while True:
        check_if_player_quits(check_action)
        if (check_action := check_action.casefold().strip()) in ('hel', 'hit', 'sta', 'dd', 'spl', 'ins', 'ttd', 'lea', 'ftt'):
            if check_action == 'hel':  # done
                print_help()
                return
            elif check_action == 'hit':
                return 'hit'
            elif check_action == 'sta':
                return 'sta'
            elif check_action == 'dd':
                return 'dd'
            elif check_action == 'spl':
                return 'spl'
            elif check_action == 'ins':
                return 'ins'
            elif check_action == 'ttd':
                return 'ttd'
            elif check_action == 'lea':
                return 'lea'
            elif check_action == 'ftt':
                return 'ftt'
        else:
            print('That was not a valid input, please try again.')
            check_action = input('')


# Anything above this is just a note/placeholder and has not been formaly implimented in the game
print('\n \n ----------Start---------- \n \n')

# Default variables and what they mean
# Option 2: Sets how many players will be playing
number_of_players = 3
# Option 3: Sets how many decks of 52 cards will be played with
decks = 1
# Option 4: Sets the targeted round for the game. 0 rounds is endless mode
targeted_round = 0
# Option 5: Turnes on/off a mode that allows betting
gamble_mode = False
# Option 5.5: When gamble_mode is on, this is the default value that everyone starts with
gamble_start_value = 10000
# Option 6: Tells the odds of the next card puting you at or under 21. Basicaly card counting
assist_mode = False
# A temporary vairable made as a place holder
Temp = ''
# Round counter
current_round = 0

# Functions & classes

# Creates players with all the needed info


class Player:
    def __init__(self):
        self.name = None
        self.wallet = 0
        self.hand1 = []
        self.hand2 = []
        self.hand3 = []
        self.hand4 = []

    def __repr__(self):
        return f'{self.name}: ${f"{(self.wallet):,}"}, Hand 1: {self.hand1}, Hand 2: {self.hand2}, Hand 3: {self.hand3}, Hand 4: {self.hand4} \n'

# Checks if the player is quiting the game


def check_if_player_quits(check_quit):
    '''Checks if the player is quiting the game'''
    if not str.isdecimal(check_quit) and ((check_quit := check_quit.casefold().strip()) == 'q' or check_quit == 'quit'):
        quit()
    else:
        return

# Prints the game rules


def print_help():
    '''Prints the game rules. Needs ( ) at the end.'''
    print('-'.center(107, '-'))
    print('''
    Game rules:
    The objective is to reach as close to 21 withough passing 21
    The game starts with the players making a bet of at least $10
    After all bets are made, each player recives 2 cards faced up
      A are 11 unles it passes 21. If that happens, it's value drops to 1
      J, Q, and K are 10
      All other cards are thire face value
    Then the dealer recives a card faced down and a card faced up
    Once everyone has a card the game begins
    If the player recives an A and either a J, Q, or K, this will total 21 and is called a Blackjack

    Blackjack:
    If the first two cards value equals to 21 (an A and a J, Q, or K) that is called a Blackjack.
    If a player gets a blackjack, they win x1.5 thire bet rather than x1
    If a player and a dealer get a Blackjack, the player keeps thire bet
    If the dealer has a Blackjack, the player loses thire bet

    If there is no Blackjack, the player can chose what they would like to do
      Help [hel]: Brings this sheet up to review the rules
        I.E. You forgot what a split does so you bring this up

      Hit [hit]: Draws a card. You can hit as many times as you want till you bust, though it is advised to stay at 17 or more.
        I.E. You start with a 3 and 5. You hit and get a 2. You hit again and get a 8. At 18 you chose to stay and your final score is 18.

      Stay [sta]: Keeps your curent cards.
        I.E. You start with a K and J. You stay and your final score is 20.

      Doubling down [dd]: If you get a score of 9, 10, or 11 on the first two cards, you can doubling down. When you duble down, you make an aditional bet equal to your original bet and you will recive only 1 more card. If you win, you will recive x2.0 you current bet.
        I.E. You bet $10 and start with a 6 and 4. You duble down and bet and aditional $10 for a total of $20. The dealer gives you your final card and it is an 8. Your final score is 18. If you win, you recive the $20 you bet plus $20 reward, if you lose, you lose $20.

      Split [spl]: If the first two cards are the same value, you can split them into two hands, this can be done up to 3 times for a total of 4 hands. Each hand requires an aditional bet equal to your original bet and each hand plays one at a time and is allowed to hit, split, or dubble down. There is one exception: If the player splits two Aces, they receive only one more card and in such a case a score of 21 is reacher, it is not considered a Blackjack, it is considered 21
        I.E. You bet $10 and start with an 8 and 8. You split and bet an aditional $10 for a toal of $20. You hit your fist hand and get a K. You chose to stay and your final score is 18 and move to your second hand. You hit your second hand and get a 5, you hit again and get a Q and bust. Your dealer goes and busts. You get $20 ($10 from your first hand + $10 from your reward and $0 from your second hand).

      Insurence [ins]: If the player thinks the dealer has a blackjack, the player can wager an aditional x0.5 of thire original bet. If the dealer has a blackjack, the player keeps thire bet and insurence. If the dealer does not, the player loses the insurence but keeps the bet. If the player and the dealer have a blackjack, the player only gets x2 of what was bet rather than x2.5
        I.E. You bet $10 and you beleve the dealer has a Blackjack. You take the insurence and bet another $5. The dealer has a Blackjack and you get back $15 ($10 from your bet and $5 from the insurence).

      Tip the Dealer [ttd]: Gives the dealer as much as you want. This brings no benifit to the player except the feeling of giving the dealer a pleasent reward.
        I.E. You are on a winning streak and decide to give the dealer some money. You tip the dealer $100.

      Leave [lea]: After a $0 bet you can leave the game.
        I.E. You are done playing for the day and decide to leave.

      Flip the Table [ftt]: Flips the table and ends the game sudenly, ruining the game for everyone.
        I.E. You are on a losing streak and people are making fun of you so you flip the table. Now no one invites you to the table anymore and the dealer blacklists you.

    After the player goes, it is the dealer's turn.
      If the dealer has 16 or lower, they will hit.
      If the dealer starts or reaches 17-21, they will stay.
      If the dealer goes over 21, they bust.
      If the dealer has an A and get 17-21, they may chose to stay or hit.

    After the dealer has gone, the winner is decided.

      If the plater has a higher card than the dealer, the player wins x2 the bet.
        I.E. If the player bet $10 and wins, they get $20 back

      If the player value is the same as the dealer, its a push and the player keeps ther bet.
        I.E. If the player bet $10 and ties, they get $10 back

      If the player value is lower then the dealer, the player loses thire bet.
        I.E. If the player bet $10 and loses, they get $0 back

    After 35% of the deck is placed, the deck is shufled again.
    After it is shufled, a player can select where to cut the cards''')
    check_if_player_quits(input('Press enter to return. '))
    print('-'.center(107, '-'))


# Game starting point
# Tital card
print('''
  /$$      /$$           /$$                                                     /$$
 | $$  /$ | $$          | $$                                                    | $$
 | $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$$$$$    /$$$$$$
 | $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$      |_  $$_/   /$$__  $$
 | $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \\ $$| $$ \\ $$ \\ $$| $$$$$$$$        | $$    | $$  \\ $$
 | $$$/ \\  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/        | $$ /$$| $$  | $$
 | $$/   \\  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$        |  $$$$/|  $$$$$$/
 |__/     \\__/ \\_______/|__/ \\_______/ \\______/ |__/ |__/ |__/ \\_______/         \\___/   \\______/
 
 
 
  /$$$$$$$$                            /$$       /$$        /$$$$$$                              /$$
 |__  $$__/                           | $$      |__/       /$$__  $$                            | $/
    | $$  /$$$$$$  /$$$$$$$   /$$$$$$$| $$$$$$$  /$$      | $$  \\__/  /$$$$$$   /$$$$$$  /$$$$$$|_//$$$$$$$
    | $$ /$$__  $$| $$__  $$ /$$_____/| $$__  $$| $$      |  $$$$$$  /$$__  $$ /$$__  $$|____  $$ /$$_____/
    | $$| $$$$$$$$| $$  \\ $$|  $$$$$$ | $$  \\ $$| $$       \\____  $$| $$  \\ $$| $$  \\__/ /$$$$$$$|  $$$$$$
    | $$| $$_____/| $$  | $$ \\____  $$| $$  | $$| $$       /$$  \\ $$| $$  | $$| $$      /$$__  $$ \\____  $$
    | $$|  $$$$$$$| $$  | $$ /$$$$$$$/| $$  | $$| $$      |  $$$$$$/|  $$$$$$/| $$     |  $$$$$$$ /$$$$$$$/
    |__/ \\_______/|__/  |__/|_______/ |__/  |__/|__/       \\______/  \\______/ |__/      \\_______/|_______/
 
 
 
  /$$$$$$$  /$$                     /$$                               /$$
 | $$__  $$| $$                    | $$                              | $$
 | $$  \\ $$| $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$  /$$$$$$   /$$$$$$$| $$   /$$
 | $$$$$$$ | $$ |____  $$ /$$_____/| $$  /$$/|__/ |____  $$ /$$_____/| $$  /$$/
 | $$__  $$| $$  /$$$$$$$| $$      | $$$$$$/  /$$  /$$$$$$$| $$      | $$$$$$/
 | $$  \\ $$| $$ /$$__  $$| $$      | $$_  $$ | $$ /$$__  $$| $$      | $$_  $$
 | $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$ \\  $$| $$|  $$$$$$$|  $$$$$$$| $$ \\  $$
 |_______/ |__/ \\_______/ \\_______/|__/  \\__/| $$ \\_______/ \\_______/|__/  \\__/
                                        /$$  | $$
                                       |  $$$$$$/
                                        \\______/''')

# Main menu
while True:
    print(f'''
         __________________________________________
        |                                          |
        |  Type 'q' at any moment to end the game  |
        |       Type 1-8 to select an option       |
        |__________________________________________|

        1) Start
        2) Players: {number_of_players}
        3) Decks: {decks} deck(s)
        4) Rounds: {"Endless" if targeted_round == 0 else targeted_round}
        5) Gamble mode: {'On' if gamble_mode else 'Off'}
        6) Assist mode: {'On' if assist_mode else 'Off'}
        7) Help''')
    player_input = input('\n        Select your option: ')
    check_if_player_quits(player_input)
    if (player_input := player_input.casefold().strip()) == '1':  # Leaves the menu and starts the game
        print('The game will start soon.')
        print('-'.center(107, '-'))
        break
    elif player_input == '2':  # Sets how many players are playing
        print('-'.center(107, '-'))
        while True:
            player_input = input(f'''
            Curently there are {number_of_players} players playing.
            How many players will play? [1-7]

            Players: ''')
            check_if_player_quits(player_input)
            if str.isdecimal(player_input) and (player_input := int(player_input)) in (range(1, 7)):
                players = player_input
                break
            else:
                print('That was not a valid input, please try again.')
        print(f'Sucsesfuly changed to {number_of_players} player(s)')
        print('-'.center(107, '-'))
    elif player_input == '3':  # Sets how many 52 card decks are going to be used
        print('-'.center(107, '-'))
        while True:
            player_input = input(f'''
            You are curently playing with {decks} decks.

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
            check_if_player_quits(player_input)
            if str.isdecimal(player_input) and (player_input := int(player_input)) in range(1, 10):
                decks = player_input
                break
            else:
                print('That was not a valid input, please try again.')
        print(f'Sucsesfuly changed to {decks} decks ({decks*52} cards)')
        print('-'.center(107, '-'))
    elif player_input == '4':  # Sets how many rounds will be played
        print('-'.center(107, '-'))
        while True:
            player_input = input(f'''
            You are curently playing {"endless" if targeted_round == 0 else targeted_round} rounds.

            How many rounds would you like to play?
            Type 0 for endless mode or any number for
            that amount of rounds.

            Rounds: ''')
            check_if_player_quits(player_input)
            if str.isdecimal(player_input) and (player_input := int(player_input)) >= 0:
                targeted_round = player_input
                break
            else:
                print('That was not a valid input, please try again.')
        player_input = ''
        print(
            f'Sucsesfuly changed to {"endless" if targeted_round == 0 else targeted_round} rounds.')
        print('-'.center(107, '-'))
    elif player_input == '5':  # Sets gamble mode on/off and what is the starting value
        print('-'.center(107, '-'))
        while True:
            player_input = input(f'''
            Gamble mode is currently {"on" if gamble_mode else "off"}{f" with a starting value of ${gamble_mode:,}" if gamble_mode else ""}.
            Would you like to turn gamble mode on or off?

            [On/Off]: ''')
            check_if_player_quits(player_input)
            if (player_input := player_input.casefold().strip()) == 'on':
                gamble_mode = True
                while True:
                    print(
                        f'Curent starting cash is ${gamble_start_value:,}. Would you like to change it?')
                    player_input = input('[Y/N]: ')
                    check_if_player_quits(player_input)
                    if (player_input := player_input.casefold().strip()) == 'y':
                        while True:
                            print('How much would you like to start with?')
                            player_input = input('Start value: ')
                            check_if_player_quits(player_input)
                            if str.isdecimal(player_input) and (player_input := int(player_input)) > 0 and player_input % 10 == 0:
                                gamble_start_value = player_input
                                break
                            elif str.isdecimal(str(player_input)) and player_input > 0 and player_input % 10 != 0:
                                print(
                                    'That was not a valid input, the value must be a multiple of 10, please try again.')
                            else:
                                print(
                                    'That was not a valid input, please try again.')
                        break
                    elif player_input == 'n':
                        break
                    else:
                        print('That was not a valid input, please try again.')
                break
            elif player_input == 'off':
                gamble_mode = False
                break
            else:
                print('That was not a valid input, please try again.')
        print(
            f'Sucsessfuly turned gamble mode {f"on and set the starting value to: ${gamble_mode:,}" if gamble_mode else "off"}.')
        print('-'.center(107, '-'))
    elif player_input == '6':  # Sets assist mode on/off
        print('-'.center(107, '-'))
        while True:
            player_input = input('''
            Would you like to turn assist mode on or off?
        
            [On/Off]: ''')
            check_if_player_quits(player_input)
            if player_input.casefold().strip() == 'on':
                assist_mode = True
                break
            elif player_input.casefold().strip() == 'off':
                assist_mode = False
                break
            else:
                print('That was not a valid input, please try again.')
        print('-'.center(107, '-'))
    elif player_input == '7':  # Prints the rules
        print_help()
    else:
        print('That was not a valid input, please try again.')
        print('-'.center(107, '-'))


# Game


# Creates {number_of_players} amount of players
player = {}
for n in range(number_of_players):
    player.update({n + 1: Player()})

# Gives each player the apropriet dict and sets both name and gamble_start_value
for n in range(number_of_players):
    while True:
        player_input = input(f'What is player {n+1}\'s name? :')
        check_if_player_quits(player_input)
        temp = input(f'Is the name {player_input} correct? [Y/N]: ')
        check_if_player_quits(temp)
        if (temp := temp.casefold().strip()) == 'y':
            player[n+1].name = player_input
            break
        elif temp == 'n':
            print('Ok, lets try that again then.')
        else:
            print('That was not a valid input, please try again.')
    player[n+1].wallet = gamble_start_value

print(player)


# Deck creation
deck_of_cards = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K')
dealers_deck = list(deck_of_cards)*4*decks

# Player creation


print('Thanks for playing. See you soon.')

print('\n \n ----------End---------- \n \n')
