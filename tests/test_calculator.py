"""Tests for the calculator module."""
import pytest
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import add, subtract, multiply, divide


class TestCalculator:
    """Test cases for calculator functions."""

    def test_add(self):
        """Test addition."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction."""
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(5, 5) == 0

    def test_multiply(self):
        """Test multiplication."""
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0

    def test_divide(self):
        """Test division."""
        assert divide(6, 2) == 3
        assert divide(5, 2) == 2.5
        assert divide(-10, 2) == -5

    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
