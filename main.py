import random
from time import sleep

# Custom Functions
# Prints the help text
def print_help():
    while True:
        print('-'.center(108, '-'))
        print('''Game rules:
 The objective is to reach as close to 21 without passing 21. The game starts with the players making a bet of at least $10. After all bets are made, the dealer receives one card faced up and one card faced down. Each player then receives 2 cards faced up.
     A are worth 11 unless it passes 21, if that happens, its value drops to 1
     J, Q, and K are worth 10
     All other cards are their face value
 Once everyone has a card the game begins''')
        while True:
            player_input = input(
                '\n\n--------------------------------------\n\nContinue or exit [C/E]?: ').casefold().strip()
            check_if_player_quits(player_input)
            if player_input == 'c':
                break
            elif player_input == 'e':
                print('\n--------------------------------------')
                return
            else:
                print('That was not valid, please try again.')
        print('''
 --------------------------------------
 
 Blackjack:
 If the first two cards value equals to 21 (an A and either a J, Q, or K) that is called a Blackjack.
 If a player gets a blackjack and the dealer does not, the player wins x2.5 their bet rather than x1
 If a player and the dealer have a Blackjack, it’s a push and the player keeps their bet
 If the dealer has a Blackjack and the player does not, the player loses their bet
 
 If the dealer’s first card is either an A, J, Q, or K, the players can opt to get insurance:
     Insurance: The player can wager an additional x0.5 of their original bet. If the dealer has a blackjack, the player keeps their bet and insurance. If the dealer does not, the player loses the insurance but keeps the bet. If the player and the dealer have a blackjack, the player only gets x2 of what was bet rather than x2.5
 I.E. You bet $10 and you believe the dealer has a Blackjack. You take the insurance and bet another $5. The dealer has a Blackjack and you get back $15 ($10 from your bet and $5 from the insurance).
 
 If the dealer does not have either an A, J, Q, or K, the player can choose what they would like to do
 Help [hel]: Brings this sheet up to review the rules
 
 Hit [hit]: Draws a card. You can hit as many times as you want till you bust (go over 21), though it is advised to stay between 17-21.
 I.E. You start with a 3 and 5. You hit and get a 2. You hit again and get an 8. At 18 you chose to stay and your final score is 18.
 
 Stay [sta]: Keeps your current cards.
 I.E. You start with a K and J. You stay and your final score is 20.
 
 Doubling down [dd]: If you get a score of 9, 10, or 11 on the first two cards, you can double down. When you double down, you make an additional bet equal to your original bet and you will receive only 1 more card. If you win, you will receive x2.0 your current bet.
 I.E. You bet $10 and start with a 6 and 4. You double down and bet and additional $10 for a total of $20. The dealer gives you your final card and it is an 8. Your final score is 18. If you win, you receive the $20 you bet plus $20 reward, if you lose, you lose $20.
 
 Split [spl]: If the first two cards are the same value (such as a 4 and another 4), you can split them into two hands (this can be done up to 3 times for a total of 4 hands). Each hand requires an additional bet equal to your original bet and each hand plays one at a time and is allowed to hit, split, or double down. There is one exception: If the player splits two Aces, they receive only one more card and in such a case, if a score of 21 is reached, it is not considered a Blackjack but rather it is considered a normal 21
 I.E. You bet $10 and start with an 8 and 8. You split and bet an additional $10 for a total of $20. You hit your fist hand and get a K. You chose to stay and your final score is 18 and move to your second hand. You hit your second hand and get a 5, you hit again and get a Q and bust. Your dealer goes and busts. You get $20 ($10 from your first hand + $10 from your reward and $0 from your second hand).
 
 Tip the Dealer [ttd]: Gives the dealer a tip. This brings no benefit to the player except the feeling of rewarding the dealer a pleasant reward.
 I.E. You are on a winning streak and decide to give the dealer some money. You tip the dealer $100.
 
 Flip the Table [ftt]: Flips the table and ends the game suddenly, ruining the game for everyone.
 I.E. You are on a losing streak and people are making fun of you so you flip the table. Now no one invites you to the table anymore and the dealer blacklists you.''')
        while True:
            player_input = input(
                '\n\n--------------------------------------\n\nContinue or exit [C/E]?: ').casefold().strip()
            check_if_player_quits(player_input)
            if player_input == 'c':
                break
            elif player_input == 'e':
                print('\n--------------------------------------')
                return
            else:
                print('That was not valid, please try again.')
        print('''
 --------------------------------------
 
 After the player goes, it is the dealer's turn.
     If the dealer has 16 or lower, they will hit.
     If the dealer starts or reaches 17-21, they will stay.
     If the dealer goes over 21, they bust.
     If the dealer has an A and get 17-21, they may choose to stay or hit.
 
 After the dealer has gone, the winner is decided.
 
 If the player's card value is higher than the dealer, the player wins x2 their bet.
     I.E. If the player bet $10 and wins, they get $20 back
 
 If the player's card value is the same as the dealer, it’s a push and the player keeps their bet.
     I.E. If the player bet $10 and ties, they get $10 back
 
 If the player's card value is lower than the dealer, the player loses their bet.
     I.E. If the player bet $10 and loses, they get $0 back
 
 After 35% of the deck is used, the deck is re-shuffled.
 After it is shuffled, a random player can select where to cut the cards
 
 Skiping a round or leaving the game: At the begining of the round, the player can leave the game or skip before any bet is made.
     I.E. You are done playing for the day and decide to leave after making a $0 bet.''')
        while True:
            player_input = input(
                '\n\n--------------------------------------\n\nExit or repeat? [E/R]?: ').casefold().strip()
            check_if_player_quits(player_input)
            if player_input == 'r':
                print("")
                break
            elif player_input == 'e':
                print('\n\n--------------------------------------\n\n')
                return
            else:
                print('That was not valid, please try again.', end='\n\n')


