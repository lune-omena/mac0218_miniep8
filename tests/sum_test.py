from src.sum_n import sum_n

from multiprocessing import Process
import pytest

def test_empty():
    assert sum_n(l = [], N = 1, S = 1) == []
    assert sum_n(l = [], N = 10, S = 10) == []

def test_impossibility():
    with pytest.raises(ValueError, match="N must be len N or less"):
        sum_n(l = [1,2,3], N = 4, S = 2) == []
    with pytest.raises(ValueError, match="N must be len N or less"):
        sum_n(l = [1], N = 30, S = 2) == []
    with pytest.raises(ValueError, match="N must be len N or less"):
        sum_n(l = [1,2,3], N = 300, S = 2) == []
    with pytest.raises(ValueError, match="N must be 1 or more"):
        sum_n(l = [1,2,3], N = -1, S = 2) == []
    with pytest.raises(ValueError, match="N must be 1 or more"):
        sum_n(l = [1,2,3], N = 0, S = 2) == []

def test_one():
    assert sum_n(l = [1,2,3], N = 1, S = 1) == [1]
    assert sum_n(l = [1,2,3], N = 1, S = 3) == [3]
    assert sum_n(l = [1,2,3], N = 1, S = 4) == []
    assert sum_n(l = [1,2,3], N = 1, S = 10) == []

def test_two():
    assert sum_n(l = [1,2,3], N = 2, S = 1) == []
    assert (sum_n(l = [1,2,3,0,0,0,0,6], N = 2, S = 3) == [1,2] or sum_n(l = [1,2,3,0,0,0,0,6], N = 2, S = 3) == [0,3])
    assert sum_n(l = [1,2,3,4,10], N = 2, S = 14) == [4,10]
    assert sum_n(l = [1,2,3,8,15], N = 2, S = 10) == [2,8]

def test_N():
    assert sum_n(l = [1,2,3], N = 3, S = 6) == [1,2,3]
    assert sum_n(l = [1,2,3,4,5,6], N = 4, S = 13) == [1,2,4,6]
    assert sum_n(l = [1,2,3,4,5,6], N = 5, S = 6) == []
    assert sum_n(l = [1,2,3,4,5,6,10], N = 5, S = 21) == [1,2,3,5,10]

@pytest.mark.timeout(15)
def test_too_long_exec():
    base_list = [1]*10000 + [5,6]

    assert sum_n(l = base_list, N = 2, S = 11) == [5,6]
    assert sum_n(l = base_list, N = 5, S = 14) == [1,1,1,5,6]
    assert sum_n(l = base_list, N = 10, S = 19) == [1,1,1,1,1,1,1,1,5,6]