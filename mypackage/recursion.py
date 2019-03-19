def sum_array(array):

    '''
        Returns sum of all items in array:

        The length of the array is checked first to see if the array has one or more items in array.

        If the array has one item, it must return that item as it doesnt have any other items to add to.

        And then if it has more than one item in the array it must add the items from the first index all the way to the end.

        Args:
        array/list (int): a list/ array of int values to add to each other.

        Examples:

        >>> sum_array([2,4,6,8,10])
            30

        >> sum_array([10,20,30,40,50])
            150

    '''

    if len(array)==1:
        return array[0]
    else:
        return array[0] + sum_array(array[1::])



def fibonacci(n):

    '''
        Returns nth term in fibonacci sequence:

        --The first two terms are 0 and 1:
        -Therefore, it must return a 0 when n is 0
        -And return 1 when n is 1

        --And all the other terms are obtained by adding the preceding two terms.
        -This means to say the nth term is the sum of (n-1)th and (n-2)th term.

        Args:
        n (int): nth term must be an int so that the fibonacci sequence can be calculated accordingly

        Examples:
        >>>fibonacci(7)
           13

        >>>fibonacci(12)
           144

    '''


    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):

    '''
        Returns n!:

        This function returns the product of n.

        Therefore, if n is less than 1 or equals to 1, it will return 1.
        Factorial is not defined for negative numbers, hence the factorial of zero is 1.

        And if n is more than 1 a value more than 1 will be returned, as n is multiplied from the nth number down to 1.

        Args:
        n (int): nth term in factorial sequence to calculate

        Examples:
        >>>factorial(8)
           40320

        >>>factorial(4)
           24

    '''

    whole_num = 1

    while n >= 1:
        whole_num = whole_num * n
        n = n - 1
    return whole_num


def reverse(word):

    '''
        Returns word in reverse:
        - For each alphabet in word , the word will be reversed from the last index all the way to the first index.

        Args:
        word (str): the word must be a string and it will return the reversed word also in a string format

        Examples:
        >>>reverse('happy')
           'yppah'

        >>>reverse('bad')
           'dab'

    '''

    for each_word in word:
        return word[::-1]
