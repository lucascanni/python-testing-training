import pytest

from implementations.restaurant_reviews import RestaurantReviews

# Parametrization
@pytest.mark.parametrize("restaurant, review_text, rating, expected", [
    ("Cafe Mocha", "Great coffee and pastries", 4, "Review added for Cafe Mocha."),
    ("Cafe Mocha", "Great coffee and pastries", 6, ValueError("Invalid Rating. It must be between 1 and 5." )),
    ("Cafe Mocha", "Great coffee and pastries", 0, ValueError("Invalid Rating. It must be between 1 and 5." )),
])

def test_add_review(restaurant, review_text, rating, expected):
    reviews = RestaurantReviews()
    result = reviews.add_review(restaurant, review_text, rating)
    assert result == expected
    assert reviews.get_review(restaurant) == {"review_text": review_text, "rating": rating}