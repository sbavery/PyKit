import mykit_learn.base as base
import pytest


def test_base():
    assert base.NAME == "mykit_learn"


def test_control():
    in1, in2, operator = "a", "b", "<"
    assert base.Control(in1, in2, operator).operate() == True
    assert base.Control(in1, in2, prints=False).printAllOps() == False

    in1, in2, operator = "2", "2", "and"
    assert base.Control(in1, in2, operator).operate() == "N/A"
    assert base.Control(in1, in2, prints=False).printAllOps() == True


def test_recursion():
    assert base.fib(20) == 6765
    assert base.fib_memo(20) == 6765

    assert base.summation(5, lambda x: x * x * x) == 225
    assert base.summation(9, lambda x: x + 1) == 54
    assert base.summation(5, lambda x: 2**x) == 62

    assert base.gcd(34, 19) == 1
    assert base.gcd(39, 91) == 13
    assert base.gcd(20, 30) == 10
    assert base.gcd(40, 40) == 40

    assert base.paths(2, 2) == 2
    assert base.paths(5, 7) == 210
    assert base.paths(117, 1) == 1
    assert base.paths(1, 157) == 1

    assert base.max_subseq(20125, 3) == 225
    assert base.max_subseq(20125, 5) == 20125
    assert base.max_subseq(20125, 6) == 20125
    assert base.max_subseq(12345, 3) == 345
    assert base.max_subseq(12345, 0) == 0
    assert base.max_subseq(12345, 1) == 5

    assert base.count_k(3, 3) == 4
    assert base.count_k(4, 4) == 8
    assert base.count_k(10, 3) == 274
    assert base.count_k(300, 1) == 1


def test_lists():
    lst1, lst2 = [1, 2, 3], [4, 5, 6]
    assert base.couple(lst1, lst2) == [[1, 4], [2, 5], [3, 6]]

    assert base.divisors(1) == [1]
    assert base.divisors(4) == [1, 2]
    assert base.divisors(12) == [1, 2, 3, 4, 6]


def test_trees():
    bt = base.BinaryTree()
    bt.add([8, 4, 12, 2, 6])
    assert bt.find(8).left.value == 4
    assert bt.find(4).right.value == 6
    assert bt.get_root().value == 8
    bt.delete_tree()
    assert bt.__str__() == None
    assert bt.get_root() == None

    tree = base.fib_tree(5)
    assert tree[0] == 5
    inc_tree = base.increment(tree)
    assert inc_tree[1][0] == 3
    assert base.count_leaves(inc_tree) == 8


def test_iterators():
    fib = base.fib_iter(2, 3)
    assert next(fib) == 5

    countdown = base.Countdown(5)
    assert list(countdown) == [5, 4, 3, 2, 1]


def test_objects():
    Sam = base.Warrior("Sam")
    Bob = base.EvilKing("Bob")
    assert Bob.health == 100
    Bob.defend(Sam.attack())
    assert Bob.health == 100
    Sam.defend(Bob.attack_with_blood_sacrifice())
    assert Sam.health == 20
    assert Bob.health == 70
    Sam.weapon = base.Weapon("Excalibur", 40)
    Bob.defend(Sam.attack_with_power())
    assert Bob.health < 0
