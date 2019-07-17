#returns the sum of all the individual digits in a given integer
def sum_func(n):

    if n < 1:
        return 0

    return n%10 + sum_func(round(n/10))
