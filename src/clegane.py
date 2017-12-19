"""
Variant of the Main-van Dongen strategy that takes the Gregor Clegane approach
- displays no ethics and is a big fan of mountains
"""

from sim_game import Game

class Clegane:
    def play(self, game):
        if game.mtn_open:
            return 0, 0, game.elves
        return 0, game.elves, 0

    def lottery(self, game):
        return 7

    def strike(self, game):
        return False

    def elf_hire(self, game):
        return game.money // 75

    def tax_man(self, game):
        return False

    def xmas_eve(self, game):
        return False

if __name__ == "__main__":
    game = Game(Clegane(), verbose=True)
    print("money made: {}".format(game.money))
