import pytest

from implementations.restaurant_reviews import RestaurantReviews

def test_add_review():
    reviews = RestaurantReviews()
    result = reviews.add_review("Cafe Mocha", "Great coffee and pastries", 4)
    assert result == "Review added for Cafe Mocha."
    assert reviews.get_review("Cafe Mocha") == {"review_text": "Great coffee and pastries", "rating": 4}

def test_add_invalid_rating():
    reviews = RestaurantReviews()
    with pytest.raises(ValueError):
        reviews.add_review("Cafe Mocha", "Great coffee and pastries", 6)
    with pytest.raises(ValueError):
        reviews.add_review("Cafe Mocha", "Great coffee and pastries", 0)