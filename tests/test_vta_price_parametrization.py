import pytest

from implementations.vta_price import vta_price

@pytest.mark.parametrize("ht, vta, expected", [
    (100, 10, 110),
    (100, 20, 120),
    (100, 30, 130),
    (100, 40, 140),
    (100, 50, 150),
])
def test_vta_price(ht, vta, expected):
    assert vta_price(ht, vta) == expected