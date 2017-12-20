"""
Implementation of the Main-van Dongen strategy - pays taxes, allows days off,
gives christmas presents and always sends elves to the forest - except on the
last (n) days, when the ungrateful little buggers go to the mountain to die.

N here is what mvd is parametrised by - originally this was 1, but `shrewd`
uses the value 6, as `shrews` uses a different heuristic for elf value - which
is earning power. 6 is obtained by solving:

40 / 3 < (200 - (40 / 3)(r + 2)) / 6
to get r < 7 => the maximum profit is found at r = 6.
This has been experimentally confirmed.

Always invests heavily in new elves.  Some elves were whipped in the making of
this script.
"""

from sim_game import Game

class MainVD:
    def __init__(self, threshold):
        self.thresh = threshold

    def play(self, game):
        if game.day >= game.days - self.thresh:
            return 0, 0, game.elves
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
    game = Game(MainVD(), verbose=True)
    print("money made: {}".format(game.money))
