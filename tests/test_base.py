import mykit_learn.base as base


def test_base():
    assert base.NAME == "mykit_learn"

    # Control and Operators
    in1, in2, operator = "a", "b", "<"
    assert base.Control(in1, in2, operator).operate() == True
    assert base.Control(in1, in2, prints=False).printAllOps() == False
    assert base.Control(in1, in2).printAllOps() == False

    in1, in2, operator = "2", "2", "and"
    assert base.Control(in1, in2, operator).operate() == "N/A"
    assert base.Control(in1, in2, prints=False).printAllOps() == True
    assert base.Control(in1, in2).printAllOps() == True

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

    lst1, lst2 = [1, 2, 3], [4, 5, 6]
    assert base.couple(lst1, lst2) == [[1, 4], [2, 5], [3, 6]]
