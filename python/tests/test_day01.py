import pytest
from y2025.d01_1 import main as main1
from y2025.d01_2 import main as main2
from y2025.d01_3 import main as main3


@pytest.fixture
def day01_example_file_lines():
    with open("data/2025/day01_example.txt") as f:
        return [line.strip() for line in f.readlines()]


@pytest.fixture
def day01_example_3_file_lines():
    with open("data/2025/test01_3.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part1(day01_example_file_lines):
    assert main1(day01_example_file_lines) == "Fyrryn"


def test_part2(day01_example_file_lines):
    assert main2(day01_example_file_lines) == "Elarzris"


def test_part3(day01_example_3_file_lines):
    assert main3(day01_example_3_file_lines) == "Drakzyph"
