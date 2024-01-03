import pytest
from fixture.menu_fixture import menu_with_some_item

def test_get_menu_item(menu_with_some_item):
    assert menu_with_some_item.get_menu_item("Cafe Mocha") == {"Mocha": {"desription": "Great coffee and pastries", "price": 3.5}, "Latte": {"desription": "Great coffee and pastries", "price": 3.5}}
    assert menu_with_some_item.get_menu_item("Sushi Express") == {"Sushi": {"desription": "Fresh sushi", "price": 5.5}, "Sashimi": {"desription": "Fresh sashimi", "price": 6.5}}
    assert menu_with_some_item.get_menu_item("Cafe Mocha") != {"Sushi": {"desription": "Fresh sushi", "price": 5.5}, "Sashimi": {"desription": "Fresh sashimi", "price": 6.5}}
    assert menu_with_some_item.get_menu_item("Sushi Express") != {"Mocha": {"desription": "Great coffee and pastries", "price": 3.5}, "Latte": {"desription": "Great coffee and pastries", "price": 3.5}}