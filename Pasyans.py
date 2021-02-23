import random


class Card:
    numstr_dict = {
        1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
        8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"
    }
    color_dict = {
        "Diamond": "Red",
        "Heart": "Red",
        "Club": "Black",
        "Spade": "Black"
    }

    def __init__(self, mark, number, side=False):
        self.mark = mark  # mark  : Diamond or Heart or Club or Spade
        self.number = number  # number: 1~13
        self.color = self.color_dict[mark]  # color : Red or Black
        self.numstr = self.numstr_dict[number]  # numstr: Ace~King
        self.side = side  # Front and Back: True=Front, False=Back

    def getData(self):
        return (self.mark, self.number, self.color, self.numstr, self.side)

    def getMAN(self):
        # Mark And Number
        man = self.mark[0] + "_" + str(self.number)
        if (self.number <= 9):
            man = self.mark[0] + "_" + "_" + str(self.number)
        return man


f = Card("Spade", 1)
print(f.getMAN())


class Deck:
    self.deck = []
    for mark in self.color:
        for number in self.numstr:
            self.Deck.append(mark, number)
            self.frontCard = None

    def get_shuffle(self):
        random.shuffle(self.deck)

    def get_Card(self):
        get_card = self.dec.pop([1])
        return get_card








