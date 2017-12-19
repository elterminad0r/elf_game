Typical data generation session:

    $ for i in mvd unethical libertarian mtn_dew half_mountain woody stingy early joker twoface shrewd; do echo "\n$i"; pypy stats.py --player $i -n 200000; done

    mvd
    collecting data for mvd
    intitialised at 0.000s
    (2.293s) progress:  99% ...................................................................................................
    done; completed 200000 games in 2.314s (that's 86448 games/s)
    sorting
    sorted
    serialising to 'datasets/mvd/200000-2017-12-19-15-35-58.dat'
    serialised
    average £4,957 ± £1,679 (variance £²2,820,216)
    min: £0; max: £11,850
    LQ: £3,765; median: £4,845; UQ: £6,001
    mode £5,289 occurred 0.536%
    sample size 200,000
    4,957 ± 1,679   2,820,216       0       3,765   4,845   6,001   11,850  5,289   0.5360  200,000

    unethical
    collecting data for unethical
    intitialised at 0.000s
    (2.413s) progress:  99% ...................................................................................................
    done; completed 200000 games in 2.432s (that's 82224 games/s)
    sorting
    sorted
    serialising to 'datasets/unethical/200000-2017-12-19-15-36-01.dat'
    serialised
    average £3,918 ± £3,865 (variance £²14,941,320)
    min: £-8,666; max: £19,440
    LQ: £220; median: £4,400; UQ: £6,732
    mode £35 occurred 0.286%
    sample size 200,000
    3,918 ± 3,865   14,941,320      -8,666  220     4,400   6,732   19,440  35      0.2860  200,000

    libertarian
    collecting data for libertarian
    intitialised at 0.000s
    (2.211s) progress:  99% ...................................................................................................
    done; completed 200000 games in 2.230s (that's 89686 games/s)
    sorting
    sorted
    serialising to 'datasets/libertarian/200000-2017-12-19-15-36-03.dat'
    serialised
    average £4,839 ± £1,668 (variance £²2,783,617)
    min: £0; max: £12,755
    LQ: £3,644; median: £4,725; UQ: £5,916
    mode £5,240 occurred 0.398%
    sample size 200,000
    4,839 ± 1,668   2,783,617       0       3,644   4,725   5,916   12,755  5,240   0.3980  200,000

    mtn_dew
    collecting data for mtn_dew
    intitialised at 0.000s
    (2.466s) progress:  99% ...................................................................................................
    done; completed 200000 games in 2.486s (that's 80435 games/s)
    sorting
    sorted
    serialising to 'datasets/mtn_dew/200000-2017-12-19-15-36-06.dat'
    serialised
    average £4,861 ± £2,624 (variance £²6,887,591)
    min: £0; max: £17,603
    LQ: £2,915; median: £4,391; UQ: £6,309
    mode £14,088 occurred 0.102%
    sample size 200,000
    4,861 ± 2,624   6,887,591       0       2,915   4,391   6,309   17,603  14,088  0.1015  200,000

    half_mountain
    collecting data for half_mountain
    intitialised at 0.000s
    (2.408s) progress:  99% ...................................................................................................
    done; completed 200000 games in 2.427s (that's 82397 games/s)
    sorting
    sorted
    serialising to 'datasets/half_mountain/200000-2017-12-19-15-36-09.dat'
    serialised
    average £4,324 ± £4,150 (variance £²17,223,173)
    min: £0; max: £30,036
    LQ: £1,428; median: £3,015; UQ: £5,809
    mode £23,487 occurred 0.095%
    sample size 200,000
    4,324 ± 4,150   17,223,173      0       1,428   3,015   5,809   30,036  23,487  0.0950  200,000

    woody
    collecting data for woody
    intitialised at 0.000s
    (2.290s) progress:  99% ...................................................................................................
    done; completed 200000 games in 2.311s (that's 86524 games/s)
    sorting
    sorted
    serialising to 'datasets/woody/200000-2017-12-19-15-36-11.dat'
    serialised
    average £2,831 ± £6 (variance £²42)
    min: £2,826; max: £2,861
    LQ: £2,826; median: £2,834; UQ: £2,835
    mode £2,826 occurred 48.227%
    sample size 200,000
    2,831 ± 6       42      2,826   2,826   2,834   2,835   2,861   2,826   48.2265 200,000

    stingy
    collecting data for stingy
    intitialised at 0.000s
    (2.201s) progress:  99% ...................................................................................................
    done; completed 200000 games in 2.221s (that's 90069 games/s)
    sorting
    sorted
    serialising to 'datasets/stingy/200000-2017-12-19-15-36-14.dat'
    serialised
    average £2,921 ± £451 (variance £²203,451)
    min: £808; max: £4,389
    LQ: £2,645; median: £2,925; UQ: £3,215
    mode £2,923 occurred 1.498%
    sample size 200,000
    2,921 ± 451     203,451 808     2,645   2,925   3,215   4,389   2,923   1.4980  200,000

    early
    collecting data for early
    intitialised at 0.000s
    (2.252s) progress:  99% ...................................................................................................
    done; completed 200000 games in 2.273s (that's 88005 games/s)
    sorting
    sorted
    serialising to 'datasets/early/200000-2017-12-19-15-36-16.dat'
    serialised
    average £4,474 ± £1,152 (variance £²1,328,250)
    min: £36; max: £8,922
    LQ: £3,648; median: £4,461; UQ: £5,181
    mode £4,451 occurred 0.746%
    sample size 200,000
    4,474 ± 1,152   1,328,250       36      3,648   4,461   5,181   8,922   4,451   0.7460  200,000

    joker
    collecting data for joker
    intitialised at 0.000s
    (4.831s) progress:  99% ...................................................................................................
    done; completed 200000 games in 4.871s (that's 41061 games/s)
    sorting
    sorted
    serialising to 'datasets/joker/200000-2017-12-19-15-36-21.dat'
    serialised
    average £3,761 ± £3,893 (variance £²15,157,191)
    min: £0; max: £36,857
    LQ: £929; median: £2,454; UQ: £5,289
    mode £132 occurred 0.087%
    sample size 200,000
    3,761 ± 3,893   15,157,191      0       929     2,454   5,289   36,857  132     0.0870  200,000

    twoface
    collecting data for twoface
    intitialised at 0.000s
    (6.706s) progress:  99% ...................................................................................................
    done; completed 200000 games in 6.750s (that's 29628 games/s)
    sorting
    sorted
    serialising to 'datasets/twoface/200000-2017-12-19-15-36-29.dat'
    serialised
    average £2,729 ± £2,575 (variance £²6,634,766)
    min: £-4,302; max: £35,659
    LQ: £943; median: £1,951; UQ: £3,681
    mode £720 occurred 0.056%
    sample size 200,000
    2,729 ± 2,575   6,634,766       -4,302  943     1,951   3,681   35,659  720     0.0560  200,000

    shrewd
    collecting data for shrewd
    intitialised at 0.000s
    (2.421s) progress:  99% ...................................................................................................
    done; completed 200000 games in 2.442s (that's 81904 games/s)
    sorting
    sorted
    serialising to 'datasets/shrewd/200000-2017-12-19-15-36-32.dat'
    serialised
    average £6,450 ± £4,519 (variance £²20,425,205)
    min: £0; max: £22,410
    LQ: £2,562; median: £5,343; UQ: £9,700
    mode £2,502 occurred 0.388%
    sample size 200,000
    6,450 ± 4,519   20,425,205      0       2,562   5,343   9,700   22,410  2,502   0.3880  200,000


Analysing stored data:

    $ for plr in datasets/*; do echo "\n$plr"; cat $plr/* | python stats.py --file -; done

    datasets/early
    reading data from file
    read data at 0.565
    sorted data at 0.627
    average £4,474 ± £1,152 (variance £²1,327,270)
    min: £10; max: £8,940
    LQ: £3,645; median: £4,461; UQ: £5,184
    mode £5,063 occurred 0.732%
    sample size 2,861,536
    4,474 ± 1,152   1,327,270       10      3,645   4,461   5,184   8,940   5,063   0.7324  2,861,536

    datasets/half_mountain
    reading data from file
    read data at 0.595
    sorted data at 0.680
    average £4,338 ± £4,176 (variance £²17,446,114)
    min: £0; max: £30,038
    LQ: £1,426; median: £3,020; UQ: £5,812
    mode £23,487 occurred 0.101%
    sample size 2,974,983
    4,338 ± 4,176   17,446,114      0       1,426   3,020   5,812   30,038  23,487  0.1006  2,974,983

    datasets/joker
    reading data from file
    read data at 0.592
    sorted data at 0.689
    average £3,765 ± £3,888 (variance £²15,119,705)
    min: £0; max: £43,451
    LQ: £927; median: £2,458; UQ: £5,307
    mode £132 occurred 0.072%
    sample size 3,011,108
    3,765 ± 3,888   15,119,705      0       927     2,458   5,307   43,451  132     0.0720  3,011,108

    datasets/libertarian
    reading data from file
    read data at 0.548
    sorted data at 0.616
    average £4,834 ± £1,670 (variance £²2,790,519)
    min: £0; max: £12,765
    LQ: £3,640; median: £4,715; UQ: £5,908
    mode £5,240 occurred 0.384%
    sample size 2,753,692
    4,834 ± 1,670   2,790,519       0       3,640   4,715   5,908   12,765  5,240   0.3840  2,753,692

    datasets/mtn_dew
    reading data from file
    read data at 0.626
    sorted data at 0.735
    average £4,858 ± £2,618 (variance £²6,858,951)
    min: £0; max: £17,612
    LQ: £2,916; median: £4,390; UQ: £6,308
    mode £14,088 occurred 0.099%
    sample size 3,175,409
    4,858 ± 2,618   6,858,951       0       2,916   4,390   6,308   17,612  14,088  0.0988  3,175,409

    datasets/mvd
    reading data from file
    read data at 1.359
    sorted data at 1.582
    average £4,956 ± £1,676 (variance £²2,811,321)
    min: £0; max: £11,858
    LQ: £3,759; median: £4,845; UQ: £6,001
    mode £5,289 occurred 0.507%
    sample size 6,877,285
    4,956 ± 1,676   2,811,321       0       3,759   4,845   6,001   11,858  5,289   0.5070  6,877,285

    datasets/shrewd
    reading data from file
    read data at 0.058
    sorted data at 0.064
    average £6,452 ± £4,519 (variance £²20,424,215)
    min: £0; max: £22,410
    LQ: £2,565; median: £5,343; UQ: £9,700
    mode £2,502 occurred 0.382%
    sample size 263,888
    6,452 ± 4,519   20,424,215      0       2,565   5,343   9,700   22,410  2,502   0.3824  263,888

    datasets/stingy
    reading data from file
    read data at 0.572
    sorted data at 0.629
    average £2,920 ± £451 (variance £²203,881)
    min: £626; max: £4,408
    LQ: £2,646; median: £2,924; UQ: £3,214
    mode £3,139 occurred 1.492%
    sample size 2,849,108
    2,920 ± 451     203,881 626     2,646   2,924   3,214   4,408   3,139   1.4923  2,849,108

    datasets/twoface
    reading data from file
    read data at 0.475
    sorted data at 0.536
    average £2,730 ± £2,568 (variance £²6,598,570)
    min: £-5,570; max: £41,073
    LQ: £941; median: £1,956; UQ: £3,683
    mode £240 occurred 0.047%
    sample size 2,249,044
    2,730 ± 2,568   6,598,570       -5,570  941     1,956   3,683   41,073  240     0.0470  2,249,044

    datasets/unethical
    reading data from file
    read data at 0.565
    sorted data at 0.653
    average £3,925 ± £3,870 (variance £²14,978,800)
    min: £-9,672; max: £20,900
    LQ: £224; median: £4,407; UQ: £6,734
    mode £45 occurred 0.283%
    sample size 2,823,587
    3,925 ± 3,870   14,978,800      -9,672  224     4,407   6,734   20,900  45      0.2826  2,823,587

    datasets/woody
    reading data from file
    read data at 0.612
    sorted data at 0.658
    average £2,831 ± £6 (variance £²42)
    min: £2,826; max: £2,861
    LQ: £2,826; median: £2,834; UQ: £2,835
    mode £2,826 occurred 48.217%
    sample size 2,911,603
    2,831 ± 6       42      2,826   2,826   2,834   2,835   2,861   2,826   48.2168 2,911,603
