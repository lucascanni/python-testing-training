import pytest

from implementations.restaurant_reviews import RestaurantReviews
from fixture.restaurant_reviews_fixture import restaurant_reviews_with_two_reviews

# Parametrization delete review existant
@pytest.mark.parametrize("restaurant, expected", [
    ("Cafe Mocha", "Review deleted for Cafe Mocha."),
    ("Sushi Express", "Review deleted for Sushi Express."),
])
def test_delete_review(restaurant_reviews_with_two_reviews, restaurant, expected):
    assert restaurant_reviews_with_two_reviews.get_review(restaurant) != None
    assert restaurant_reviews_with_two_reviews.delete_review(restaurant) == expected
    with pytest.raises(ValueError):
        restaurant_reviews_with_two_reviews.get_review(restaurant)

# Parametrization delete review non existant
@pytest.mark.parametrize("restaurant, expected", [
    ("Cafe Pizza", ValueError),
    ("Cafe Burger", ValueError),
])
def test_delete_invalid_review(restaurant_reviews_with_two_reviews,restaurant, expected):
    with pytest.raises(expected):
        restaurant_reviews_with_two_reviews.delete_review(restaurant)

