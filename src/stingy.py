"""
Stingy variant of the Main-van Dongen strategy - doesn't buy elves the second
time round.
"""

from sim_game import Game

class Stingy:
    def play(self, game):
        if game.day == game.days - 1:
            return 0, 0, game.elves
        return 0, game.elves, 0

    def lottery(self, game):
        return 7

    def strike(self, game):
        return True

    def elf_hire(self, game):
        if game.days - game.day < 10:
            return 0
        return game.money // 75

    def tax_man(self, game):
        return True

    def xmas_eve(self, game):
        return True

if __name__ == "__main__":
    game = Game(Stingy(), verbose=True)
    print("money made: {}".format(game.money))
