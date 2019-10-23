"""Simple game of blackjack."""
from textwrap import dedent

import requests


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str):
        """Card properties."""
        self.suit = suit
        self.value = value
        self.code = code

    def __repr__(self):
        """Represent card."""
        return self.code


class Hand:
    """Simple class for holding hand information."""

    def __init__(self):
        """Create hand."""
        self.score = 0
        self.cards = []
        self.ac_used = False
        self.ad_used = False
        self.ah_used = False
        self.as_used = False

    def add_card(self, card: Card):
        """Add new card."""
        self.cards.append(card)
        if card.value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            self.score += int(card.value)
        if card.value in ['JACK', 'QUEEN', 'KING']:
            self.score += 10
        if card.value == "ACE":
            self.score += 11
        while self.score > 21:
            for card in self.cards:
                if card.code == "AS" and not self.as_used:
                    self.score -= 10
                    self.as_used = True
                    break
                elif card.code == "AD" and not self.ad_used:
                    self.score -= 10
                    self.ad_used = True
                    break
                elif card.code == "AC" and not self.ac_used:
                    self.score -= 10
                    self.ac_used = True
                    break
                elif card.code == "AH" and not self.ah_used:
                    self.score -= 10
                    self.ah_used = True
                    break
            break


class Deck:
    """Class for holding deck information."""

    def __init__(self, shuffle=False):
        """
        Tell api to create a new deck.

        :param shuffle: if shuffle option is true, make new shuffled deck.
        """
        if not shuffle:
            deck = requests.get("https://deckofcardsapi.com/api/deck/new").json()
        else:
            deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle").json()
        self.id = deck["deck_id"]
        self.is_shuffled = deck["shuffled"]

    def shuffle(self):
        """Shuffle the deck."""
        deck = requests.get(f"https://deckofcardsapi.com/api/deck/{self.id}/shuffle").json()
        self.is_shuffled = deck["shuffled"]

    def draw(self) -> Card:
        """
        Draw card from the deck.

        :return: card instance.
        """
        card = requests.get(f"https://deckofcardsapi.com/api/deck/{self.id}/draw").json()
        return Card(card["cards"][0]["value"], card["cards"][0]["suit"], card["cards"][0]["code"])


class BlackjackController:
    """Blackjack controller. For controlling the game and data flow between view and database."""

    def __init__(self, deck: Deck, view: 'BlackjackView'):
        """
        Start new blackjack game.

        :param deck: deck to draw cards from.
        :param view: view to communicate with.
        """
        self.deck = deck
        if not self.deck.is_shuffled:
            deck.shuffle()
        self.view = view
        self.dealer = Hand()
        self.player = Hand()
        self.state = {"dealer": self.dealer, "player": self.player}

        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())
        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())

        while True:
            if self.player.score > 21:
                self.view.player_lost(self.state)
                return
            if self.player.score == 21:
                self.view.player_won(self.state)
                return
            action = self.view.ask_next_move(self.state)
            if action == "S":
                break
            if action == "H":
                self.player.add_card(self.deck.draw())

        while True:
            if self.dealer.score > 21:
                self.view.player_won(self.state)
                return
            if self.dealer.score > self.player.score:
                self.view.player_lost(self.state)
                return
            self.dealer.add_card(self.deck.draw())


class BlackjackView:
    """Minimalistic UI/view for the blackjack game."""

    def ask_next_move(self, state: dict) -> str:
        """
        Get next move from the player.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :return: parsed command that user has choses. String "H" for hit and "S" for stand
        """
        self.display_state(state)
        while True:
            action = input("Choose your next move hit(H) or stand(S) > ")
            if action.upper() in ["H", "S"]:
                return action.upper()
            print("Invalid command!")

    def player_lost(self, state):
        """
        Display player lost dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You lost")

    def player_won(self, state):
        """
        Display player won dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You won")

    def display_state(self, state, final=False):
        """
        Display state of the game for the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :param final: boolean if the given state is final state. True if game has been lost or won.
        """
        dealer_score = state["dealer"].score if final else "??"
        dealer_cards = state["dealer"].cards
        if not final:
            dealer_cards_hidden_last = [c.__repr__() for c in dealer_cards[:-1]] + ["??"]
            dealer_cards = f"[{','.join(dealer_cards_hidden_last)}]"

        player_score = state["player"].score
        player_cards = state["player"].cards
        print(dedent(
            f"""
            {"Dealer score":<15}: {dealer_score}
            {"Dealer hand":<15}: {dealer_cards}

            {"Your score":<15}: {player_score}
            {"Your hand":<15}: {player_cards}
            """
        ))


if __name__ == '__main__':
    BlackjackController(Deck(), BlackjackView())  # start the game.
