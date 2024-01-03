import pytest

from implementations.restaurant_reviews import RestaurantReviews
from fixture.restaurant_reviews_fixture import restaurant_reviews_with_two_reviews

# Parametrization get review existant
@pytest.mark.parametrize("restaurant, expected", [
    ("Cafe Mocha", {"review_text": "Great coffee and pastries", "rating": 4}),
    ("Sushi Express", {"review_text": "Fresh sushi", "rating": 4}),
])
def test_get_review(restaurant_reviews_with_two_reviews, restaurant, expected):
    assert restaurant_reviews_with_two_reviews.get_review(restaurant) == expected

# Parametrization get review non existant
@pytest.mark.parametrize("restaurant, expected", [
    ("Cafe Pizza", ValueError),
    ("Cafe Burger", ValueError),
])
def test_get_invalid_review(restaurant_reviews_with_two_reviews,restaurant, expected):
    with pytest.raises(expected):
        restaurant_reviews_with_two_reviews.get_review(restaurant)