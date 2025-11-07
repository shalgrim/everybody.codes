import pytest
from y2025.d01_1 import main


@pytest.fixture
def day01_example_file_lines():
    with open("data/2025/day01_example.txt") as f:
        return [line.strip() for line in f.readlines()]


def test_part1(day01_example_file_lines):
    assert main(day01_example_file_lines) == "Fyrryn"
