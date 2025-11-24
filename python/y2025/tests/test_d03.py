import pytest
from y2025.d03_1 import main as main1
from y2025.d03_2 import main as main2
from y2025.d03_3 import main as main3


@pytest.fixture
def day03_example_text():
    with open("data/2025/test03.txt") as f:
        return f.read().strip()


@pytest.fixture
def day03_example_text_2():
    with open("data/2025/test03_2.txt") as f:
        return f.read().strip()


@pytest.fixture
def day03_example_text_3():
    with open("data/2025/test03_3.txt") as f:
        return f.read().strip()


def test_part1(day03_example_text):
    assert main1(day03_example_text) == 29


def test_part2(day03_example_text_2):
    assert main2(day03_example_text_2) == 781


def test_part3(day03_example_text_3):
    assert main3(day03_example_text_3) == 3
