"""
OOP simulating an elf game, as per LWB 18/12
"""

from random import random, randrange
from collections import deque
from enum import Enum

class Events(Enum):
    STRIKE   = 0
    MTN_OPEN = 1
    ELF_HIRE = 2
    TAX_MAN  = 3
    XMAS_EVE = 4
    LOTTERY  = 5

SCHEDULE = { 6: Events.LOTTERY,
             8: Events.STRIKE,
            11: Events.MTN_OPEN,
            12: Events.ELF_HIRE,
            13: Events.LOTTERY,
            14: Events.TAX_MAN,
            15: Events.STRIKE,
            17: Events.ELF_HIRE,
            18: Events.LOTTERY,
            20: Events.TAX_MAN,
            23: Events.LOTTERY,
            25: Events.XMAS_EVE}

class GameFoul(Exception):
    pass

class GameEnd(Exception):
    pass

class Game:
    def __init__(self, handler, *, starting_elves=12, days=25, sched=SCHEDULE, verbose=False):
        self.day = 0
        self.money = 0
        self.elves = starting_elves
        self.days = days
        self.sched = sched
        self.verb = verbose
        self.striking = 0
        self.mtn_open = False
        self.handler = handler
        self.extra_tax = 0
        deque(iter(self.play, 1), maxlen=0)

    def play(self):
        self.day += 1
        self.verb and print("\nday {}".format(self.day))
        if self.day in self.sched:
            self.extra_meths[self.sched[self.day]](self)
        if self.day >= self.days:
            self.verb and print("last day")
            return 1
        if not self.striking:
            woods, forest, mountain = self.handler.play(self)
            self.verb and print("woods: {}, forest: {}, mountain: {}".format(woods, forest, mountain))
            self.money += woods * 10
            roll = randrange(1, 7)
            if roll >= 5:
                self.elves -= mountain
                self.verb and print("it's a blizzard, the {} elves on the mountain died gruesomely and you only made £{}".format(mountain, woods * 10))
            else:
                self.money += forest * 20 + mountain * 50
                self.verb and print("no blizzard: made £{}".format(woods * 10 + forest * 20 + mountain * 50))
        else:
            self.verb and print("elves are on strike")
            self.striking -= 1
        if self.extra_tax:
            self.verb and print("paid £{} in tax".format(-((-self.money * self.extra_tax) // 100)))
            self.money = self.money * (100 - self.extra_tax) // 100
            self.extra_tax = 0
        self.verb and print("left with £{} and {} elves".format(self.money, self.elves))

    def lottery(self):
        guess = self.handler.lottery(self)
        if guess == randrange(1, 7) + randrange(1, 7):
            self.money += 10
            self.verb and print("you won £{} at the lottery".format(10))
        else:
            self.verb and print("you won nothing at the lottery")

    def strike(self):
        allow = self.handler.strike(self)
        if allow:
            self.striking = 1
            self.verb and print("you let the elves have a day off")
        elif random() < 0.5:
            self.striking = 2
            self.verb and print("your elves decided to go on strike")
        else:
            self.verb and print("you elves didn't go on strike but your lack of ethical capitalism has given you nightmares")

    def mountain(self):
        self.mtn_open = True
        self.verb and print("the mountain pass has opened")

    def elf_hire(self):
        elves = self.handler.elf_hire(self)
        self.elves += elves
        self.money -= elves * 75
        self.verb and print("hired {} elves at an expense of £{}".format(elves, elves * 75))

    def tax_man(self):
        pay = self.handler.tax_man(self)
        if pay:
            self.verb and print("obediently paid {} in tax".format(-((-self.money) // 10)))
            self.money = self.money * 9 // 10
        elif random() < 0.5:
            self.extra_tax = 20
            self.verb and print("you'll have to pay 20% tax later")
        else:
            self.verb and print("not paying tax and got away with it what are you facebook")

    def xmas_eve(self):
        pay = self.handler.xmas_eve(self)
        if pay:
            self.money -= self.elves * 50
            self.verb and print("you paid your elves £{} on xmas eve".format(self.elves * 50))
        elif random() < 0.5:
            self.money -= self.elves * 150
            self.verb and print("you didn't pay your elves and they stole a total of £{}".format(self.elves * 150))
        else:
            self.verb and print("you, the grinch, didn't pay your elves anything. bah humbug")

    extra_meths = {
            Events.LOTTERY:  lottery,
            Events.STRIKE:   strike,
            Events.MTN_OPEN: mountain,
            Events.ELF_HIRE: elf_hire,
            Events.TAX_MAN:  tax_man,
            Events.XMAS_EVE: xmas_eve}
