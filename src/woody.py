"""
Variation of the Main-van Dongen strategy that always sends elves into woods.
Lives a boring but peaceful life and knows all its elves by name.
"""

from sim_game import Game

class Woody:
    def play(self, game):
        if game.day == game.days - 1:
            return 0, 0, game.elves
        return game.elves, 0, 0

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
    game = Game(Woody(), verbose=True)
    print("money made: {}".format(game.money))
