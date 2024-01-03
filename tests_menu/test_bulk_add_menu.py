import pytest

from implementations.menu import Menu

@pytest.mark.parametrize("restaurant, item, description, price, expected", [
    ("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5, "Menu item added for Cafe Mocha."),
    ("Sushi Express", "Sushi", "Fresh sushi", 5.5, "Menu item added for Sushi Express."),
    ("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5, "Menu item added for Cafe Mocha."),
    ("Sushi Express", "Sashimi", "Fresh sashimi", 6.5, "Menu item added for Sushi Express.")
])
def test_add_menu_item(restaurant, item, description, price, expected):
    menu = Menu()
    result = menu.add_menu_item(restaurant, item, description, price)
    assert result == expected   

@pytest.mark.parametrize("restaurant, item, description, price, expected", [
    ("Cafe Mocha", "Mocha", "Great coffee and pastries", -3.5, "Price must be positive."),
    ("Sushi Express", "Sushi", "Fresh sushi", -5.5, "Price must be positive."),
    ("Cafe Mocha", "Latte", "Great coffee and pastries", -3.5, "Price must be positive."),
    ("Sushi Express", "Sashimi", "Fresh sashimi", -6.5, "Price must be positive.")
])
def test_add_menu_item_with_negative_price(restaurant, item, description, price, expected):
    menu = Menu()
    with pytest.raises(ValueError) as e:
        menu.add_menu_item(restaurant, item, description, price)
    assert str(e.value) == expected