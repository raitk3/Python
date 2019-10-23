"""Golf solitaire."""
from itertools import zip_longest
from textwrap import dedent
import os

from cards1 import Deck


class Solitaire:
    """
    Solitaire class representing a game of Golf Solitaire.

    This game has 7 columns and 5 cards in each column,
    but the methods should work with other valid values as well.
    """

    columns = 7
    cards_in_column = 5

    def __init__(self):
        """
        Constructor, do the setup here.

        After setup with Solitaire.columns = 7, Solitaire.cards_in_column = 5
        You should have:
        self.tableau -> 7 columns of cards with 5 cards in each column
        self.stock -> 16 cards
        self.waste -> 1 card
        """
        self.deck = Deck(symbols=True)  # -> Deck instance
        self.tableau = []  # -> list of (columns[lists] (where each list -> cards_in_column * Card instances))
        self.waste = []  # -> list of Card instances
        self.stock = []  # -> list of Card instances
        self.start_game()

    def start_game(self):
        """Generate table."""
        self.deck.shuffle_deck()
        if len(self.deck.cards) > 0:
            self.waste.append(self.deck.deal_card())
            self.stock.append(self.deck.deal_card())
        for i in range(self.columns):
            self.tableau.append([])
        for _ in range(self.cards_in_column):
            for i in range(self.columns):
                if len(self.deck.cards) > 0:
                    self.tableau[i].append(self.deck.deal_card())
        for _ in range(len(self.deck.cards)):
            if len(self.deck.cards) > 0:
                self.stock.append(self.deck.deal_card())

    def can_move(self, card) -> bool:
        """
        Validate if a card from the tableau can be moved to the waste pile.

        The card must be last in the column list and adjacent by rank
        to the topmost card of the waste pile (last in waste list).
        Example: 8 is adjacent to 7 and 9. Ace is only adjacent to 2.
        King is only adjacent to Queen.
        """
        if len(self.tableau) > 0:
            for column in self.tableau:
                if len(column) > 0 and card == column[-1] and \
                        ((card.rank - 1) == self.waste[-1].rank or (card.rank + 1 == self.waste[-1].rank)):
                    return True
        return False

    def move_card(self, col: int):
        """
        Move a card from the tableau to the waste pile.

        Does not validate the move.
        :param col: index of column
        """
        self.waste.append(self.tableau[col].pop(-1))

    def deal_from_stock(self):
        """
        Deal last card from stock pile to the waste pile.

        If the stock is empty, do nothing.
        """
        if len(self.stock) > 0:
            self.waste.append(self.stock.pop(-1))

    def has_won(self) -> bool:
        """Check for the winning position - no cards left in tableau."""
        for el in self.tableau:
            if len(el) > 0:
                return False
        return True

    def has_lost(self) -> bool:
        """
        Check for the losing position.

        Losing position: no cards left in stock and no possible moves.
        """
        if len(self.stock) == 0:
            for i in range(self.columns):
                if len(self.tableau[i]) > 0 and self.can_move(self.tableau[i][-1]):
                    return False
            return True
        return False

    def print_game(self):
        """
        Print the game.

        Assumes:
        Card(decorated=True) by default it is already set to True
        self.tableau -> a list of lists (each list represents a column of cards)
        self.stock -> a list of Card objects that are in the stock
        self.waste_pile -> a list of Card objects that are in the waste pile

        You may modify/write your own print_game.
        """
        number_of_columns = [str(i).center(3, " ") for i in range(self.columns)]
        print(f" {'   '.join(number_of_columns)}")
        print('-' * (6 * self.columns - 1))
        print("\n".join([(" ".join((map(str, x)))) for x in (zip_longest(*self.tableau, fillvalue="     "))]))
        print()
        print(f"Kaarte pakis: {len(self.stock)} kaart{'i' if len(self.stock) != 1 else ''}")
        print(f"Viimane maha pandud kaart: {self.waste[-1] if self.waste else 'Empty'}")

    @staticmethod
    def rules():
        """Print the rules of the game."""
        print("Reeglid".center(40, "-"))
        print(dedent(f"(Eesmärk: Saada kaardid mängulaualt maha.\n"
                     f"\n"
                     f"Kaarti saab maha panna, kui kaart on 1 võrra suurem\n"
                     f"või väiksem viimasest käidud kaardist. Mast ei ole oluline.\n"
                     f"Maha saab panna vaid iga tulba kõige alumist kaarti.\n"
                     f"\n"
                     f"Alati saab pakist panna 1 kaardi maha.\n"
                     f"Mäng on kaotatud kui pakist on kõik kaardid otsas\n"
                     f"ning ühtegi käiku ei saa enam sooritada.\n"
                     f"Mäng on võidetud kui mängulaud on tühi.\n"
                     f"\n"
                     f"Käsud:\n"
                     f"(0-{Solitaire.columns - 1}) - Tulba number, kust soovid alumist kaarti maha panna.\n"
                     f"(d) - Pane 1 kaart pakist maha.\n"
                     f"(r) - Näita reegleid.\n"
                     f"(q) - Loobu."))

    def check_if_lost_won(self):
        """Check if won."""
        if self.has_won():
            print("ʕ♥ᴥ♥ʔ Sa võitsid!")
            return True
        if self.has_lost():
            print("(╥﹏╥) Sa kaotasid!")
            return True

    def play(self):
        """
        Play a game of Golf Solitaire.

        Create the game loop here.
        Use input() for player input.
        Available commands are described in rules().
        """
        self.print_game()
        next_move = input("(ʘ‿ʘ)╯ Tere tulemast mängima Golf Solitaire'i!\nMillist käiku soovite teha?")
        while True:
            if next_move.lower() == "q":
                print("ʕ♥ᴥ♥ʔ Tänan, et mängisite seda mängu!")
                break
            elif next_move.lower() == "r":
                self.rules()
                self.print_game()
                next_move = input("(ʘ‿ʘ) Milline on teie järgmine käik?")
            elif next_move.lower() == "d":
                self.deal_from_stock()
                self.print_game()
                if self.check_if_lost_won():
                    break
                next_move = input("(ʘ‿ʘ) Milline on teie järgmine käik?")
            elif next_move.isnumeric() and 0 <= int(next_move) < self.columns:
                if len(self.tableau[int(next_move)]) < 1:
                    next_move = input("( ｡_｡) See tulp on juba tühi!")
                else:
                    card_to_play = self.tableau[int(next_move)][-1]
                    if self.can_move(card_to_play):
                        self.move_card(int(next_move))
                        self.print_game()
                        if self.check_if_lost_won():
                            break
                        next_move = input("(ʘ‿ʘ) Milline on teie järgmine käik?")
                    else:
                        next_move = input("(ಠ_ಠ) Seda kaarti ei saa käia!")
            else:
                next_move = input("(◎.◎) Ei oska midagi teha...\nSisesta palun sobiv käsk!\n"
                                  "Reeglite kuvamiseks sisestage 'r'.")


if __name__ == '__main__':
    s = Solitaire()
    s.play()
