import pytest
from y2025.d02_1 import main as main1


@pytest.fixture
def day02_example_text():
    with open("data/2025/test02.txt") as f:
        return f.read().strip()


def test_part1(day02_example_text):
    assert main1(day02_example_text) == "[357,862]"
