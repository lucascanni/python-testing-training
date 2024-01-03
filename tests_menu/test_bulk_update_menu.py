import pytest

from implementations.menu import Menu
from fixture.menu_fixture import menu_with_some_item

@pytest.mark.parametrize("restaurant, item, new_description, new_price, expected", [
    ("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5, "Menu item updated for Cafe Mocha."),
    ("Sushi Express", "Sushi", "Fresh sushi", 5.5, "Menu item updated for Sushi Express."),
    ("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5, "Menu item updated for Cafe Mocha."),
    ("Sushi Express", "Sashimi", "Fresh sashimi", 6.5, "Menu item updated for Sushi Express.")
])
def test_update_menu_item(restaurant, item, new_description, new_price, expected):
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    menu.add_menu_item("Sushi Express", "Sashimi", "Fresh sashimi", 6.5)
    result = menu.update_menu_item(restaurant, item, new_description, new_price)
    assert result == expected

@pytest.mark.parametrize("restaurant, item, new_description, new_price, expected", [
    ("Cafe Mocha", "Mocha", "Great coffee and pastries", -3.5, "Price must be positive."),
    ("Sushi Express", "Sushi", "Fresh sushi", -5.5, "Price must be positive."),
    ("Cafe Mocha", "Latte", "Great coffee and pastries", -3.5, "Price must be positive."),
    ("Sushi Express", "Sashimi", "Fresh sashimi", -6.5, "Price must be positive.")
])
def test_update_menu_item_with_negative_price(restaurant, item, new_description, new_price, expected):
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    menu.add_menu_item("Sushi Express", "Sashimi", "Fresh sashimi", 6.5)
    with pytest.raises(ValueError) as e:
        menu.update_menu_item(restaurant, item, new_description, new_price)
    assert str(e.value) == expected

@pytest.mark.parametrize("restaurant, item, new_description, new_price, expected", [
    ("Starbucks", "Mocha", "Great coffee and pastries", 3.5, ValueError),
    ("McDonalds", "Sushi", "Fresh sushi", 5.5, ValueError),
    ("KFC", "Latte", "Great coffee and pastries", 3.5, ValueError),
    ("Pizza Hut", "Sashimi", "Fresh sashimi", 6.5, ValueError)
])
def test_update_menu_item_with_non_existing_restaurant(restaurant, item, new_description, new_price, expected):
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    menu.add_menu_item("Sushi Express", "Sashimi", "Fresh sashimi", 6.5)
    with pytest.raises(expected) as e:
        menu.update_menu_item(restaurant, item, new_description, new_price)
    assert str(e.value) == "No such restaurant exists."

@pytest.mark.parametrize("restaurant, item, new_description, new_price, expected", [
    ("Cafe Mocha", "Cappuccino", "Great coffee and pastries", 3.5, ValueError),
    ("Sushi Express", "Tacos", "Fresh sashimi", 6.5, ValueError)
])
def test_update_menu_item_with_non_existing_item(restaurant, item, new_description, new_price, expected):
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    menu.add_menu_item("Sushi Express", "Sashimi", "Fresh sashimi", 6.5)
    with pytest.raises(expected) as e:
        menu.update_menu_item(restaurant, item, new_description, new_price)
    assert str(e.value) == "No such item exists."

@pytest.mark.parametrize("restaurant, item, new_description, new_price, expected", [
    ("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5, "Menu item updated for Cafe Mocha."),
    ("Sushi Express", "Sushi", "Fresh sushi", 5.5, "Menu item updated for Sushi Express."),
    ("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5, "Menu item updated for Cafe Mocha."),
    ("Sushi Express", "Sashimi", "Fresh sashimi", 6.5, "Menu item updated for Sushi Express.")
])
def test_update_menu_item_with_fixture(menu_with_some_item, restaurant, item, new_description, new_price, expected):
    result = menu_with_some_item.update_menu_item(restaurant, item, new_description, new_price)
    assert result == expected

@pytest.mark.parametrize("restaurant, item, new_description, new_price, expected", [
    ("Cafe Mocha", "Mocha", "Great coffee and pastries", -3.5, "Price must be positive."),
    ("Sushi Express", "Sushi", "Fresh sushi", -5.5, "Price must be positive."),
    ("Cafe Mocha", "Latte", "Great coffee and pastries", -3.5, "Price must be positive."),
    ("Sushi Express", "Sashimi", "Fresh sashimi", -6.5, "Price must be positive.")
])
def test_update_menu_item_with_fixture_and_negative_price(menu_with_some_item, restaurant, item, new_description, new_price, expected):
    with pytest.raises(ValueError) as e:
        menu_with_some_item.update_menu_item(restaurant, item, new_description, new_price)
    assert str(e.value) == expected

@pytest.mark.parametrize("restaurant, item, new_description, new_price, expected", [
    ("Starbucks", "Mocha", "Great coffee and pastries", 3.5, ValueError),
    ("McDonalds", "Sushi", "Fresh sushi", 5.5, ValueError),
    ("KFC", "Latte", "Great coffee and pastries", 3.5, ValueError),
    ("Pizza Hut", "Sashimi", "Fresh sashimi", 6.5, ValueError)
])
def test_update_menu_item_with_fixture_and_non_existing_restaurant(menu_with_some_item, restaurant, item, new_description, new_price, expected):
    with pytest.raises(expected) as e:
        menu_with_some_item.update_menu_item(restaurant, item, new_description, new_price)
    assert str(e.value) == "No such restaurant exists."

@pytest.mark.parametrize("restaurant, item, new_description, new_price, expected", [
    ("Cafe Mocha", "Cappuccino", "Great coffee and pastries", 3.5, ValueError),
    ("Sushi Express", "Tacos", "Fresh sashimi", 6.5, ValueError)
])
def test_update_menu_item_with_fixture_and_non_existing_item(menu_with_some_item, restaurant, item, new_description, new_price, expected):
    with pytest.raises(expected) as e:
        menu_with_some_item.update_menu_item(restaurant, item, new_description, new_price)
    assert str(e.value) == "No such item exists."
