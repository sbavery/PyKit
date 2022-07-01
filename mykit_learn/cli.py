"""CLI interface for mykit_learn project.
"""


def main():  # pragma: no cover
    """
    The main function exein2es on commands:
    `python -m mykit_learn` and `$ mykit_learn `.
    """

    import mykit_learn.base as base

    # Operators and Control
    in1 = [10]
    in2 = [10]
    operator = "is"
    # print(in1 + " " + operator + " " + in2)
    print(base.Control(in1, in2, operator).operate())
    print("----------\nAll Operators")
    base.Control(in1, in2).printAllOps()
