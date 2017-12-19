"""
Implementation of the Main-van Dongen strategy - pays taxes, allows days off,
gives christmas presents and always sends elves to the forest - except on the
last day, when the ungrateful little buggers go to the mountain to die. Always
invests heavily in new elves. Some elves were whipped in the making of this
script.
"""

from sim_game import Game

class MainVD:
    def play(self, game):
        if game.day == game.days - 1:
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
