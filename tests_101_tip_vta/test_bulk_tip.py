import pytest

from implementations.tip import total_with_tip

# Parametrization

@pytest.mark.parametrize("num1, num2, expected", [
    (10,20,12),
    (100,20,120),
    (0,0,5)
])

def test_bulk_tip(num1, num2, expected):
    assert total_with_tip(num1, num2) == expected