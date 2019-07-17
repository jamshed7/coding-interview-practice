#Reverse a string using recursion
def reverse(s):

    if len(s) == 1:
        return s

    return reverse(s[1::]) + s[0]


#Testing
from nose.tools import assert_equal

class Test(object):
    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')

        print ('PASSED ALL TEST CASES!')

test = Test()
test.test_rev(reverse)
