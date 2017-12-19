"""
Shrewd optimisation of the Main-van Dongen strategy, which starts sending elves
to the mountain a little earlier. Here, the "worth" of an elf is not calculated by
the actual cost but by time remaining.
The magic number 6 is calculated by solving
40 / 3 < (200 - (40 / 3)(r + 2)) / 6
to get r < 7 => the maximum profit is found at r = 6
experimentally confirmed
"""

from sim_game import Game

class Shrewd:
    def play(self, game):
        if game.days - game.day < 6:
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
    game = Game(Shrewd(), verbose=True)
    print("money made: {}".format(game.money))