# Checks if the player is quiting the game
def check_if_player_quits(check_quit):
    if check_quit.isalpha() and check_quit in ('q', 'quit'):
        print('Exiting the game. Thanks for playing!\n\n' +
              'End'.center(108, '-'), end='\n\n')
        quit()


# Draws a card for the dealer and removes it from the deck
def dealer_draw():
    dealer.hand.append(random.choice(dealer.deck))
    dealer.deck.remove(dealer.hand[-1])


# Makes a player draw a card into hand-X depending on the hand_numb
def player_draw(hand_numb):
    for n in range(number_of_players):
        if player[n+1].leave == False and player[n+1].skip == False:
            player[n +
                        1].hand[hand_numb].append(random.choice(dealer.deck))
            dealer.deck.remove(player[n+1].hand[hand_numb][-1])


# Adds the last card's value to the hand_value of the specific player/dealer
def determine_hand_value(player, hand):
    player.hand_value = 0
    for card in hand:
        if hand == []:
            return
        elif card in ['A(1)']:
            player.hand_value += 1
        elif card in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            player.hand_value += int(card)
        elif card in ['J(10)', 'Q(10)', 'K(10)']:
            player.hand_value += 10
        else:
            player.hand_value += 11
    while player.hand_value > 21:
        if any(card in player.hand for card in ['A(11)']):
            player.hand_value -= 10
            player_hand[player.hand.index('A(11)')] = 'A(1)'
        else:
            break
    return


# Checks what the player can do
def check_player_moves(player_numb, hand_numb):
    player[player_numb].posible_moves = ['[hel]', '[hit]', '[sta]']
    if any([player[player_numb].hand[hand_numb][0] + player[player_numb].hand[hand_numb][1] == x for x in (9, 10, 11)]) and len(player[player_numb].hand[hand_numb]) == 2:
        player[player_numb].posible_moves.append('[dd]')
    if hand_numb == 1 and player[player_numb].hand[1][0] == player[player_numb].hand[1][1] and len(player[player_numb].hand[1]) == 2 and player[player_numb].hand[4] == [] and (player[player_numb].hand[2][0] == [] or 'A' not in player[player_numb].hand[2]):
        player[player_numb].posible_moves.append('[spl]')
    if player[player_numb].hand[hand_numb][0] + player[player_numb].hand[hand_numb][1] == 21 and len(player[player_numb].hand[hand_numb]) == 2:
        player[player_numb].posible_moves = ['[hel]', '[sta]']
    player[player_numb].posible_moves.extend(['[ttd]', '[ftt]'])

# Custom Variables
# Whatever the player inputs
player_input = None

# Option 2: Sets how many players will be playing
number_of_players = 1

# Option 3: Sets how many decks of 52 cards will be played with
deck_size = 1

# Option 4: Sets the targeted round for the game. 0 rounds is endless mode
targeted_round = 0

# Option 5: Turns gambaling on/off
gamble_mode = True

# Option 5.5: When gamble_mode is on, this is the default money that everyone starts with
gamble_start_value = 10000

# Option 6: Tells the odds of the next card puting you at or under 21. Basicaly card counting
assist_mode = False

# Adds a new line in f-strings
nl = '\n'

# Round counter
current_round = 0

# Miscellaneous counter
misc_count = 0


# Player class (range from player1 - player7)
class PlayerCreation:
    def __init__(self):
        self.name = None
        self.wallet = 0
        self.bet = 0
        self.skip = False
        self.posible_moves = []
        self.hit = False
        self.stay = False
        self.double_down = {
            0: False,
            1: False,
            2: False,
            3: False
        }
        self.split = False
        self.insurence = False
        self.tip_the_dealer = False
        self.leave = True
        self.flip_the_table = False
        self.hand = {
            0: [],
            1: [],
            2: [],
            3: []
        }
        self.hand_value = 0
        self.blackjack = False

    def __repr__(self):
        return f'''{self.name} data:
 Wallet size: {self.wallet}
 Currently betting: {self.bet}
 Skip: {self.skip}
 Posible moves: {self.posible_moves}
 Hit: {self.hit}
 Stay: {self.stay}
 Double down: {self.double_down}
 Split: {self.split}
 Has insurence: {self.insurence}
 Tip the dealer: {self.tip_the_dealer}
 Left the game: {self.leave}
 Flip the table: {self.flip_the_table}
 Hand 1: {self.hand[1]}
 Hand 2: {self.hand[2]}
 Hand 3: {self.hand[3]}
 Hand 4: {self.hand[4]}
 Hand value: {self.hand_value}
 Blackjack: {self.blackjack}\n\n'''''


# Creates 7 players
player = {}
for n in range(0, 7):
    player[n] = PlayerCreation()


# Dealer class, created this way to stay consistent with player creation
class DealerCreation:
    def __init__(self):
        self.deck_of_cards = ('A(11)', '2', '3', '4', '5',
                              '6', '7', '8', '9', '10', 'J(10)', 'Q(10)', 'K(10)')
        self.deck = []
        self.hand = []
        self.hand_value = 0
        self.blackjack = False

    def __repr__(self):
        return f'''Dealer data:
    Remaining cards in the deck: {self.deck}
    Hand: {self.hand}
    Hand value: {self.hand_value}
    Blackjackt: {self.blackjack}\n\n'''


# Creates the dealer
dealer = DealerCreation()


print('\n\n' + 'Start'.center(108, '-'), end='\n\n')

