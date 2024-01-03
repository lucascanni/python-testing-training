import pytest

from implementations.menu import Menu
from fixture.menu_fixture import menu_with_some_item

@pytest.mark.parametrize("restaurant,  expected", [
    ("Cafe Mocha", {"Mocha": {"desription": "Great coffee and pastries", "price": 3.5}, "Latte": {"desription": "Great coffee and pastries", "price": 3.5}}),
    ("Sushi Express", {"Sushi": {"desription": "Fresh sushi", "price": 5.5}, "Sashimi": {"desription": "Fresh sashimi", "price": 6.5}}),
])
def test_get_menu_item(restaurant, expected):
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    menu.add_menu_item("Sushi Express", "Sashimi", "Fresh sashimi", 6.5)
    result = menu.get_menu_item(restaurant)
    assert result == expected

@pytest.mark.parametrize("restaurant, expected", [
    ("Starbucks", ValueError),
    ("McDonalds", ValueError),
    ("KFC", ValueError),
    ("Pizza Hut", ValueError),
])
def test_get_menu_item_with_non_existing_restaurant(restaurant, expected):
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    menu.add_menu_item("Sushi Express", "Sashimi", "Fresh sashimi", 6.5)
    with pytest.raises(expected) as e:
        menu.get_menu_item(restaurant)
    assert str(e.value) == "No such restaurant exists."

@pytest.mark.parametrize("restaurant,  expected", [
    ("Cafe Mocha", {"Mocha": {"desription": "Great coffee and pastries", "price": 3.5}, "Latte": {"desription": "Great coffee and pastries", "price": 3.5}}),
    ("Sushi Express", {"Sushi": {"desription": "Fresh sushi", "price": 5.5}, "Sashimi": {"desription": "Fresh sashimi", "price": 6.5}}),
])
def test_get_menu_item_with_fixture(menu_with_some_item, restaurant, expected):
    assert menu_with_some_item.get_menu_item(restaurant) == expected

@pytest.mark.parametrize("restaurant, expected", [
    ("Starbucks", ValueError),
    ("McDonalds", ValueError),
    ("KFC", ValueError),
    ("Pizza Hut", ValueError),
])
def test_get_menu_item_with_fixture_and_non_existing_restaurant(menu_with_some_item, restaurant, expected):
    with pytest.raises(expected) as e:
        menu_with_some_item.get_menu_item(restaurant)
    assert str(e.value) == "No such restaurant exists."