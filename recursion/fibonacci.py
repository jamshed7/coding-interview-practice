# Functions to return the nth Fibonacci number


# recursive solution
def fib_rec(n):

    if n == 1 or n == 0:
        return n

    else:
        return fib_rec(n-1) + fib_rec(n-2)



# Dynamic programming solution

# Size of cache has to set before execution of function
n = 23
cache = [None] * (n + 1)


def fib_dyn(n):
    if n == 1 or n == 0:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]


# Simple iterative solution
def fib_iter(n):
    first = 0
    second = 1

    for i in range(n):
        temp = first + second
        first = second
        second = temp

    return first



#Testing
from nose.tools import assert_equal

class TestFib(object):

    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)
        print ('Passed all tests.')


t = TestFib()

print('\nTesting recursive solution:')
t.test(fib_rec)

print('\nTesting dynamic programming solution:')
t.test(fib_dyn) # Note, will need to reset cache size for each test!

print('\nTesting iterative solution:')
t.test(fib_iter)