# Main menu
while True:
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
    print('\n\n' + ' _____________________________________________________ '.center(107, ' '))
    print('|                                                     |'.center(107, ' '))
    print('|  Type \'q\' or \'quit\' at any moment to quit the game  |'.center(107, ' '))
    print('|            Type 1-8 to select an option             |'.center(107, ' '))
    print('|_____________________________________________________|'.center(107, ' '))
    print('')
    print('1) Start                                    '.center(107, ' '))
    print(f'2) Players: {number_of_players}                               '.center(
        107, ' '))
    print(f'3) Decks used: {deck_size} {"deck (52 cards)  " if deck_size == 1 else f"decks ({deck_size*52} cards)"}         '.center(
        107, ' '))
    print(f'4) Rounds: {"Endless" if targeted_round == 0 else f"{targeted_round}      "}{" "*(27-(len(str(targeted_round))))}'.center(107, ' '))
    print(f'5) Gamble mode: {"On " if gamble_mode else "Off"}                         '.center(
        107, ' '))
    print(f'6) Assist mode: {"On " if assist_mode else "Off"}                         '.center(
        107, ' '))
    print('7) Help                                     '.center(107, ' '))
    player_input = input('\n' + 'Select your option: ').casefold().strip()
    check_if_player_quits(player_input)
    if player_input == '1':  # Leaves the menu and starts the game
        print('The game will start soon.\n\n' +
              'Start'.center(108, '-'), end='\n\n')
        break
    elif player_input == '2':  # Sets number_of_players
        print('\n\n' + '-'.center(108, '-'), end='\n\n')
        while True:
            player_input = input(
                f'''Curently number of players: {number_of_players}\nNew number of players [1-7]: ''').casefold().strip()
            check_if_player_quits(player_input)
            if player_input.isdecimal() and int(player_input) in (range(1, 8)):
                number_of_players = int(player_input)
                print(
                    f'Number of players set to: {number_of_players}'+'\n\n' + '-'.center(108, '-'), end='\n\n')
                break
            else:
                print(
                    'That was not a valid input, please try again.\n--------------------------------------', end='\n\n')
    elif player_input == '3':  # Sets deck_size
        print('\n\n' + '-'.center(108, '-'), end='\n\n')
        while True:
            print(
                f'Curent decks used: {deck_size} {"deck (52 cards)" if deck_size == 1 else f"decks ({deck_size*52} cards)"}')
            print('With how many decks would you like to play with?', end='\n\n')
            print(' ___________________________________ ')
            print('|                                   |')
            print('| 1 deck (52 cards) (clasic mode)   |')
            print('| 2 decks (104 cards)               |')
            print('| 3 decks (156 cards)               |')
            print('| 4 decks (208 cards)               |')
            print('| 5 decks (260 cards)               |')
            print('| 6 decks (312 cards)               |')
            print('| 7 decks (364 cards)               |')
            print('| 8 decks (416 cards)               |')
            print('| 9 decks (468 cards) (casino mode) |')
            print('|___________________________________|', end='\n\n\n')
            player_input = input(
                'New deck size [1-9]: ').casefold().strip()
            check_if_player_quits(player_input)
            if player_input.isdecimal() and int(player_input) in range(1, 10):
                deck_size = int(player_input)
                print(
                    f'Decks in use set to: {deck_size} ({deck_size*52} cards)\n\n' + '-'.center(108, '-'), end='\n\n')
                break
            else:
                print(
                    'That was not a valid input, please try again.\n--------------------------------------', end='\n\n')
    elif player_input == '4':  # Sets targeted_round
        print('\n\n' + '-'.center(108, '-'), end='\n\n')
        while True:
            player_input = input(
                f'''Current rounds: {"Endless" if targeted_round == 0 else targeted_round}  rounds')\n'How many rounds would you like to play?\n\nRounds [0-\u221E]: ''').casefold().strip()
            check_if_player_quits(player_input)
            if player_input.isdecimal() and int(player_input) >= 0:
                targeted_round = int(player_input)
                print(
                    f'Number of rounds set to: {"Endless" if targeted_round == 0 else targeted_round}\n\n' + '-'.center(108, '-'), end='\n\n')
                break
            else:
                print(
                    'That was not a valid input, please try again.\n--------------------------------------', end='\n\n')
    elif player_input == '5':  # Sets gamble_mode and gamble_start_value
        print('\n\n' + '-'.center(108, '-'), end='\n\n')
        while True:
            player_input = input(
                f'Gamble mode: {"On" if gamble_mode else "Off"}\n{f"Starting money is set to: ${gamble_start_value:,}.{nl}" if gamble_mode else ""}Would you like to turn gamble mode on or off?\n\nGamble mode [On/Off]: ').casefold().strip()
            check_if_player_quits(player_input)
            if player_input == 'on':
                gamble_mode = True
                while True:
                    player_input = input(
                        f'Starting money is set to: ${gamble_start_value:,}\nWould you like to change it?\n\nChange [Y/N]: ').casefold().strip()
                    check_if_player_quits(player_input)
                    if player_input == 'y':
                        while True:
                            player_input = input(
                                'How much will everyone start with?\n\nStart value [10-\u221E]: ').casefold().strip()
                            check_if_player_quits(player_input)
                            if player_input.isdecimal() and int(player_input) > 0 and int(player_input) % 10 == 0:
                                gamble_start_value = int(
                                    player_input)
                                break
                            elif player_input.isdecimal() and int(player_input) > 0 and int(player_input) % 10 != 0:
                                print(
                                    'That was not valid, the value must be a multiple of 10, please try again.\n--------------------------------------', end='\n\n')
                            else:
                                print(
                                    'That was not valid, please try again.\n--------------------------------------', end='\n\n')
                        break
                    elif player_input == 'n':
                        break
                    else:
                        print(
                            'That was not a valid input, please try again.\n--------------------------------------', end='\n\n')
                break
            elif player_input == 'off':
                gamble_mode = False
                gamble_start_value = 10000
                break
            else:
                print(
                    'That was not a valid input, please try again.\n--------------------------------------', end='\n\n')
        print(f'Gamble mode is {f"on and everyone will start with: ${gamble_start_value:,}" if gamble_mode else "off"}\n\n' +
              '-'.center(108, '-'), end='\n\n')
    elif player_input == '6':  # Sets assist mode on/off
        print('\n\n' + '-'.center(108, '-'), end='\n\n')
        while True:
            player_input = input(
                f'Assist mode: {"On" if assist_mode else "Off"}\nWould you like to turn assist mode on or off?\n\nAssist mode [On/Off]: ').casefold().strip()
            check_if_player_quits(player_input)
            if player_input == 'on':
                assist_mode = True
                break
            elif player_input == 'off':
                assist_mode = False
                break
            else:
                print(
                    'That was not valid, please try again.\n--------------------------------------', end='\n\n')
        print(
            f'Assist mode set to: {"On" if assist_mode else "Off"}\n\n' + '-'.center(108, '-'), end='\n\n')
    elif player_input == '7':  # Prints the rules
        print_help()
    else:
        print('That was not a valid input, please try again.\n'+'-'.center(107, '-'))

