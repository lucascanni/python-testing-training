import pytest

from implementations.menu import Menu
from fixture.menu_fixture import menu_with_some_item

def test_update_menu_item():
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    result = menu.update_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    assert result == "Menu item updated for Cafe Mocha."

def test_update_menu_item_with_negative_price():
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    with pytest.raises(ValueError) as e:
        menu.update_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", -3.5)
    assert str(e.value) == "Price must be positive."

def test_update_menu_item_with_non_existing_restaurant():
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    with pytest.raises(ValueError) as e:
        menu.update_menu_item("Starbucks", "Mocha", "Great coffee and pastries", 3.5)
    assert str(e.value) == "No such restaurant exists."

def test_update_menu_item_with_non_existing_item():
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    with pytest.raises(ValueError) as e:
        menu.update_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    assert str(e.value) == "No such item exists."

def test_update_menu_item_with_fixture(menu_with_some_item):
    result = menu_with_some_item.update_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    assert result == "Menu item updated for Cafe Mocha."

def test_update_menu_item_with_fixture_and_negative_price(menu_with_some_item):
    with pytest.raises(ValueError) as e:
        menu_with_some_item.update_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", -3.5)
    assert str(e.value) == "Price must be positive."

def test_update_menu_item_with_fixture_and_non_existing_restaurant(menu_with_some_item):
    with pytest.raises(ValueError) as e:
        menu_with_some_item.update_menu_item("Starbucks", "Mocha", "Great coffee and pastries", 3.5)
    assert str(e.value) == "No such restaurant exists."

def test_update_menu_item_with_fixture_and_non_existing_item(menu_with_some_item):
    with pytest.raises(ValueError) as e:
        menu_with_some_item.update_menu_item("Cafe Mocha", "Cappuccino", "Great coffee and pastries", 3.5)
    assert str(e.value) == "No such item exists."
