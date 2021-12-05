import numpy as np

def compare(first_card, second_card,  trump_suit):
    """
    This function returns the result of the sub-game based on the suit of the trump card in each stage.
    The result is 1 if player one wins, otherwise 0.
    """

    assert trump_suit in ["spades", "clubs", "hearts", "diamonds"]
    assert first_card.value in range(2,15)
    assert second_card.value in range(2,15)
    
    if first_card.suit == second_card.suit:

        assert first_card.value != second_card.value
        if first_card.value > second_card.value:

            return True

        else:

            return False
     
    else:
        if first_card.suit ==  trump_suit and second_card.suit !=  trump_suit:
            return True
        
        else:
            return False


def legitimate_card(card, facing_card, trump_suit, player_cards):
    """  It returns 1 if player two's card is legitimate based on player one's card,
         the trump suit, and all cards in player two's deck.
    """
    
    if card.suit == facing_card.suit:
        return 1
    
    elif card.suit ==  trump_suit:
        return 1

    else:

        all_possible_suits = [i.suit for i in player_cards]
        if facing_card.suit in all_possible_suits or\
               trump_suit in all_possible_suits:
            return 0

        else:
            return 1
    

class Card:

    """ Each Card has a value between "2,3,4,5,6,7,8,9,10,J,Q,K,Ace" and a suit.
        This class represents each card by this two characteristics.
    """

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Hokm_game():
    
    """ 
    First Player => Agent
    Second Player => Player

    The class initiates the first five cards for the first player and 13 cards for each player. 
    `first_five_cards` provides access to the first five cards.

    13-cards deck for both players are accessible by `agent_cards`, `player_cards`.

    In the first stage, player one chooses a trump suit based on the first five cards. After this, the value `trump_suit_decided` is True.

    The sub-game will end after the second player chooses the eligible card, and the first player should begin a new one until the last (13th) sub-game is played.
    """

    done = False
    agent_wins, player_wins = 0,0
    suits = ["spades", "clubs", "hearts", "diamonds"]
    cards = np.concatenate(([[Card(value, suit) for value in np.arange(2,15)] for suit in suits]))    
    cards = np.random.choice(cards, len(cards)//2, replace=False)

    def __init__(self):
    
        self.stage = 1
        self.player_cards = self.cards[len(self.cards)//2:]
        self.agent_cards = self.cards[:len(self.cards)//2]
        self.first_five_cards =self.agent_cards[:5]
        self.agent_card = None
        self.agent_decided = False
        self.trump_suit_decided = False


    def trump_suit(self, suit):

        if self.stage == 1:
            self.trump_suit = suit
            self.trump_suit_decided = True

        
    def agent_action(self, card):

        if not(self.trump_suit_decided):
            print("Trump Suit should be chosen first")

        elif not(self.done):
            self.agent_card = card
            self.agent_decided = True
        
    
    def player_action(self, card):

        assert len(self.player_cards) == len(self.agent_cards)

        if not(self.agent_decided):
            print("The agent should choose the card first")
        
        elif not(legitimate_card(card, self.agent_card, self.trump_suit, self.player_cards)):
            print("This card is not playable.")
        
        if not(self.done):
            
            self.player_card = card

            if compare(self.agent_card, self.player_card, self.trump_suit):
                self.agent_wins += 1
                
            else:
                self.player_wins += 1

            self.stage += 1
            
            
            self.agent_decided = False
            self.agent_cards = np.delete(self.agent_cards, np.where(self.agent_cards == self.agent_card))
            self.player_cards = np.delete(self.player_cards, np.where(self.player_cards == self.player_card))

        if self.stage == 13:
            self.done = True