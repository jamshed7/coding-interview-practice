# Given a target amount n and a array of distinct coin values
# returns the fewest coins needed to make the change amount.
# https://en.wikipedia.org/wiki/Change-making_problem


#simple recursive solution

def rec_coin(target,coins):

    #base case
    if target == 0:
        return 0

    else:
        #coins.sort(reverse = True)

        for coin in coins[::-1]:
            x = target-coin
            if x >= 0:
                #print(coin) <- uncomment to reveal each coin being added

                return 1 + rec_coin( (target-coin), coins)



# Memoized solution
def rec_coin_dyn(target,coins, cache):

    #base case
    if target == 0:
        return 0

    elif cache[target] != None:
        return cache[target]

    else:
        #coins.sort(reverse = True)

        for coin in coins[::-1]:
            x = target-coin
            if x >= 0:
                cache[target] = 1 + rec_coin_dyn( (target-coin), coins, cache)

                return cache[target]


# Note:
# For this solution, the coins need to be sorted in increasing order
# This can be done using : coins.sort(reverse = True)


# Testing
from nose.tools import assert_equal

class TestCoins(object):

    def check(self,solution):
        coins = [1,5,10,25]
        assert_equal(solution(45,coins),3)
        assert_equal(solution(23,coins),5)
        assert_equal(solution(74,coins),8)
        print ('Passed all tests.')
# Run Test

test = TestCoins()
print('\nRecursive solution test:')
test.check(rec_coin)
