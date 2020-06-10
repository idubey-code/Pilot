import random
from IPython.display import clear_output

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = None
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        return f'{list(map(str,self.deck))}'

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        self.shuffle()
        return self.deck.pop()
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces+=1
        
    def adjust_for_ace(self):
    # If value becomes more than 21 and we have aces, value of aces can be adjusted to 1 from 11 and we can continue playing
        if self.value > 21 and self.aces > 1:
            self.value -= 10
            self.aces -= 1
            
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('\nEnter your bet amount: '))
            if chips.bet > chips.total:
                print(f'\nNot enough chips. Please re-enter (Total Chips = {chips.total} )\n')
                continue
            else:
                break
        except:
            print('\nPlease enter a valid amount.')
            continue
            
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        try:
            choice = int(input('\nHit or Stand ? (Press 1 -> Hit, Press 0 -> Stand) : '))
            if choice in [0,1]:
                break
            else:
                raise Exception
        except:
            print('\nPlease make a valid selection')
            continue
    if choice == 1:
        hit(deck,hand)
    elif choice == 0:
        print('\nPlayer Stands. Dealer is playing.')
        playing = False
        
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <Hidden Card> ",end=' | ')
    print(f" {dealer.cards[1]}")
    print("\nPlayer's Hand:")
    print(*player.cards,sep=' | ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:")
    print(*dealer.cards,sep=" | ")
    print("\nPlayer's Hand:")
    print(*player.cards,sep=" | ")
    print(f"\nDealer's Value: {dealer.value}")
    print(f"\nPlayer's Value: {player.value}")
    
def player_busts(player,dealer,chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("\nPlayer won!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nDealer busts!")
    chips.lose_bet()
    
def dealer_wins(player,dealer,chips):
    print("\nDealer won!")
    chips.win_bet()
    
def push(player,dealer):
    print("\nDealer and Player tie. It's a push!")
    
while True:
    # Print an opening statement
    clear_output()
    print(" * Welcome. We will now be playing Black Jack!")
    print(" * Get as close to 21 as you can without going over!")
    print(" * Dealer hits until she reaches 17. Aces count as 1 or 11.")
    
    # Create & shuffle the deck, deal two cards to each player
    deck=Deck()
    player=Hand()
    dealer=Hand()
    for i in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)

    
    while playing: # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player,dealer,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        while dealer.value < 17:
            hit(deck,dealer)

        # Show all cards
        show_all(player,dealer)

        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player,dealer,player_chips)

        elif dealer.value > player.value:
            dealer_wins(player,dealer,player_chips)

        elif dealer.value < player.value:
            player_wins(player,dealer,player_chips)

        else:
            push(player,dealer)
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("\nDo you want to play again ? Enter y or n: ")
    if new_game[0].lower() == 'y':
        playing=True
        continue
    else:
        print('\nThank you for playing.')
        break
