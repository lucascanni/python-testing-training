import pytest

from implementations.menu import Menu
from fixture.menu_fixture import menu_with_some_item

def test_get_menu_item():
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    result = menu.get_menu_item("Cafe Mocha")
    assert result == {"Mocha": {"desription": "Great coffee and pastries", "price": 3.5}, "Latte": {"desription": "Great coffee and pastries", "price": 3.5}}

def test_get_menu_item_with_non_existing_restaurant():
    menu = Menu()
    with pytest.raises(ValueError) as e:
        menu.get_menu_item("Starbucks")
    assert str(e.value) == "No such restaurant exists."

def test_get_menu_item_with_fixture(menu_with_some_item):
    assert menu_with_some_item.get_menu_item("Cafe Mocha") == {"Mocha": {"desription": "Great coffee and pastries", "price": 3.5}, "Latte": {"desription": "Great coffee and pastries", "price": 3.5}}
    assert menu_with_some_item.get_menu_item("Sushi Express") == {"Sushi": {"desription": "Fresh sushi", "price": 5.5}, "Sashimi": {"desription": "Fresh sashimi", "price": 6.5}}
    assert menu_with_some_item.get_menu_item("Cafe Mocha") != {"Sushi": {"desription": "Fresh sushi", "price": 5.5}, "Sashimi": {"desription": "Fresh sashimi", "price": 6.5}}
    assert menu_with_some_item.get_menu_item("Sushi Express") != {"Mocha": {"desription": "Great coffee and pastries", "price": 3.5}, "Latte": {"desription": "Great coffee and pastries", "price": 3.5}}

def test_get_menu_item_with_fixture_and_non_existing_restaurant(menu_with_some_item):
    with pytest.raises(ValueError) as e:
        menu_with_some_item.get_menu_item("Starbucks")
    assert str(e.value) == "No such restaurant exists."