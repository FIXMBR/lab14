from app import shuffle
from app import is_sorted
from app import bogosort
import pytest

testdata1 = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], True, True),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], False, True),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], True, False),
    ([4, 7, 2, 8, 4, 1], True, False),
    ([4, 7, 2, 8, 4, 1], False, False),
    ([1, 4, 7, 9], True, True),
    ([9, 8, 5, 2, 1], False, True),
]


@pytest.mark.parametrize('sample, ascending, result', testdata1)
def test_shuffle(sample, ascending, result):
    assert len(shuffle(sample)) == len(sample)


@pytest.mark.parametrize('sample, ascending, result', testdata1)
def test_is_sorted(sample, ascending, result):

    assert is_sorted(sample, ascending) == result


testdata2 = [
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], True, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([5, 6, 4, 7, 3, 8, 2, 9, 1], False, [9, 8, 7, 6, 5, 4, 3, 2, 1])
]


@pytest.mark.parametrize('sample, ascending, expected_output', testdata2)
def test_bogosort(sample, ascending, expected_output):

    assert bogosort(sample, ascending) == expected_output