# Dealer intro
print(f'''Dealer: Welcome honrable guests to Tenshi Sora's Casino.\n{"Dealer: The minimum bet at this table is a $10 chip, no $1 nor $5 chip is acceptable for betting." if gamble_mode else "Dealer: Let's have a fun, casual game with no betting."}\nDealer: Before we begin, I would like to know your names.''')

# For number_of_players players, sets their names, default wallet sizes, and sets each player as in game
for n in range(number_of_players):
    player_input = input(
        f'Dealer: You in seat #{n+1}, what is your name?\n\nName : ')
    misc_count = 0
    while player[n].name == None:
        check_if_player_quits(player_input)
        for i in range(number_of_players):
            if player[i].name == None or player_input.casefold() != player[i].name.casefold():
                misc_count += 1
        if misc_count != number_of_players:
            player_input = input(
                'Dealer: That will be confusing with two people with the same name. What else can I call you?\n\nNew name: ')
            misc_count = 0
        elif misc_count == number_of_players:
            player[n].name = player_input
            while True:
                player_input = input(
                    f"Dealer: Your name is '{player[n].name}' correct?\n\n[Y/N]: ").casefold().strip()
                check_if_player_quits(player_input)
                if player_input == 'y':
                    print(f'Dealer: Nice to meet you {player[n].name}.')
                    break
                elif player_input == 'n':
                    player_input = input(
                        f'Dealer: I beg your pardon, I must have misunderstood you. Lets try this again then, what is your name?\n\nName : ')
                    player[n].name = None
                    misc_count = 0
                    break
                else:
                    print(f'Dealer: I am sorry, I didn\'t get that.')
    player[n].leave = False
    if gamble_mode:
        player[n].wallet = gamble_start_value

# Creates the playable deck, and shuffles it
print(f'Dealer: Now that I know your {"name" if number_of_players == 1 else "names"}, let\'s begin.\nDealer: We are playing {"till you decide to leave" if targeted_round == 0 else f"for {targeted_round} rounds"}.\nDealer: May the odds ever be in your favor.\n\n* Dealer shuffled the deck *', end='')
dealer.deck = list(dealer.deck_of_cards)*4*deck_size
random.shuffle(dealer.deck)

