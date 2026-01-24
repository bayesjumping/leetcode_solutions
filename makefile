.PHONY: help venv install test clean lint format run

# Default target
help:
	@echo "Available commands:"
	@echo "  make venv      - Create virtual environment"
	@echo "  make install   - Install dependencies"
	@echo "  make test      - Run tests"
	@echo "  make lint      - Run linter"
	@echo "  make format    - Format code"
	@echo "  make clean     - Remove generated files"

# Create virtual environment
venv:
	python3 -m venv .venv
	@echo "Virtual environment created. Activate with: source .venv/bin/activate"

# Install dependencies
install:
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install pytest pytest-cov black ruff

# Run tests
test:
	.venv/bin/pytest tests/ -v

# Run tests with coverage
test-cov:
	.venv/bin/pytest tests/ -v --cov=src --cov-report=term-missing

# Run linter
lint:
	.venv/bin/ruff check src/ tests/

# Format code
format:
	.venv/bin/black src/ tests/

# Clean generated files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf .coverage htmlcov/
