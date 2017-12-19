"""
Mountain-favouring variant of the Main-van Dongen strategy - parametrised by a
ratio of elves to send to the moutnain when available.
"""

from sim_game import Game

class MtnDew:
    def __init__(self, rat):
        self.mtn_ratio = rat

    def play(self, game):
        if not game.mtn_open:
            return 0, game.elves, 0
        else:
            if game.day == game.days - 1:
                return 0, 0, game.elves
            m_elves = int(game.elves * self.mtn_ratio)
            return 0, game.elves - m_elves, m_elves

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
    game = Game(MtnDew(0.2), verbose=True)
    print("money made: {}".format(game.money))
