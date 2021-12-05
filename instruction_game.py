from hokm import Hokm_game
import numpy as np

#make a new single game
NewGame = Hokm_game()

#Play until all sub-games are completed
while NewGame.done == False:

    if NewGame.stage == 1:

        # First player should choose the trump suit based on the first five cards.
        # Let's pick the suit of the first card as an example!
        NewGame.trump_suit(NewGame.first_five_cards[0].suit)



    # In the next sub-game, it doesn't matter if you choose the trump suit or not.
    # example:
    # NewGame.agent_action(THE_FIRST_CARD, TRUMP_SUIT)

    NewGame.agent_action(np.random.choice(NewGame.agent_cards))

    # After that, the player chooses a card
    NewGame.player_action(np.random.choice(NewGame.player_cards))

    # It's possible to see the results of sub-games, as well as all the data associated with the games
    print(NewGame.player_wins, NewGame.agent_wins)
