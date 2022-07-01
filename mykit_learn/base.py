"""
mykit_learn base module.
"""

NAME = "mykit_learn"


class Control:
    """Demonstrates how various operators work for two
    inputs. Prints human readable outputs from each
    operation
    """

    import operator as o

    operators = {
        ">": o.gt,
        "<": o.lt,
        ">=": o.ge,
        "<=": o.le,
        "==": o.eq,
        "+": o.add,
        "-": o.sub,
        "//": o.floordiv,
        "/": o.truediv,
        "%": o.mod,
        "*": o.mul,
        "@": o.matmul,
        "**": o.pow,
        "not": o.not_,
        "is": o.is_,
        "and": o.and_,
        "or": o.or_,
        "xor": o.xor,
        "concat": o.concat,
        "contains": o.contains,
    }

    def __init__(self, in1, in2, op="", prints=True):
        self.in1 = in1
        self.in2 = in2
        self.op = op
        self.prints = prints

    def operate(self):
        try:
            return self.operators[self.op](self.in1, self.in2)
        except Exception:
            return "N/A"

    def printAllOps(self):
        last_op = ""

        for op in self.operators:
            self.op = op
            last_op = self.operate()
            if self.prints is True:
                print(
                    str(self.in1)
                    + " "
                    + op
                    + " "
                    + str(self.in2)
                    + " : "
                    + str(last_op)
                )

        return last_op


# Recursion


def summation(n, term):
    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!
    """
    assert n >= 1

    if n == 1:
        return term(1)
    else:
        return term(n) + summation(n - 1, term)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.
    """
    if a > b and a % b != 0:
        return gcd(b, a % b)
    elif b > a and b % a != 0:
        return gcd(a, b % a)
    else:
        return b


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    """
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)


def max_subseq(n, length):
    """Return the maximum subsequence of specified length
    that can be found in the given number n.
    """
    s = str(n)

    if length == 0:
        return 0
    elif len(s) < length or len(s) < 2:
        return int(s[:length])
    else:
        return max(
            max_subseq(int(s[:-1]), length),
            int(s[-1]) + 10 * max_subseq(int(s[:-1]), length - 1),
        )


def count_k(n, k):
    """Return the number of paths up a staircase using
    up to k steps at a time.
    """
    c = 0
    if n in {0, 1}:
        return 1
    else:
        for i in range(1, k + 1):
            if (n - i) < 0:
                pass
            else:
                c += count_k(n - i, k)
        return c

# Lists

def couple(lst1, lst2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    """
    assert len(lst1) == len(lst2)

    bigboy = []
    for i in range(0, len(lst1)):
        bigboy.append([lst1[i], lst2[i]])

    return bigboy

# Trees

def nut_finder(t):
    """Returns True if t contains a node with the value 'nut' and
    False otherwise.

    >>> scrat = tree('nut')
    >>> nut_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('nut')]), tree('branch2')])
    >>> nut_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> nut_finder(numbers)
    False
    >>> t = tree(1, [tree('nut',[tree('not nut')])])
    >>> nut_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"