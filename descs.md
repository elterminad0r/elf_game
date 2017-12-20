Strategy filename | Strategy description
---|---
src/clegane.py | Variant of the Main-van Dongen strategy that takes the Gregor Clegane approach - displays no ethics and is a big fan of mountains
src/joker.py | Stochastic variant of the Main-van Dongen strategy (randomly decides whether or not to send elves to the mountain, and how many, using a uniform distribution between 0 and the number of elves).
src/libertarian.py | Libertarian variant of Main-van Dongen strategy (doesn't pay taxes).
src/main\_vd.py | Implementation of the Main-van Dongen strategy - pays taxes, allows days off, gives christmas presents and always sends elves to the forest - except on the last (n) days, when the ungrateful little buggers go to the mountain to die.<br>N here is what mvd is parametrised by - originally this was 1, but `shrewd` uses the value 6, as `shrews` uses a different heuristic for elf value - which is earning power. 6 is obtained by solving:<br>40 / 3 < (200 - (40 / 3)(r + 2)) / 6 to get r < 7 => the maximum profit is found at r = 6. This has been experimentally confirmed.<br>Always invests heavily in new elves.  Some elves were whipped in the making of this script.
src/mtn\_dew.py | Mountain-favouring variant of the Main-van Dongen strategy - parametrised by a ratio of elves to send to the moutnain when available. NB that `mtn_dew` uses the ratio 1 / 5, `half_mountain` is a duplicate using the ratio 1 / 2, and `jefferson` uses the ratio 1.
src/stingy.py | Stingy variant of the Main-van Dongen strategy - doesn't buy elves the second time round.
src/twoface.py | Even more stochastic of the Main-van Dongen strategy (tosses a coin for each boolean decision), and even randomly guesses for the lottery
src/unethical.py | Unethical variant of Main-van Dongen strategy - doesn't allow days off, no christmas presents and doesn't pay tax.
src/woody.py | Variation of the Main-van Dongen strategy that always sends elves into woods. Lives a boring but peaceful life and knows all its elves by name.
