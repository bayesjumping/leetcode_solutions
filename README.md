# LeetCode Solutions
![Tests](https://github.com/bayesjumping/leetcode_solutions/actions/workflows/tests.yml/badge.svg) [![codecov](https://codecov.io/gh/bayesjumping/leetcode_solutions/branch/main/graph/badge.svg)](https://codecov.io/gh/bayesjumping/leetcode_solutions)

These are some solutions to LeetCode problems as I work through them.

## Setup

1. Create the virtual environment:
```bash
make venv
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
make install
```

## Running Tests

Run all tests:
```bash
make test
```

Run tests with coverage:
```bash
make test-cov
```

## Other Commands

- `make lint` - Run linter
- `make format` - Format code
- `make clean` - Remove generated files 
