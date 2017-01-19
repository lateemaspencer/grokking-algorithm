from itertools import combinations
from random import randrange
from unittest import TestCase

def merge_and_count_inversions(seq, start, middle, end):
    """Merge two adjacent sorted sub-sequences of seq and count
    inversions.

    Arguments:
    seq -- sequence to sort
    start -- index of beginning of first sorted subsequence
    middle -- end of first, and beginning of second, sorted subsequence
    end -- end of second sorted subsequence

    Result: number of inversions (cases where i < j, but seq[i] > seq[j]).

    Side effect: seq is sorted between start and end.

    """
    assert 0 <= start < middle < end <= len(seq)
    inversions = 0
    temp = []
    i = start
    j = middle
    while i < middle and j < end:
        if seq[i] <= seq[j]:
            temp.append(seq[i])
            i += 1
        else:
            temp.append(seq[j])