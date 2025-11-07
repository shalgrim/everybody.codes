# Everybody Codes Solutions

Solutions for [Everybody Codes](https://everybody.codes) - a coding puzzle competition.

## Languages

Currently includes:
- Python

## Setup

### Python
```bash
cd python
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux, or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt
pip install pytest  # For running tests
```

## Running Tests

### Python
```bash
cd python
pytest                      # Run all tests
pytest tests/test_dayXX.py # Run specific day's tests
pytest -v                   # Verbose output
```

## Project Structure

```
everybody.codes/
├── python/           # Python solutions
│   ├── dayXX_Y.py   # Solution files (XX = day number, Y = part number)
│   ├── tests/       # pytest test files
│   └── .venv/       # Python virtual environment
└── data/            # Shared input data and examples
    └── dayXX_*.txt  # Example and actual puzzle inputs
```
