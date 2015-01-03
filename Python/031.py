import sys
import os
import timeit
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###############################################################################
# In England the currency is made up of pound, P, and pence, p,
# and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, 1P (100p) and 2P (200p).
# It is possible to make 2P in the following way:

# 1x1P + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
# How many different ways can P2 be made using any number of coins?
###############################################################################


def coin_combs_brute_force(t):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = 0

    for a in range(t, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1 , -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                ways += 1


    return ways

def coin_combs_dynamic_prog(t):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (t + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, t + 1):
            ways[i] += ways[i-coin]
    return ways[t]
    

def main():
    print("Number of different ways to produce 2 pounds: {}".format(coin_combs_dynamic_prog(200)))
    

print("Time: {}".format(timeit.timeit('main()', "from __main__ import main", number=1)))