import pytest
from y2025.d02_1 import add, multiply
from y2025.d02_1 import main as main1
from y2025.d02_2 import main as main2
from y2025.d02_2 import should_engrave


@pytest.fixture
def day02_example_text():
    with open("data/2025/test02.txt") as f:
        return f.read().strip()


def test_part1(day02_example_text):
    assert main1(day02_example_text) == "[357,862]"


def test_add():
    """
    [1,1] + [2,2] = [1 + 2, 1 + 2] = [3,3]
    [2,5] + [3,7] = [2 + 3, 5 + 7] = [5,12]
    [-2,5] + [10,-1] = [-2 + 10, 5 + -1] = [8,4]
    [-1,-2] + [-3,-4] = [-1 + -3, -2 + -4] = [-4,-6]
    """
    assert add((1, 1), (2, 2)) == (3, 3)


def test_multiply():
    """
    [1,1] * [2,2] = [1 * 2 - 1 * 2, 1 * 2 + 1 * 2] = [2 - 2, 2 + 2] = [0,4]
    [2,5] * [3,7] = [2 * 3 - 5 * 7, 2 * 7 + 5 * 3] = [6 - 35, 14 + 15] = [-29,29]
    [-2,5] * [10,-1] = [-2 * 10 - 5 * -1, -2 * -1 + 5 * 10] = [-20 + 5, 2 + 50] = [-15,52]
    [-1,-2] * [-3,-4] = [-1 * -3 - -2 * -4, -1 * -4 + -2 * -3] = [3 - 8, 4 + 6] = [-5,10]
    """
    assert multiply((1, 1), (2, 2)) == (0, 4)


def test_part2():
    assert main2("A=[35300,-64910]") == 4076


def test_should_engrave():
    assert should_engrave(35_630, -64_880)
    assert should_engrave(35_630, -64_870)
    assert should_engrave(35_640, -64_860)
    assert should_engrave(36_230, -64_270)
    assert should_engrave(36_250, -64_270)
    assert not should_engrave(35_640, -64_910)
    assert not should_engrave(35470, -64910)
    assert not should_engrave(35480, -64910)
    assert not should_engrave(35680, -64_850)
    assert not should_engrave(35630, -64_830)
