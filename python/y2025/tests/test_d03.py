import pytest
from y2025.d03_1 import main as main1


@pytest.fixture
def day03_example_text():
    with open("data/2025/test03.txt") as f:
        return f.read().strip()


def test_part1(day03_example_text):
    assert main1(day03_example_text) == 29
