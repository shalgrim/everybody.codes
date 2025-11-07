# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a solution repository for Everybody Codes (https://everybody.codes) - a coding puzzle competition similar to Advent of Code. The repository contains Python solutions organized by day, with test cases and example input data.

## Repository Structure

```
everybody.codes/
├── python/           # Python solution implementations
│   ├── dayXX_Y.py   # Solution files (XX = day number, Y = part number)
│   ├── tests/       # pytest test files
│   └── .venv/       # Python virtual environment
└── data/            # Input data and examples
    └── dayXX_*.txt  # Example and actual puzzle inputs
```

## Development Commands

### Environment Setup
```bash
cd python
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
pip install pytest  # For running tests
```

Note: `requirements-dev.txt` contains a local editable install (`-e ../../coding-puzzle-tools`) intended for the repository author's development environment.

### Running Tests
```bash
# From the python/ directory
pytest                           # Run all tests
pytest tests/test_dayXX.py      # Run specific day's tests
pytest -v                        # Verbose output
pytest -k test_part1            # Run specific test by name
```

### Dependency Management
This project uses `uv` for dependency management:
```bash
# Compile production dependencies
uv pip compile requirements.in -o requirements.txt

# Compile dev dependencies (author only)
uv pip compile requirements-dev.in -o requirements-dev.txt
```

## Code Architecture

### Solution Pattern
Each day's solution follows a standard pattern:
- **Solution file** (`dayXX_Y.py`): Contains a `main(lines)` function that accepts puzzle input as a list of strings and returns the solution
- **Test file** (`tests/test_dayXX.py`): Uses pytest fixtures to load example data from `data/dayXX_example.txt` and verify the solution
- **Input data**: Example inputs in `data/dayXX_example.txt` for testing, actual puzzle inputs may be stored separately

### Dependencies
- **coding-puzzle-tools**: Custom utility library for common puzzle-solving patterns (https://github.com/shalgrim/coding-puzzle-tools)
- **pytest**: Testing framework with fixtures for loading puzzle input files

### Testing Strategy
Tests use pytest fixtures to load example input data:
```python
@pytest.fixture
def dayXX_example_file_lines():
    with open("data/dayXX_example.txt") as f:
        return [line.strip() for line in f.readlines()]
```

Solutions are validated against known outputs from example data before running on actual puzzle inputs.

## Working Directory
When running tests or executing solutions, the working directory should be `python/` to ensure proper path resolution for data files.