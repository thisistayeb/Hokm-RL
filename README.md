# Hokm-RL
Two-player **Hokm or Court piece** model for Reinforcement learning 


# Gameplay: How does it work?

In a two-player version of hokm, each player receives 13 cards after shuffling a 52-card deck, so half of the deck is thrown out. The first player chooses the trump suit from the first five cards in the deck without knowing any other information about the deck. A second player can pick a card with the same suit as the first player's card, if there is no card with the same suit, any card could be acceptable.
Using this class, the second player cannot play an illegal card, and all rules are mandatory. After the second player plays his card, the sub-game will be finished, the used cards will be inactive, and the Agent should start the next sub-game.
When all 13 sub-games have been completed, the game will be finished. "Done" indicates that all the sub-games have been completed.

