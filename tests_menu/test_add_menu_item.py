import pytest

from implementations.menu import Menu

def test_add_menu_item():
    menu = Menu()
    result = menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    assert result == "Menu item added for Cafe Mocha."
    result = menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    assert result == "Menu item added for Sushi Express."

def test_add_menu_item_with_negative_price():
    menu = Menu()
    with pytest.raises(ValueError) as e:
        menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", -3.5)
    assert str(e.value) == "Price must be positive."