""" Here is an explanation of some terms used in the docstrings:

- Let's say that a mark on a piece of work is 4/5.
  - the raw mark is 4
  - the maximum possible mark is 5

- The final course mark is out of a maximum possible mark of 100.

- Let's say that A1 is worth 10 marks of the final course mark (out of 100).
  If a student earns 80% on A1, then the contribution of A1 to the final
  course mark is 8 (out of 10).
  
"""


def percentage(raw_mark, max_mark):
    """ (number, number) -> float

    Return the percentage mark for a piece of work that received a mark of
    raw_mark out of a maximum possible mark max_mark.

    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    """

    return raw_mark / max_mark * 100


def contribution(mark_as_percent, weight):
    """ (number, number) -> float

    Return the number of marks that a piece of work contributes to the final
    course mark for a piece of work that earned mark_as_percentage percent and
    is worth weight marks (out of 100).
    
    >>> contribution(100, 7)
    7.0
    >>> contribution(50, 12.5)
    6.25
    """
    
    return mark_as_percent * weight / 100

def raw_contribution(raw_mark, max_mark, weight):
    """ (number, number, number) -> float

    Return the number of marks that a piece of work contributes to the final
    course mark for a piece of work that received a mark of raw_mark out of
    a maximum possible mark max_mark, and is worth weight marks (out of 100).
    
    >>> raw_contribution(13.5, 15, 10)
    9.0
    >>> raw_contribution(5, 10, 20)
    10.0
    """
    
    return raw_mark / max_mark * weight

def assignments_contribution(a1, a2):
    """ (number, number) -> float

    Return the contributation to final course mark made by raw marks a1
    and a2, which are both marked out of 40 and worth 10% each.

    >>> assignments_contribution(32, 30)
    15.5
    """

    return raw_contribution(a1, 40, 10) + raw_contribution(a2, 40, 10)


def exercises_contribution(e1, e2, e3, e4):
    """ (number, number, number, number) -> float

    Return the contributation to final course mark made by raw marks e1, e2,
    e3 and e4, which are all marked out of 10 and worth 3% each.

    >>> exercises_contribution(10, 10, 5, 10)
    10.5
    >>> exercises_contribution(7, 8, 9, 10)
    10.2
    """
    
    return raw_contribution(e1, 10, 3) + raw_contribution(e2, 10, 3) + raw_contribution(e3, 10, 3) + raw_contribution(e4, 10, 3)


def test_contribution(test):
    """ (number) -> float

    Return the contributation to final course mark made by raw mark test,
    which is marked out of 25 and worth 14%.

    >>> test_contribution(21)
    11.76
    >>> test_contribution(15)
    8.4
    """

    return raw_contribution(test, 25, 14)

def term_work_mark(assignments, exercises, labs, prep, test):
    """ (number, number, number, number, number) -> float

    Return the total contribution to the final course mark with
    contributions to the final course grade of assignments (out of 20),
    exercises (out of 12), labs (out of 4.5), prep (out of 5.5) and test
    (out of 14).
    
    >>> term_work_mark(16, 10.5, 4, 5, 12)
    47.5
    >>> term_work_mark(2, 8, 10, 3, 5)
    28.0
    """

    return float(assignments + exercises + labs + prep + test)


def exam_required(term_work, desired_grade):
    """ (float, int) -> float
    
    Return the percentage mark required on the exam for the final mark to be
    desired_grade with a term work mark of term_work (out of 56).
    
    >>> exam_required(47, 80)
    75.0
    >>> exam_required(42, 75)
    75.0
    """

    return (desired_grade - term_work ) / 44 * 100
