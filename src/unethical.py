"""
Unethical variant of Main-van Dongen strategy
"""

from sim_game import Game

class Unethical:
    def play(self, game):
        if game.day == game.days - 1:
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
    game = Game(Unethical(), verbose=True)
    print("money made: {}".format(game.money))
