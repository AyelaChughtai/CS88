######################
# Required Questions #
######################

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    current_n = n
    if n==0 or n==1:
        return 1
    if k== 0:
        return 1

    while k >1 and n> 1:
        current_n = current_n * (n-1)
        n=n-1
        k=k-1
    return current_n


def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    for i in lst:
        if i!=0:
            return i


def has_n(lst, n):
    """ Returns whether or not a list contains the value n.

    >>> has_n([1, 2, 2], 2)
    True
    >>> has_n([0, 1, 2], 3)
    False
    >>> has_n([], 5)
    False
    """
    for i in lst:
        if (i==n):
            return True
    return False

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    counter = 1
    while n != 1:
        counter= counter+1
        print(int(n))

        if n%2==0:
            n=n/2
        else :
            n=3*n +1
    print(int(n))
    return counter

def odd_even(x):
    """Classify a number as odd or even.
    
    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    if x%2==0:
        return 'even'
    else:
        return 'odd'

def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    return ['even' if x%2==0 else 'odd' for x in s]


def decode_helper(pair):
    """
    Optional helper function! Could be useful to turn something like [0, 0] to 'Male 0-9'
    """
    "*** YOUR CODE HERE ***"
    if pair[1]>=10:
        age = "100+"
    else:
        age = str(pair[1]*10) + "-" + str(pair[1]*10+9)
    if pair[0]== 0:
        sex = "Male"
    else:
        sex = "Female"

        
    return ( sex + " " + age)
    

def decode(list_of_sex_age_pairs):
    """
    >>> decode([[0, 0], [1, 1], [1, 10]])
    ['Male 0-9', 'Female 10-19', 'Female 100+']
    >>> decode([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]])
    ['Male 0-9', 'Male 10-19', 'Male 20-29', 'Male 30-39', 'Male 40-49', 'Female 50-59', 'Female 60-69', 'Female 70-79', 'Female 80-89', 'Female 90-99', 'Female 100+']
    """ 
    
    return [decode_helper(num1) for num1 in list_of_sex_age_pairs]


