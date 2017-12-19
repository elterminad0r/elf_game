"""
Even more stochastic of the Main-van Dongen strategy (tosses a coin for each
boolean decision), and even randomly guesses for the lottery
"""

from random import randrange, random

from sim_game import Game

class TwoFace:
    def play(self, game):
        if game.day == game.days - 1:
            return 0, 0, game.elves
        elif random() < 0.5:
            m_elves = randrange(game.elves)
            return 0, game.elves - m_elves, m_elves
        return 0, game.elves, 0

    def lottery(self, game):
        return randrange(2, 13)

    def strike(self, game):
        return random() < 0.5

    def elf_hire(self, game):
        return randrange(game.money // 75 + 1)

    def tax_man(self, game):
        return random() < 0.5

    def xmas_eve(self, game):
        return random() < 0.5

if __name__ == "__main__":
    game = Game(TwoFace(), verbose=True)
    print("money made: {}".format(game.money))
