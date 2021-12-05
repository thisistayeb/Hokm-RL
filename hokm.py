import numpy as np

def compare(first_card, second_card,  trump_suit):
    """  In every sub-game, firstplayer (agent) deliberately choose the card,
    then second player (player) should choose their card.
    In first sub-game, last round winner choose the TRUMP SUIT.

    This function gets First player's card and Second player's card and trump suit.
    If the fist player's card wins the second player's card, the result is True,
    otherwise False
    
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


def legitimate_card(card, facing_card,  trump_suit, player_cards):
    """  The function return 1 if the second player's card is legitimate'
        Otherwise return 0.
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

    """ Every Card has a value between "2,3,4,5,6,7,8,9,10,J,Q,K,Ace"
        and hase a suits, this class represents each card.
    """

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Hokm_game():
    
    """ In two-player hokm, after shuffling 52-card deck, each player gets 13 random cards.
    so half of the deck is out of game, 
    This class first generate each player's cards, then Agent in first sub-game should choose 
    the trump suit (the  defult value for trump suit is *diamonds*), the trump suit wouldn'the
    change during all 13 stage of the game.

    The second player should choose the second card, accroding to the rules.
    In situations where the second player's card is illegal, the code return an error but
    the second player can choose another card.

    After the second-player plays their card, the sub-game will be finished, the used card can be use again,
    and the Agent should play another card to start next sub-game.

    after the 13 sub-games, the game will be finished. "done" indicates that the all sub-games finished.

    at every level of the game, it's possible to access:
    all sub-games that first player wins by *agent_wins
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
        self.agent_card = None
        self.agent_decided = False
        self.trump_suit = "diamonds"

        
    def agent_action(self, card, *trump_suit):
        if self.stage == 1:
            self.trump_suit = trump_suit[0]
        if not(self.done):
            self.agent_card = card
            self.agent_decided = True
        
    
    def player_action(self, card):
        assert len(self.player_cards) == len(self.agent_cards)
        if self.done:
            pass
        elif not(self.agent_decided):
            print("Agent should choose card first")
        
        elif not(legitimate_card(card, self.agent_card, self.trump_suit, self.player_cards)):
            print("You can't play this card!")
        
        else:
            
            self.player_card = card

            if compare(self.agent_card, self.player_card, self.trump_suit):
                print("[Agent Wins]")
                self.agent_wins += 1
                
            else:
                print("[Player Wins]")
                self.player_wins += 1

            self.stage += 1
            
            

            self.agent_cards = np.delete(self.agent_cards, np.where(self.agent_cards == self.agent_card))
            self.player_cards = np.delete(self.player_cards, np.where(self.player_cards == self.player_card))

        if self.stage == 13:
            self.done = True