# Game actualy starts
while targeted_round == 0 or current_round != targeted_round:
    current_round += 1  # Default 0, adds 1 to determine the current round
    if targeted_round == 0:  # Endless mode: prints current round
        print(
            '\n\n' + f'Round {current_round}'.center(108, '-'), end='\n\n')
    else:  # Prints current_round of targeted_round or final round
        print('\n\n' + 'Final round'.center(108, '-'), end='\n\n') if current_round == targeted_round else print(
            '\n\n' + f'Round {current_round} of {targeted_round}'.center(108, '-'), end='\n\n')
    if current_round >= 2:  # Asks if the player wants to leave or skip starting round 2
        while True:
            player_input = input(
                'Dealer: Would anyone like to skip this turn or leave?\n\n[Y/N] :').casefold().strip()
            check_if_player_quits(player_input)
            if player_input == 'y':
                while player_input == 'y':
                    # Ask who wants to leave and sets player[n].leave = True/False
                    while True:
                        print(
                            'Dealer: Curently we have the following people playing: | ', end='')
                        for n in range(number_of_players):
                            if player[n].leave == False:
                                print(f'{player[n].name} | ', end='')
                        player_input = input(
                            '\nDealer: Would anyone like to leave? Remember that you can\'t come back to this table later.\n\n[Y/N]: ').casefold().strip()
                        check_if_player_quits(player_input)
                        if player_input == 'y':
                            while player_input == 'y':
                                print(
                                    'Dealer: Alright, who would like to leave?:\n| ', end='')
                                for n in range(number_of_players):
                                    if player[n].leave == False:
                                        print(
                                            f'{player[n].name} | ', end=' ')
                                player_input = input(
                                    ': ').casefold().strip()
                                check_if_player_quits(player_input)
                                for n in range(number_of_players):
                                    if player_input == player[n].name.casefold().strip() and player[n].leave == False:
                                        player[n].leave = True
                                        print(
                                            f'Dealer: Thanks for playing {player[n].name}')
                                        break
                                    elif n+1 == number_of_players:
                                        print(
                                            f'Dealer: I apoligize but I do not know a "{player_input}" in this table.')
                                while True:
                                    player_input = input(
                                        'Dealer: Would anyone else like to leave?\n\n[Y/N]: ').casefold().strip()
                                    check_if_player_quits(
                                        player_input)
                                    if player_input == 'y':
                                        break
                                    elif player_input == 'n':
                                        break
                                    else:
                                        print('Dealer: I didn\'t get that.')
                            break
                        elif player_input == 'n':
                            print('Dealer: Ok what about skipping?')
                            break
                        else:
                            print('Dealer: I didn\'t get that.')
                    # Ask who wants to skip and sets player[n].skip = True/False
                    while True:
                        print(
                            'Dealer: Curently we have the following people playing this round: | ', end='')
                        for n in range(number_of_players):
                            if player[n].leave == False and player[n].skip == False:
                                print(f'{player[n].name} | ', end='')
                        player_input = input(
                            '\nDealer: Would anyone like to skip this round? Remember that you can\'t re-join till the round is over.\n\n[Y/N]: ').casefold().strip()
                        check_if_player_quits(player_input)
                        if player_input == 'y':
                            while player_input == 'y':
                                print(
                                    'Dealer: Who would like to skip?:\n| ', end='')
                                for n in range(number_of_players):
                                    if player[n].skip == False and player[n].leave == False:
                                        print(
                                            f'{player[n].name} | ', end=' ')
                                player_input = input(
                                    ': ').casefold().strip()
                                check_if_player_quits(player_input)
                                for n in range(number_of_players):
                                    if player_input == player[n].name.casefold().strip() and player[n].skip == False and player[n].leave == False:
                                        player[n].skip = True
                                        print(
                                            f'Dealer: {player[n].name} is out for this round.')
                                        break
                                    elif player_input == player[n].name.casefold().strip() and player[n].skip == True:
                                        print(
                                            f'Dealer: {player[n].name} is already out for this round.')
                                        break
                                    elif n+1 == number_of_players:
                                        print(
                                            f'Dealer: I apoligize but I do not know a "{player_input}" in this table.')
                                while True:
                                    player_input = input(
                                        'Dealer: Would anyone else like to skip this round?\n\n[Y/N]: ').casefold().strip()
                                    check_if_player_quits(
                                        player_input)
                                    if player_input == 'y':
                                        break
                                    elif player_input == 'n':
                                        break
                                    else:
                                        print('Dealer: I didn\'t get that.')
                            break
                        elif player_input == 'n':
                            print('Dealer: Alright, moving on then.')
                            break
                        else:
                            print('Dealer: I didn\'t get that.')
                    print(
                        'Dealer: curently we have the following people playing: | ', end='')
                    misc_count = 0
                    for n in range(number_of_players):
                        if player[n].leave == False:
                            print(f'{player[n].name} | ', end='')
                        elif player[n].leave == True:
                            misc_count += 1
                        if misc_count == number_of_players:
                            print('|', end='')
                    print(
                        '\nDealer: And these people are playing this round: | ', end='')
                    misc_count = 0
                    for n in range(number_of_players):
                        if player[n].leave == False and player[n].skip == False:
                            print(f'{player[n].name} | ', end=' ')
                        elif player[n].leave == False and player[n].skip == True:
                            misc_count += 1
                        if misc_count == number_of_players:
                            print('|', end='')
                    while True:
                        player_input = input(
                            '\nDealer: Would anyone else like to leave or skip?\n\n[Y/N]: ').casefold().strip()
                        check_if_player_quits(player_input)
                        if player_input == 'y':
                            break
                        elif player_input == 'n':
                            print('Dealer: Lets move on then.')
                            break
                        else:
                            print('Dealer: I didn\'t get that.')
                break
            elif player_input == 'n':
                print('Dealer: Ok, lets start then.')
                break
            else:
                print('Dealer: I didn\t get that.')
    if gamble_mode:  # Makes a bet if gammble == True
        for n in range(number_of_players):
            while player[n].leave == False and player[n].skip == False:
                while True:  # Asks how much to bet
                    player_input = input(
                        f'Dealer: How much would you like to bet this round {player[n].name}?\n\nWallet ${player[n].wallet:,}: ').strip()
                    check_if_player_quits(player_input)
                    if player_input.isdecimal() and int(player_input) > 0:
                        player[n].bet = int(player_input)
                        if player[n].bet % 10 == 0 and player[n].bet <= player[n].wallet:
                            break
                        elif player[n].bet % 10 == 0:
                            print(
                                f'Dealer: You can\'t make a bet higher than ${player[n].wallet:,}.')
                        else:
                            print(
                                f'Dealer: You can\'t make a bet of ${int(player[n].bet)} beacuse you can\' bet ${int(player[n].bet) % 10}.')
                    else:
                        print('Dealer: That was not a valid bet.')
                while True:  # Bet confirmation
                    player_input = input(
                        f'Dealer: Just to confirm {player[n].name}, you would like bet ${player[n].bet:,} correct?\n\n[Y/N]: ').casefold().strip()
                    check_if_player_quits(player_input)
                    if player_input == 'y':
                        print(
                            f'Dealer: Ok, {player[n].name} has bet ${player[n].bet:,}.')
                        player[n].wallet -= player[n].bet
                        break
                    elif player_input == 'n':
                        print(
                            f'Dealer: I am sorry {player[n].name}, I must have misunderstood you. Lets try again.')
                        player[n].bet = 0
                        break
                    else:
                        print(
                            f'Dealer: I didn\'t get that {player[n].name}.')
                if player[n].bet > 0:
                    break
        print(
            f'Dealer: Now that the {"bet is" if number_of_players == 0 else "bets are"} on the table, let\'s begin.')
    for _ in range(2):  # Each player draws 1 card then each player draws 1 card again and adds the value of the 2 cards
        for n in range(number_of_players):
            player[n].hand[0].append(random.choice(dealer.deck))
            dealer.deck.remove(player[n].hand[0][-1])
            determine_hand_value(player[n], player[n].hand[0])
    # Checks posible moves and checks for blackjack
    for n in range(number_of_players):
        player[n].posible_moves = ['hel', 'hit', 'sta', 'ttd', 'ftt']
        if player[n].hand[0][0] == player[n].hand[0][1]:
            player[n].posible_moves.insert(3, 'spl')
        if any(value in str(player[n].hand_value) for value in ['9', '10', '11']):
            player[n].posible_moves.insert(3, 'dd')
        if any(card in player[n].hand[0] for card in ['A(11)']) and any(card in player[n].hand[0] for card in ['10', 'J(10)', 'Q(10)', 'K(10)']):
            player[n].blackjack = True
            player[n].posible_moves = ['hel', 'sta', 'ttd', 'ftt']
    dealer_draw()  # Draws 1 card for the dealer
    determine_hand_value(dealer, dealer.hand)
    # Prints each player's card one at a time then the dealer's card
    for c1 in range(number_of_players):
        print('\n\n' + '-'.center(108, '-'), end='\n\n')
        print(f'Dealer\'s cards:')
        print(
            f'{player[0].name}\'s cards: {player[0].hand[0][0] if c1 >= 0 else ""}')
        print(
            f'{player[1].name}\'s cards: {player[1].hand[0][0] if c1 >= 1 else ""}') if number_of_players >= 2 else ''
        print(
            f'{player[2].name}\'s cards: {player[2].hand[0][0] if c1 >= 2 else ""}') if number_of_players >= 3 else ''
        print(
            f'{player[3].name}\'s cards: {player[3].hand[0][0] if c1 >= 3 else ""}') if number_of_players >= 4 else ''
        print(
            f'{player[5].name}\'s cards: {player[5].hand[0][0] if c1 >= 4 else ""}') if number_of_players >= 5 else ''
        print(
            f'{player[6].name}\'s cards: {player[6].hand[0][0] if c1 >= 5 else ""}') if number_of_players >= 6 else ''
        print(
            f'{player[7].name}\'s cards: {player[7].hand[0][0] if c1 >= 6 else ""}') if number_of_players >= 7 else ''
        sleep(.5)
        if c1+1 == number_of_players:
            for c2 in range(number_of_players):
                print('\n\n' + '-'.center(108, '-'), end='\n\n')
                print(f'Dealer\'s cards:')
                print(
                    f'{player[0].name}\'s cards: {player[0].hand[0][0]}{f", {player[0].hand[0][1]} = {player[0].hand_value}" if c2 >= 0 else ""}')
                print(f'{player[1].name}\'s cards: {player[1].hand[0][0]}{f", {player[1].hand[0][1]} = {player[1].hand_value}" if c2 >= 1 else ""}') if number_of_players >= 2 else ''
                print(f'{player[2].name}\'s cards: {player[2].hand[0][0]}{f", {player[2].hand[0][1]} = {player[2].hand_value}" if c2 >= 2 else ""}') if number_of_players >= 3 else ''
                print(f'{player[3].name}\'s cards: {player[3].hand[0][0]}{f", {player[3].hand[0][1]} = {player[3].hand_value}" if c2 >= 3 else ""}') if number_of_players >= 4 else ''
                print(f'{player[5].name}\'s cards: {player[5].hand[0][0]}{f", {player[5].hand[0][1]} = {player[5].hand_value}" if c2 >= 4 else ""}') if number_of_players >= 5 else ''
                print(f'{player[6].name}\'s cards: {player[6].hand[0][0]}{f", {player[6].hand[0][1]} = {player[6].hand_value}" if c2 >= 5 else ""}') if number_of_players >= 6 else ''
                print(f'{player[7].name}\'s cards: {player[7].hand[0][0]}{f", {player[7].hand[0][1]} = {player[7].hand_value}" if c2 >= 6 else ""}') if number_of_players >= 7 else ''
                sleep(.5)
                if c2+1 == number_of_players:
                    for _ in range(2):
                        print('\n\n' + '-'.center(108, '-'), end='\n\n')
                        print(
                            f'Dealer\'s cards: {dealer.hand[0]}{", ?" if _ else ""}')
                        print(
                            f'{player[0].name}\'s cards: {player[0].hand[0][0]}, {player[0].hand[0][1]} = {player[0].hand_value}')
                        print(
                            f'{player[1].name}\'s cards: {player[1].hand[0][0]}, {player[1].hand[0][1]} = {player[1].hand_value}') if number_of_players >= 2 else ''
                        print(
                            f'{player[2].name}\'s cards: {player[2].hand[0][0]}, {player[2].hand[0][1]} = {player[2].hand_value}') if number_of_players >= 3 else ''
                        print(
                            f'{player[3].name}\'s cards: {player[3].hand[0][0]}, {player[3].hand[0][1]} = {player[3].hand_value}') if number_of_players >= 4 else ''
                        print(
                            f'{player[5].name}\'s cards: {player[5].hand[0][0]}, {player[5].hand[0][1]} = {player[5].hand_value}') if number_of_players >= 5 else ''
                        print(
                            f'{player[6].name}\'s cards: {player[6].hand[0][0]}, {player[6].hand[0][1]} = {player[6].hand_value}') if number_of_players >= 6 else ''
                        print(
                            f'{player[7].name}\'s cards: {player[7].hand[0][0]}, {player[7].hand[0][1]} = {player[7].hand_value}') if number_of_players >= 7 else ''
                        print('\n\n' + '-'.center(108, '-'),
                              end='\n\n') if _ else ''
                        sleep(.5)
    sleep(.5)  # Sleep to give the player time to see what everyone has
    # Asks if the player would like insurence agenst a dealer's blackjack, checks if the dealer has a blackjack, goes to winer part if he does
    if any(card in dealer.hand for card in ['A(11)', '10', 'J(10)', 'Q(10)', 'K(10)']):
        while True:  # Asks if the player would like insurence agenst a dealer's blackjack
            player_input = input(
                f'Dealer: Would {"you" if number_of_players == 1 else "anyone"} like insurence agenst a Blackjack?\n\n[Y/N] :').casefold().strip()
            check_if_player_quits(player_input)
            if player_input == 'y':
                for n in range(number_of_players):
                    while True:
                        if player[n].blackjack:
                            print(
                                f'Dealer: {player[n].name}, you have a blackjack so you are protected.')
                            break
                        if number_of_players == 1:
                            while True:
                                player_input = input(
                                    f'Dealer: Just to confirm {player[n].name}, you want insurence for ${int(player[n].bet/2):,} correct?\n\n[Y/N] :').strip().casefold()
                                check_if_player_quits(player_input)
                                if player_input == 'y':
                                    player[n].insurence = True
                                    player[n +
                                                1].wallet -= int(player[n].bet/2)
                                    print(
                                        'Dealer: You are now insured agenst a Blackjack.')
                                    break
                                elif player_input == 'n':
                                    print('Dealer: Ok, good luck.')
                                    break
                                else:
                                    print('Dealer: I didn\'t get that.')
                            break
                        player_input = input(
                            f'Dealer: {player[n].name}, would you like some insurence? It will cost you ${int(player[n].bet/2):,}.\n\n[Y/N] :').strip().casefold()
                        check_if_player_quits(player_input)
                        if player_input == 'y':
                            player[n].insurence = True
                            player[n +
                                        1].wallet -= int(player[n].bet/2)
                            print('Dealer: You are now insured agenst a Blackjack.')
                            break
                        elif player_input == 'n':
                            print('Dealer: Ok, good luck.')
                            break
                        else:
                            print('Dealer: I didn\'t get that.')
                break
            if player_input == 'n':
                print('Dealer: Alright, good luck to everyone.')
                break
            else:
                print('Dealer: I didn\'t get that.')
        dealer_draw()
        if any(card in dealer.hand for card in ['A(11)']) and any(card in dealer.hand for card in ['10', 'J(10)', 'Q(10)', 'K(10)']):
            print(
                f'Dealer\'s cards: {dealer.hand[0]}, {dealer.hand[1]}')
            print('Dealer: Blackjack')
            dealer.blackjack = True
            for n in range(number_of_players):
                if player[n].insurence:
                    print(
                        f'Dealer: {player[n].name} pushed so you keep your bet.')
                    player[n].wallet += player[n].bet
                elif player[n].insurence:
                    print(
                        f'Dealer: {player[n].name} did have insurence so you get ${(player[n].bet+(player[n].bet/2)):,} back.')
                    player[n].wallet += player[n +
                                                         1].bet+(player[n].bet/2)
                else:
                    print(
                        f'Dealer: {player[n].name} did not have insurence so you lose your ${player[n].bet:,} bet.')
        else:
            print('Dealer: It is not a Blackjack.')
            determine_hand_value(dealer, dealer.hand)
            for n in range(number_of_players):
                if player[n].insurence:
                    print(
                        f'Dealer: Sorry {player[n].name} but you lose your insurence.')
    if dealer.blackjack == False:  # Player and dealer's turn
        print('Dealer: Now lets begin.')
        # Player's turn and everything a player does
        for n in range(number_of_players):
            for h in range(4):
                determine_hand_value(
                    dplayer[n], player[n].hand[h])
                if h == 3 and 'spl' in player[n].posible_moves:
                    player[n].posible_moves.remove('spl')
                if player[n].split == True or h == 0:
                    player[n].split = False
                    while True:
                        print(f'Dealer cards: {dealer.hand[0]}, ?')
                        print(f'{player[n].name} cards: {player[n].hand[h]} = {player[n].hand_value}{" (dobaling down)" if player[n].double_down[h] else ""}'.replace(
                            '[', '').replace('\'', '').replace(']', ''))
                        print(
                            f'Posible moves: {player[n].posible_moves}'.replace('\'', ''))
                        player_input = input(
                            f'\nYour move: ').strip().casefold()
                        check_if_player_quits(player_input)
                        if any(choice in player_input for choice in player[n].posible_moves):
                            if player_input == 'hel':  # PER
                                print_help()
                            elif player_input == 'hit':
                                player[n].hand[h].append(
                                    random.choice(dealer.deck))
                                dealer.deck.remove(
                                    player[n].hand[h][-1])
                                determine_hand_value(
                                    player[n], player[n].hand[h])
                                if 'dd' in player[n].posible_moves:
                                    player[n].posible_moves.remove('dd')
                                if 'spl' in player[n].posible_moves:
                                    player[n].posible_moves.remove('spl')
                                print(
                                    f'Dealer: {player[n].hand[h][-1]}, you are now at {player[n].hand_value}{" and that is a bust" if player[n].hand_value >21 else ""}.')
                                if player[n].hand_value > 21:
                                    break
                                else:
                                    pass
                            elif player_input == 'sta':
                                print(
                                    f'Dealer: Ok {player[n].name}, your score is {player[n].hand_value}.')
                                break
                            elif player_input == 'dd':
                                while True:
                                    player_input = input(
                                        f'Dealer: Just to confirm {player[n].name}, you want to bet ${player[n].bet:,} to duble down correct? [Y/N]:').strip().casefold()
                                    check_if_player_quits(
                                        player_input)
                                    if player_input == 'y':
                                        print(
                                            f'Dealer: Alright {player[n].name}, good luck on your bet.')
                                        player[n].posible_moves.remove(
                                            'dd')
                                        if 'spl' in player[n].posible_moves:
                                            player[n].posible_moves.remove(
                                                'spl')
                                        player[n].wallet -= player[n].bet
                                        player[n].double_down[h] == True
                                        break
                                    elif player_input == 'n':
                                        print(
                                            'Dealer: Ok, what would you like to do then?')
                                        break
                                    else:
                                        print('Dealer: I didn\'t get that.')
                            elif player_input == 'spl':
                                pass  # WIP
                            elif player_input == 'ttd':
                                while True:
                                    player_input = input(
                                        f'System: How much would you like to tip the dealer? [$0-${player[n].wallet}]: $')
                                    check_if_player_quits(
                                        player_input)
                                    if player_input.isnumeric() and int(player_input) == 0:
                                        break
                                    if player_input.isnumeric() and int(player_input) <= player[n].wallet:
                                        print(
                                            f'Dealer: What a pleasent suprise! Thank you for the tip {player[n].name}.')
                                        player[n].wallet -= int(
                                            player_input)
                                        break
                                    else:
                                        print(
                                            'System: Invalid input, try again.')
                                pass  # WIP
                            elif player_input == 'fft':
                                while True:
                                    player_input = input(
                                        'System: Are you sure you want to flip the table? [Y/N]:').strip().casefold()
                                    check_if_player_quits(
                                        player_input)
                                    if player_input == 'y':
                                        print('System: You flip the table.')
                                        print(
                                            f'Dealer: WHAT HAVE YOU DONE! SECURITY!!! ESCORE {player[n].name} OUT OF HERE!')
                                        print(
                                            f'System: {player[n].name} was escorted out of the casino. Since the table fliped, all bets are lost till the camera fotage is reviewed. Every one else levaes the casino.')
                                        print(
                                            '\n\n' + 'Game Over'.center(108, '-'), end='\n\n')
                                        quit()
                                    elif player_input == 'n':
                                        break
                                    else:
                                        print(
                                            'System: Invalid input, please try again.')
                            else:
                                print(
                                    'Dealer: That was not a valid move, try again.\n')
        print('Dealer: Now that everyone has gone, its my turn')
        while dealer.hand_value < 17:  # Dealer's turn
            print('Dealer\'s cards: ', end='')
            print(*dealer.hand, sep=', ', end='')
            print(f' = {dealer.hand_value}')
            dealer_draw()
            determine_hand_value(dealer, dealer.hand)
            if dealer.hand_value >= 17:
                print('Dealer\'s cards: ', end='')
                print(*dealer.hand, sep=', ', end='')
                print(f' = {dealer.hand_value}')
        for n in range(number_of_players):  # Determin the winer
            if dealer.hand_value > 21:
                for h in range(4):
                    determine_hand_value(
                        player[n], player[n].hand[h])
                    if player[n].blackjack:
                        print(f'{h} - {player[n].hand_value}')
                        print(
                            f'Dealer: Congradulations {player[n].name} on the Blackjack! You get ${player[n].bet*3.5:,} back!')
                        player[n].wallet += player[n].bet*3.5
                    elif player[n].hand_value != 0 and player[n].hand_value < 21:
                        print(f'{h} - {player[n].hand_value}')
                        print(
                            f'Dealer: {player[n].name}, congratulations, you get ${player[n].bet*2:,}{f" for hand {h+1}" if player[n].hand_value[1] != 0 else ""}', end='')
                        player[n].wallet += player[n].bet*2
                        if player[n].double_down[h]:
                            print(
                                f' and an extra {player[n].bet*2} for doubleing down.', end="")
                            player[n].wallet += player[n].bet*2
                        print('')
                    elif player[n].hand_value != 0 and player[n].hand_value > 21:
                        print(f'{h} - {player[n].hand_value}')
                        print(
                            f'Dealer: {player[n].name}, you get nothing for busting{f" hand {h+1}" if player[n].hand[1] != [] else ""}')
            else:
                for h in range(4):
                    determine_hand_value(
                        player[n], player[n].hand[h])
                    if player[n].hand_value != 0 and dealer.hand_value == player[n].hand_value:
                        print(f'{h} - {player[n].hand_value}')
                        print(
                            f'Dealer: {player[n].name} pushed so you get your ${player[n].bet} back{f" for hand {h+1}" if player[n].hand_value[1] != 0 else ""}.')
                    elif player[n].hand_value != 0 and player[n].hand_value < 21 and player[n].hand_value > dealer.hand_value:
                        print(f'{h} - {player[n].hand_value}')
                        print(
                            f'Dealer: {player[n].name}, congratulations, you get ${player[n].bet*2:,}{f" for hand {h+1}" if player[n].hand_value[1] != 0 else ""}', end='')
                        player[n].wallet += player[n].bet
                        if player[n].double_down[h]:
                            print(
                                f' and an extra {player[n].bet} for doubleing down.', end="")
                            player[n].wallet += player[n].bet
                        print('')
                    elif player[n].hand_value != 0 and player[n].hand_value < 21 and player[n].hand_value < dealer.hand_value:
                        print(f'{h} - {player[n].hand_value}')
                        print(
                            f'Dealer: {player[n].name}, you get nothing for being under {dealer.hand_value}.')
                    elif player[n].hand_value != 0 and player[n].hand_value > 21:
                        print(f'{h} - {player[n].hand_value}')
                        print(
                            f'Dealer: {player[n].name}, you get nothing for busting{f" hand {h+1}" if player[n].hand_value != 0 else ""}')
    for n in range(number_of_players):  # Resets player variables
        player[n].bet = 0
        player[n].skip = False
        player[n].posible_moves = []
        player[n].hit = False
        player[n].stay = False
        player[n].double_down[0] = False
        player[n].double_down[1] = False
        player[n].double_down[2] = False
        player[n].double_down[3] = False
        player[n].split = False
        player[n].insurence = False
        player[n].tip_the_dealer = False
        player[n].hand[0] = []
        player[n].hand[1] = []
        player[n].hand[2] = []
        player[n].hand[3] = []
        player[n].hand_value = 0
        player[n].blackjack = False
    # Resets dealer variables
    dealer.hand, dealer.hand_value, dealer.blackjack = [], 0, False
    # Checks if 35% or more of the deck was played and re-shuffles
    if len(dealer.deck) <= (len((list(dealer.deck_of_cards)*4*deck_size)))*0.65:
        dealer.deck = list(dealer.deck_of_cards)*4*deck_size
        random.shuffle(dealer.deck)
        print('* Dealer shuffled the deck *')

if gamble_mode:
    print(f'Dealer: And with that we end our game. Here are the final scores: {player[0].name}: ${player[0].wallet:,} {f"{nl}{player[1].name} ${player[1].wallet:,}" if int(number_of_players) >= 2 else ""} {f"{nl}{player[2].name} ${player[2].wallet:,}" if int(number_of_players) >= 3 else ""} {f"{nl}{player[3].name} ${player[3].wallet:,}" if int(number_of_players) >= 4 else ""} {f"{nl}{player[5].name} ${player[5].wallet:,}" if int(number_of_players) >= 5 else ""} {f"{nl}{player[6].name} ${player[6].wallet:,}" if int(number_of_players) >= 6 else ""} {f"{nl}{player[7].name} ${player[7].wallet:,}" if int(number_of_players) >= 7 else ""}')

print('Dealer: Thanks for playing and I hope to see you soon.')

print('\n\n' + 'End'.center(107, '-'), end='\n\n')
