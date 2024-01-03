import pytest

from implementations.menu import Menu
from fixture.menu_fixture import menu_with_some_item

@pytest.mark.parametrize("restaurant, item, expected", [
    ("Cafe Mocha", "Mocha", "Menu item deleted for Cafe Mocha."),
    ("Sushi Express", "Sushi", "Menu item deleted for Sushi Express."),
    ("Cafe Mocha", "Latte", "Menu item deleted for Cafe Mocha."),
    ("Sushi Express", "Sashimi", "Menu item deleted for Sushi Express.")
])
def test_delete_menu_item(menu_with_some_item, restaurant, item, expected):
    assert menu_with_some_item.delete_menu_item(restaurant, item) == expected

@pytest.mark.parametrize("restaurant, item, expected", [
    ("Starbucks", "Mocha", ValueError),
    ("McDonalds", "Sushi", ValueError),
    ("KFC", "Latte", ValueError),
    ("Pizza Hut", "Sashimi", ValueError),
])
def test_delete_menu_item_with_non_existing_restaurant(restaurant, item, expected):
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    menu.add_menu_item("Sushi Express", "Sashimi", "Fresh sashimi", 6.5)
    with pytest.raises(expected) as e:
        menu.delete_menu_item(restaurant, item)
    assert str(e.value) == "No such restaurant exists."

@pytest.mark.parametrize("restaurant, item, expected", [
    ("Cafe Mocha", "Cappuccino", ValueError),
    ("Sushi Express", "Tacos", ValueError)
])
def test_delete_menu_item_with_non_existing_item(restaurant, item, expected):
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    menu.add_menu_item("Sushi Express", "Sashimi", "Fresh sashimi", 6.5)
    with pytest.raises(expected) as e:
        menu.delete_menu_item(restaurant, item)
    assert str(e.value) == "No such item exists."

@pytest.mark.parametrize("restaurant, item, expected", [
    ("Cafe Mocha", "Mocha", "Menu item deleted for Cafe Mocha."),
    ("Sushi Express", "Sushi", "Menu item deleted for Sushi Express."),
    ("Cafe Mocha", "Latte", "Menu item deleted for Cafe Mocha."),
    ("Sushi Express", "Sashimi", "Menu item deleted for Sushi Express.")
])
def test_delete_menu_item_with_fixture(menu_with_some_item, restaurant, item, expected):
    assert menu_with_some_item.delete_menu_item(restaurant, item) == expected

@pytest.mark.parametrize("restaurant, item, expected", [
    ("Starbucks", "Mocha", ValueError),
    ("McDonalds", "Sushi", ValueError),
    ("KFC", "Latte", ValueError),
    ("Pizza Hut", "Sashimi", ValueError),
])
def test_delete_menu_item_with_fixture_and_non_existing_restaurant(menu_with_some_item, restaurant, item, expected):
    with pytest.raises(expected) as e:
        menu_with_some_item.delete_menu_item(restaurant, item)
    assert str(e.value) == "No such restaurant exists."

@pytest.mark.parametrize("restaurant, item, expected", [
    ("Cafe Mocha", "Cappuccino", ValueError),
    ("Sushi Express", "Tacos", ValueError)
])
def test_delete_menu_item_with_fixture_and_non_existing_item(menu_with_some_item, restaurant, item, expected):
    with pytest.raises(expected) as e:
        menu_with_some_item.delete_menu_item(restaurant, item)
    assert str(e.value) == "No such item exists."