import pytest

from implementations.menu import Menu

@pytest.fixture
def menu_with_some_item():
    menu = Menu()
    menu.add_menu_item("Cafe Mocha", "Mocha", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Cafe Mocha", "Latte", "Great coffee and pastries", 3.5)
    menu.add_menu_item("Sushi Express", "Sushi", "Fresh sushi", 5.5)
    menu.add_menu_item("Sushi Express", "Sashimi", "Fresh sashimi", 6.5)
    return menu