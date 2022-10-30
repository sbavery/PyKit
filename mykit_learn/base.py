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


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_memo(n, memo={1: 1, 2: 1}):
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo=memo) + fib_memo(n - 2, memo=memo)
    return memo[n]


def fib_perf(n, num_runs, calculate="fib_all"):
    from timeit import timeit

    fib_time, fib_memo_time = "N/A", "N/A"
    if calculate in ("fib_all", "fib"):
        fib_time = timeit(
            "fib(" + str(n) + ")", "from base import fib", number=num_runs
        )
    if calculate in ("fib_all", "fib_memo"):
        fib_memo_time = timeit(
            "fib_memo(" + str(n) + ")",
            "from base import fib_memo",
            number=num_runs,
        )
    return [fib_time, fib_memo_time]


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


# List Comprehensions


def divisors(n):
    """Return the integers that evenly divide n."""
    return [1] + [x for x in range(2, n) if n % x == 0]


# Trees


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is not None:
            self.print_tree(self.root)

    def print_tree(self, node, lvl=0):
        if node is not None:
            self.print_tree(node.right, lvl + 1)
            print(" " * 3 * lvl + str(node.value) + "<")
            self.print_tree(node.left, lvl + 1)

    def get_root(self):
        return self.root

    def add(self, val):
        if isinstance(val, list):
            if self.root is None and len(val) > 1:
                self.root = Node(val[0])
                val.pop(0)
            elif self.root is None:
                self.root = Node(val[0])
                return None
            for v in val:
                self._add(v, self.root)
        else:
            if self.root is None:
                self.root = Node(val)
            else:
                self._add(val, self.root)

    def _add(self, val, node):
        if val < node.value:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.value:
            return node
        elif val < node.value and node.left is not None:
            return self._find(val, node.left)
        elif val > node.value and node.right is not None:
            return self._find(val, node.right)

    def delete_tree(self):
        # garbage collector will do this for us.
        self.root = None


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    """Construct a Fibonacci tree."""
    if n == 0 or n == 1:
        return tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(t):
    """The number of leaves in tree."""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])


def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])


# Iterators


def fib_iter(n1=0, n2=1):
    """Yield fibonacci sequence."""
    yield n1 + n2
    yield from fib_iter(n2, n1 + n2)


class Countdown:
    """Count down to zero."""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        v = self.start
        while v > 0:
            yield v
            v -= 1


# Object Oriented Programming


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100

    strength = 0
    defense = 0
    weapon = Weapon("None", 0)
    armor = Armor("None", 0)

    def attack(self, damage_multiplier=1):
        return damage_multiplier * (self.strength + self.weapon.damage)

    def defend(self, damage):
        net_damage = damage - (self.defense + self.armor.defense)

        if net_damage > 0:
            self.health -= net_damage


class Warrior(Character):
    strength = 10
    defense = 5
    weapon = Weapon("Dagger", 5)
    armor = Armor("Tunic", 5)

    def attack_with_power(self):
        return Character.attack(self, 2)


class EvilKing(Character):
    strength = 20
    defense = 10
    weapon = Weapon("Evil King Staff", 10)
    armor = Armor("Evil King Armor", 10)

    def attack_with_blood_sacrifice(self):
        self.health -= 30
        return Character.attack(self, 3)


# Linked Lists

class Link:
    def __init__(self,first,rest):
        self.first = first
        self.rest = rest