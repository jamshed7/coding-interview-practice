#function that uses recursion to output a list of all the possible permutations of a string

def permute(s):

    out = []

    if len(s) == 1:
        return s

    else:
        #for each letter in the string
                             #remember: enumerate returns tuple -> (index, value)
        for index, letter in enumerate(s):
            #for each permutation of the string minus the letter itself
            # i.e. the string with the letter taken out
            for perm in permute( s[:index] + s[index+1:] ):
                #add to output, the letter itself and the permutations of the remainder of the string
                out += [letter + perm]


    #return the output list
    return out



#Testing
from nose.tools import assert_equal

class Test(object):

    def test(self,solution):

        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )

        print ('All test cases passed.')


t = Test()
t.test(permute)
