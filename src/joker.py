"""
Stochastic of the Main-van Dongen strategy (randomly decides whether or not to
send elves to the mountain, and how many)
"""

from random import randrange, random

from sim_game import Game

class Joker:
    def play(self, game):
        if game.day == game.days - 1:
            return 0, 0, game.elves
        elif random() < 0.5:
            m_elves = randrange(game.elves)
            return 0, game.elves - m_elves, m_elves
        return 0, game.elves, 0

    def lottery(self, game):
        return 7

    def strike(self, game):
        return True

    def elf_hire(self, game):
        return game.money // 75

    def tax_man(self, game):
        return True

    def xmas_eve(self, game):
        return True

if __name__ == "__main__":
    game = Game(Joker(), verbose=True)
    print("money made: {}".format(game.money))
