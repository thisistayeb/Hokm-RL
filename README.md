# Hokm-RL
A two-player **Hokm or Court piece** model for Reinforcement learning.



# Gameplay: How does it work?

In a two-player version of hokm, each player receives 13 cards after shuffling a 52-card deck, so half of the deck is thrown out. The first player chooses the trump suit from the first five cards in the deck without knowing any other information about the deck. A second player can pick a card with the same suit as the first player's card, if there is no card with the same suit, any card could be acceptable.
Using this class, the second player cannot play an illegal card, and all rules are mandatory. After the second player plays his card, the sub-game will be finished, the used cards will be inactive, and the Agent should start the next sub-game.
When all 13 sub-games have been completed, the game will be finished. "Done" indicates that all the sub-games have been completed.

# Value of Cards

The model uses a standard 52-card deck comprises 13 ranks in each of the four suits: clubs (♣), diamonds (♦), hearts (♥) and spades (♠).

In hokm, Ace is the most valuable card in the deck, and two is the lowest value card.

**Card**| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | J  | Q  | K  | Ace |
|---|---|---|---|---|---|---|---|---|----|----|----|----|-----|
**Numerical Value**| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14  |


**Trump Suit**:
During the first round of each game, the first player gets the first five cards and chooses the trump suit.
A trump card has more value than another card of a different suit.

