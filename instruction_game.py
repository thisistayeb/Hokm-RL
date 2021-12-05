from hokm import Hokm_game
import numpy as np

#Creat a single game
NewGame = Hokm_game()

#continue game until sub-games finished
while NewGame.done == False:
    """
    in first stage first_player could choose the *Trump Suit*
    choose the trump suit and the first card at same time.
    in next sub-game,it donesn't matter if choosing the trump suit or not, Nothing happens.
    example:
    NewGame.agent_action(THE_FIRST_CARD, TRUMP_SUIT)
    """
    NewGame.agent_action(np.random.choice(NewGame.agent_cards), "hearts")


    """
    Then Player chooses their card
    """
    NewGame.player_action(np.random.choice(NewGame.player_cards))

    # It's possible to see the result of sub-games, and all the date in games
    print(NewGame.player_wins, NewGame.agent_wins)
